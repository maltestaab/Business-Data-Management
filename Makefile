VENV = chanelenv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

# Default Task: Setup and Run
all: venv install run

# Create Virtual Environment
venv:
	python3 -m venv $(VENV)

# Install Dependencies
install: venv
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

# Run Main Script
run:
	$(PYTHON) chanel.py

# Clean Unnecessary Files
clean:
	rm -rf __pycache__ *.pyc
	rm -rf $(VENV)

# Help
help:
	@echo "make venv      - Create virtual environment"
	@echo "make install   - Install dependencies"
	@echo "make run       - Run the main script"
	@echo "make clean     - Remove virtual environment and cache"
	@echo "make all       - Setup and run everything"
