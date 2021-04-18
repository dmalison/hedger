PYTHON := python3
VENV := .venv
SRC := marchmadness/
TESTS := tests/


.PHONY: venv
venv: 
	${PYTHON} -m venv ${VENV}
	./$(VENV)/bin/pip install -r requirements.txt

.PHONY: clean
clean:
	rm -rf ${VENV}
	find . -type f -name '*.pyc'

.PHONY: lint
lint:
	${PYTHON} -m flake8 ${SRC} ${TESTS}

.PHONY: test
test:
	${PYTHON} -m pytest ${TESTS}

.PHONY: coverage
coverage:
	coverage run --source=${SRC} -m pytest ${TESTS}
	coverage report -m
