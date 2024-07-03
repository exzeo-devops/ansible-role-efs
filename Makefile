###############################################################################
### Ansible
###############################################################################
install:
	pipenv install --dev

shell: install
	pipenv shell

test: install
	pipenv run molecule test --all

###############################################################################
### Git Hooks
###############################################################################
run-pre-commit-hooks:
	pre-commit run --all-files

install-pre-commit-hooks:
	pre-commit install
	pre-commit install-hooks
