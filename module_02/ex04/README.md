## About
my_minipack package consists of 2 modules:
* The progress bar (module_00/ex10) which should be imported it via ```import my_minipack.progressbar```
* The logger (module_02/ex02), which should be imported via ```import my_minipack.logger```

## Usage
Run the script by running the following command:
```./build.sh```
This will upgrade pip if necessary, and then build my_minipack package in both wheel and egg format.
The built packages will be saved to a dist directory, which will be created if it does not already exist.
Once the script finishes running, you can install your package using pip by running either one of the following commands:
* ```pip install ./dist/my_minipack-1.0.0.tar.gz``` file in the ```dist``` directory to install the package.
* ```pip install ./dist/my_minipack-1.0.0-py3-none-any.whl``` file in the ```dist``` directory to install the package.

## Virtual environment usage
Python “Virtual Environments” allow Python packages to be installed in an isolated location for a particular application, rather than being installed globally
Then you can proceed by using the following commands:
* ```python -m venv tmp_env && source tmp_env/bin/activate```
* ~~```pip list```~~
* ```bash build.sh```
* ```pip install ./dist/my_minipack-1.0.0.tar.gz || pip install ./dist/my_minipack-1.0.0-py3-none-any.whl```
* ~~```ls dist```~~
* ~~```pip list```~~
* ```pip show -v my_minipack```


## Structure
A python package has to be comprised of the following files according to a similar file structure (one the two setup files is enough):
```
ex02/
├─ LICENSE.md
├─ pyproject.toml
├─ README.md 
├─ setup.py
├─ build.sh
├─ src/
|  └───my_minipack/
│      ├── __init__.py
│      ├── logger.py
│      └── progressbar.py
└── tests/
```