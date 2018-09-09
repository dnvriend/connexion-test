.PHONY: help init clean run docker-build docker-run docker-shell test
.DEFAULT_GOAL := run

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

init: ## init python
	@pipenv install --three --dev

clean: ## clean
	@pipenv --rm

run: test ## run the example
	@pipenv run python app.py

mock:
	@pipenv run connexion run swagger.yaml --mock=all -v --port=8080

docker-build: ## build the docker image
	@docker build -t connexion-test .

docker-run: ## run the docker container
	@docker run -d -p 8080:8080 connexion-test

docker-shell: ## access the container shell
	@docker run -it connexion-test /bin/bash

test: ## validate swagger
	@./validate_swagger.sh
