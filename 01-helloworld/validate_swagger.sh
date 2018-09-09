#!/bin/bash
for i in `find . -name "swagger.yaml" -type f`; do
    echo "validating $i"
    pipenv run openapi-spec-validator --schema 2.0 $i
done