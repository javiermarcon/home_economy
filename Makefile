all: apk

.PHONY: check_git_tree next_version


check_git_tree:
	@if [ "`git status --untracked-files=no --porcelain`" != "" ]; then \
		echo "Hay archivos sin comitear, comitealos antes de seguir..."; \
		exit 1; \
	fi

# Compila la aplicación generando un archivo apk en la carpeta bin
apk: check_git_tree next_version
	echo "compilando apk"
	buildozer android debug

# incrementa la versión de la aplicación
next_version:
	bumpversion patch
