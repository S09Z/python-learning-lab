# Define the Python version
PYTHON_VERSION=3.10.11

# Define the pyenv and poetry commands
PYENV=$(shell pyenv which pyenv)
POETRY=$(shell which poetry)

# Default target
all: setup

# Target to set local Python version and configure Poetry
setup:
	@echo "Setting local Python version with pyenv..."
	@pyenv local $(PYTHON_VERSION)
	@echo "Configuring Poetry to use the specified Python version..."
	@$(POETRY) env use $(shell pyenv which python)

# Additional target to install dependencies
install:
	@echo "Installing dependencies with Poetry..."
	@$(POETRY) lock --no-update   
	@$(POETRY) install

# Clean up virtual environment
clean:
	@echo "Removing Poetry virtual environment..."
	@$(POETRY) env remove $(shell pyenv which python)
