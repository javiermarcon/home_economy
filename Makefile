all: help

.PHONY: check_git_tree next_version

help:
	@echo "Comandos android:"
	@echo "    apk - Compila la aplicación generando un archivo apk en la carpeta bin"
	@echo "    android_deploy - instala el apk en el celular"
	@echo "    android_run - corre el apk en el celular"
	@echo "    android_logcat - captura salida de la aplicacion en el celular"
	@echo "     - "

check_git_tree:
	@if [ "`git status --untracked-files=no --porcelain`" != "" ]; then \
		echo "Hay archivos sin comitear, comitealos antes de seguir..."; \
		exit 1; \
	fi

# Compila la aplicación generando un archivo apk en la carpeta bin
apk: check_git_tree next_version
	@echo "compilando apk"
	buildozer android debug

# incrementa la versión de la aplicación
next_version:
	bumpversion patch

# instala el apk en el celular
android_deploy: apk
	buildozer android deploy

# corre el apk en el celular
android_run: android_deploy
	buildozer android run

# captura salida de la aplicacion en el celular
android_logcat: android_deploy
	buildozer android logcat
