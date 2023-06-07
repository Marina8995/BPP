virtualenv env
env\Scripts\activate
pip install pyqt5
pip install sphinx sphinx_rtd_theme
mkdir docs
cd docs
sphinx-quickstart
cd..
sphinx-apidoc -o docs proyecto1/
make html
