PYTHON := python3
VENV := .venv


.PHONY: venv
venv: 
	${PYTHON} -m venv ${VENV}
	./$(VENV)/bin/pip install -r requirements.txt

.PHONY: clean
clean:
	rm -rf ${VENV}


SRC := marchmadness/
TESTS := tests/

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
