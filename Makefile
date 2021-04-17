PYTHON := python3
VENV := .venv

.PHONY: venv
venv: 
	${PYTHON} -m venv ${VENV}
	./$(VENV)/bin/pip install -r requirements.txt

.PHONY: clean
clean:
	rm -rf ${VENV}
