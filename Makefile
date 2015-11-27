MANAGE=python manage.py
LOCALE=ru_RU.UTF-8

# Targets
default: run

run:
	$(MANAGE) runserver

syncdb:
	$(MANAGE) syncdb

shell:
	$(MANAGE) shell

dbshell:
	$(MANAGE) dbshell

### End: ***
