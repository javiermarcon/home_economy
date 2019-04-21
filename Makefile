all: help

.PHONY: check_git_tree patchversion docs

help:
	@echo "Comandos android:"
	@echo "    apk - Compila la aplicación generando un archivo apk en la carpeta bin."
	@echo "    android_deploy - instala el apk en el celular."
	@echo "    android_run - corre el apk en el celular."
	@echo "    android_logcat - captura salida de la aplicacion en el celular."
	@echo ""
	@echo "Documentacion:"
	@echo "    docs - Genera documentación HTML con sphinx y luego la abre."
	@echo ""
	@echo "Git:"
	@echo "    commit - Hace commit agregando archivos .py y .kv e incrementando la version de la app."
	@echo "             hay que pasarle la variable msg. make commit msg="mensaje de commit"

check_git_tree:
	@if [ "`git status --untracked-files=no --porcelain`" != "" ]; then \
		echo "Hay archivos sin comitear, comitealos antes de seguir..."; \
		exit 1; \
	fi

# Compila la aplicación generando un archivo apk en la carpeta bin
apk: patchversion
	@echo "compilando apk"
	buildozer android debug

# incrementa la versión de la aplicación
patchversion majorversion minorversion: check_git_tree
	bumpversion $(subst version,,$@)

# instala el apk en el celular
android_deploy: apk
	buildozer android deploy

# corre el apk en el celular
android_run: android_deploy
	buildozer android run

# captura salida de la aplicacion en el celular
android_logcat: android_deploy
	buildozer android logcat

docs:
	$(MAKE) -C docs html
	xdg-open docs/build/html/index.html

check_msg_var:
	@:$(call check_defined, msg)

# Check that given variables are set and all have non-empty values,
# die with an error otherwise.
#
# Params:
#   1. Variable name(s) to test.
#   2. (optional) Error message to print.
check_defined = \
    $(strip $(foreach 1,$1, \
        $(call __check_defined,$1,$(strip $(value 2)))))
__check_defined = \
    $(if $(value $1),, \
      $(error Variable $1$(if $2, ($2)) no definida. Por favor corra el makefile con $1$(if $2, ($2))="..."))

git_commit: check_msg_var
	# root files 
	git add ./Makefile ./readme.md ./buildozer.spec ./.bumpversion.cfg
	# requirements
	git add ./src/requirements*.txt
	# documents
	git add ./doc/*
	git add ./docs/build/html/*
	# python files
	@find src -iname "*.py" -type f -exec git add {} \;
	# perform commit
	git commit -m "$(msg)"

commit: | git_commit patchversion
