all: install_dependencies build_playwrigth
install_dependencies:
	@echo "Instalando as dependencias do python"
	pip install -r requeriments.txt
	@echo "# FINALIZADO -----------------------"
build_playwrigth:
	@echo "instalando dependencias do playwright"
	playwright install-deps
	playwright install
	@echo "# FINALIZADO -----------------------"

	@echo "# Now you can use Python3 main.py"