#!/bin/bash
covered=`jq .totals.percent_covered ./ops/tmp/coverage-summary.json`
covered=${covered%.*}
if [ ${covered} -lt 70 ]; then
        echo the covered on code coverage is $covered % need to check all test functionlty >&2
        exit 1
else
    exit 0
fi
