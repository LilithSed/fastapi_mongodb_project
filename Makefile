# Variables
# --------------------------------------------------------------------------------------
CONTAINER_NAME := MAIN

# All phony commands are listed here
.PHONY: \
	all \
	clean \
	env \
	ready \
	pre-commit-install \
	pre-commit-run \
	pre-commit-update \
	docker \
	docker-pytest-run \
	docker-bash \
	docker-build \
	docker-run \
	docker-logs \
	docker-test \
	docker-coverage \
	docker-pytest \
	docker-test-coverage-report \
	docker-test-coverage-html \
	test \
	test-pytest \
	test-coverage \
	test-coverage-report \
	test-coverage-html \
	sbom \
	docker-pre-commit-run \
	pre-commit-run-manual

# This command is used to prepare the development environment and run Docker containers
all: \
	env
	docker

# This command is used to prepare the development environment
env:
	cat .env.example >> .env

# This command is used to clean up the development environment
clean:
	./ops/scripts/clean.sh

# This command is used to prepare the repo with pre-commit hooks
ready: \
	pre-commit-install \
	pre-commit-update

# This command is used to install pre-commit hooks
pre-commit-install:
	# Install pre-commit hooks
	@pre-commit install

# This command is used to update pre-commit hooks
pre-commit-update:
	@pre-commit autoupdate

# This command is used to run pre-commit hooks on all files
pre-commit-run:
	@pre-commit run --all-files

pre-commit-run-manual:
	@pre-commit run --hook-stage manual --all-files

# This command is used to build and run Docker containers
docker: \
	docker-build \
	docker-run

docker-pytest-run:
	@docker exec $(CONTAINER_NAME) python -m pytest -vv --continue-on-collection-errors

docker-pre-commit-run:
	@docker exec $(CONTAINER_NAME) sh -c "make ready && make pre-commit-run-manual && make test"


# This command is used to build Docker containers
docker-build:
	@docker-compose build

# This command is used to run Docker containers
docker-run:
	@docker-compose up -d

# This command is used to view logs for Docker containers
docker-logs:
	@docker-compose logs -f

# This command is used to open a bash terminal in a running Docker container
docker-bash:
	@docker exec -it $(CONTAINER_NAME) bash

# This command is used to run tests in Docker containers
docker-test: \
	docker-coverage \
	docker-test-coverage-html

# This command is used to run Pytest in a Docker container
docker-pytest:
	@docker exec $(CONTAINER_NAME) python -m pytest -vv -s \
		--continue-on-collection-errors

# This command is used to run tests with coverage in Docker containers
docker-coverage:
	@docker exec $(CONTAINER_NAME) coverage run -m pytest

# This command is used to run tests with coverage in Docker containers
docker-coverage-json:
	docker exec $(CONTAINER_NAME) python -m pytest -vv \
		--continue-on-collection-errors \
		--cov-report json:./ops/tmp/coverage-summary.json

# This command is used to check code coverage in Docker containers
check-code-coverage:
	@docker exec $(CONTAINER_NAME) ./ops/scripts/check_code_coverage.sh

# This command is used to view coverage reports for tests run in Docker containers
docker-test-coverage-report:
	@docker exec $(CONTAINER_NAME) coverage report -m

# This command is used to view coverage reports in HTML format for tests run in
# Docker containers
docker-test-coverage-html:
	@docker exec $(CONTAINER_NAME) coverage html

# This command is used to generate cyclone
generate-cyclonedx-sbom:
	@docker exec $(CONTAINER_NAME) ops/scripts/generate-cyclone.sh

# This command is used to run tests locally
test:
	@python -m pytest

# This command is used to run Pytest locally
test-pytest:
	@python -m pytest

# This command is used to run tests with coverage locally
test-coverage:
	@coverage run -m pytest

# This command is used to view coverage reports for tests run locally
test-coverage-report:
	@coverage report -m

# This command is used to view coverage reports in HTML format for tests run locally
test-coverage-html:
	@coverage html

# Install CycloneDX BOM generator and generate a JSON and XML SBOM
sbom:
	@pip install -U cyclonedx-bom
	@cyclonedx-py -r -i ops/docker/requirements.txt -o bom.json --format json
	@cyclonedx-py -r -i ops/docker/requirements.txt -o bom.xml --format xml


local-install-kubeseal: ## This will install kubeseal locally
	wget https://github.com/bitnami-labs/sealed-secrets/releases/download/v${KUBESEAL_VERSION}/kubeseal-${KUBESEAL_VERSION}-linux-amd64.tar.gz
	tar -xvzf kubeseal-${KUBESEAL_VERSION}-linux-amd64.tar.gz kubeseal
	sudo install -m 755 kubeseal /usr/local/bin/kubeseal
	rm kubeseal-${KUBESEAL_VERSION}-linux-amd64.tar.gz
	rm kubeseal

kubeseal-save-private-key: ## This will save a copy of the kubeseal private key on the cluster
	kubectl get secret \
		-n kube-system \
		-l sealedsecrets.bitnami.com/sealed-secrets-key \
		-o yaml > main.key

create-sealed-secrets:
	kubeseal -o yaml < ops/kustomize/overlays/gcp-staging/secrets/firebase-service-account.yaml > ops/kustomize/overlays/gcp-staging/sealed-secrets/firebase-service-account-sealed.yaml
	kubeseal -o yaml < ops/kustomize/overlays/gcp-staging/secrets/google-service-account.yaml > ops/kustomize/overlays/gcp-staging/sealed-secrets/google-service-account-sealed.yaml
	kubeseal -o yaml < ops/kustomize/overlays/gcp-staging/secrets/tls-secret.yaml > ops/kustomize/overlays/gcp-staging/sealed-secrets/tls-secret-sealed.yaml
