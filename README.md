# Linguistic Measures

Tools for calculating linguistic measures and other useful utilities.

# Tabula rasa

* Usage on measures can be found [here](./measures/README.md)
* Usage on transformations can be found [here](./transforms/README.md)
* Usage on tools can be found [here](./tools/README.md)
* If you use these measures in an acedemic work, consider adding in one of [these](./references.bib) refrences.

# Prerequsits

The following packages need to be installed.
I recomend using [Chocolatey](https://chocolatey.org/install).
After [Python][python] is installed, the prerequsit packages need installed too.
If you want to modify the code, I recomend [VS Code][vscode].

* [Python][python]
* [VS Code][vscode] along with the below plugins
  * Python by Microsoft.

```{ps1}
if('Unrestricted' -ne (Get-ExecutionPolicy)) { Set-ExecutionPolicy Bypass -Scope Process -Force }
iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
refreshenv

choco install python3  -y
refreshenv
pip install -r requirements.txt

choco install vscode -y
refreshenv
code --install-extension ms-python.python
```

python: https://www.python.org/downloads/windows
vscode: https://code.visualstudio.com/Download
