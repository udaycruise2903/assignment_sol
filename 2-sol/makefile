# Define the virtual environment path and activate it
VENV = reward-venv
ACTIVATE = . $(VENV)/bin/activate

# Define the Django project settings module
DJANGO_SETTINGS_MODULE = myproject.settings

.PHONY: all test lint runserver migrate createsuperuser collectstatic

all: runserver

# Create the virtual environment
$(VENV):
	python3 -m venv $(VENV)

# Install Python dependencies
requirements: $(VENV) requirements.txt
	$(ACTIVATE) && pip install -r requirements.txt

# Run tests
test: $(VENV)
	$(ACTIVATE) && python manage.py test

# Start the development server
runserver: $(VENV)
	$(ACTIVATE) && python manage.py runserver

# Apply database migrations
migrate: $(VENV)
	$(ACTIVATE) && python manage.py migrate --settings=$(DJANGO_SETTINGS_MODULE)

# Create a superuser
createsuperuser: $(VENV)
	$(ACTIVATE) && python manage.py createsuperuser --settings=$(DJANGO_SETTINGS_MODULE)

# Collect static files
collectstatic: $(VENV)
	$(ACTIVATE) && python manage.py collectstatic --settings=$(DJANGO_SETTINGS_MODULE)