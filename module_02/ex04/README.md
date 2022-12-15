# About
my_minipack package consists of 2 modules:
* The progress bar (module_00/ex10) which should be imported it via ```import my_minipack.progressbar```
* The logger (module_02/ex02), which should be imported via ```import my_minipack.logger```

## Usage
Run the script by running the following command:
```./build.sh```
This will upgrade pip if necessary, and then build my_minipack package in both wheel and egg format.
The built packages will be saved to a dist directory, which will be created if it does not already exist.
Once the script finishes running, you can install your package using pip by running the following command:
* ```pip install ./dist/my_minipack-1.0.0.tar.gz```</br>
Alternatively, you can use:
* ```my_minipack-1.0.0-py3-none-any.whl``` file in the ```dist``` directory to install the package.
