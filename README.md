# Py File &amp; Folder Encrypt CLI App

Encrypt & decrypt file or folder

CLI app included in distribution folder (dist/py-encrypt-cli.exe)

![](./py-encrypt-cli-ss.jpg)

## Basic Usage
1. Help
```
py py-encrypt-cli -h
```
2. Generate file "filekey.key" with key
```
py py-encrypt-cli -gk true
```
3. Generate file "filekey.key" with key
```
py py-encrypt-cli -gk true
```


## Setup for Local Development

1. Creating a virtual environment
```
py -m venv venv
```
2. Activate the environment
```
.\venv\Scripts\activate
```
3. Install all of the packages using requirements.txt
```
pip install -r requirements.txt
```
4. Run cli application 
```
py py-encrypt-cli.py -h
```
5. Build cli output (more refer to : https://pyinstaller.org/en/stable/usage.html)
```
pyinstaller py-encrypt-cli.spec
```
6. Export a list of all installed packages (Optional)
```
pip freeze > requirements.txt
```
7. Leaving the environment
```
deactivate
```

## Reference Links
- https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/
- https://docs.python.org/3/library/index.html
- https://docs.python.org/3/library/argparse.html
- https://cryptography.io/
- https://pyinstaller.org/en/stable/usage.html
- https://pyinstaller.org/en/stable/man/pyi-makespec.html

