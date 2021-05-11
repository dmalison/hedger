PYTHON_VERSION := 3.8.9
VENV := .venv
SRC := hedger/
TESTS := tests/

.PHONY: python
ZSHRC := ~/.zshrc
python:
	brew upgrade pyenv
	pyenv install ${PYTHON_VERSION} -s
	pyenv local ${PYTHON_VERSION}
	if ! grep -Fq '$$(pyenv init -)' ${ZSHRC}; then \
		echo 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$$(pyenv init -)"\nfi' >> ${ZSHRC}; \
	fi;
	exec zsh

.PHONY: venv
venv:
	python -m venv ${VENV}
	./$(VENV)/bin/pip install -r requirements.txt

.PHONY: clean
clean:
	rm -rf ${VENV}
	find . -type f -name '*.pyc'

.PHONY: lint
lint:
	python -m flake8 ${SRC} ${TESTS}

.PHONY: test
test:
	python -m pytest ${TESTS}

.PHONY: coverage
coverage:
	coverage run --source=${SRC} -m pytest ${TESTS}
	coverage report -m
