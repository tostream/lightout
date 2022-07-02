# import config
include .devcontainer/devcontainer.env

.PHONY: all pipenv-install clean-pipenv pipenv-lock pipenv-rebuild-lock

all: clean pipenv-install

clean:
	pipenv --rm || true

pipenv-install:
	pipenv install --dev --deploy --ignore-pipfile
	
pipenv-lock:
	pipenv lock --dev --keep-outdated

pipenv-rebuild-lock:
	rm -f ./Pipfile.lock || pipenv --clear && pipenv lock --dev