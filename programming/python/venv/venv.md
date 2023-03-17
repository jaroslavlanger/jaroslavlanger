# venv

Virtual enviroment

## Contents <!-- omit in toc -->

- [Create virtual enviroment](#create-virtual-enviroment)
- [Activate the enviroment](#activate-the-enviroment)
- [Deactivation](#deactivation)
- [Modules requiring instalation outside of the enviroment](#modules-requiring-instalation-outside-of-the-enviroment)
- [Modules suitable for instalation inside of the venv](#modules-suitable-for-instalation-inside-of-the-venv)

## Create virtual enviroment

```sh
python3 -m venv /path/.nameoftheenv
```

## Activate the enviroment

```sh
source /path/.nameoftheenv/bin/activate
```

## Deactivation

```sh
deactivate
```

## Modules requiring instalation outside of the enviroment

```sh
pip3 install numpy
pip3 install matplotlib
pip3 install html5lib
```

## Modules suitable for instalation inside of the venv

```sh
pip3 install notebook
pip3 install requests
pip3 install pandas
pip3 install Cython
pip3 install -U scikit-learn
pip3 install seaborn
pip3 install lxml
pip3 install BeautifulSoup4
pip3 install xlrd
pip3 install pywebcopy
pip3 install pillow

pip3 install plotly
pip3 install -U kaleido
```

