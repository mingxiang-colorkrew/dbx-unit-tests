## How to Use

- main coding of notebooks is done within Databricks Browser or locally via Databricks Connect
- Git can be managed from external repository (e.g. Github) and using Git GUIs (e.g. VSCode)
- Can choose to write python code directly and upload it for exection
- Can use external tools to format code (e.g. [black](https://github.com/psf/black))

## Setup Local Dependencies


```bash
# install poetry CLI tool to manage package dependencies
curl -sSL https://install.python-poetry.org | python3 -

# install dependencies
poetry install

# install nutter CLI tool
pip install nutter

# set DATABRICKS_HOST and DATABRICKS_TOKEN ENV variables for nutter
export DATABRICKS_HOST=""
export DATABRICKS_TOKEN=""
```

## Usage

You can use Nutter CLI to list and run tests

``` bash
# list tests
nutter list /Repos/<namespace>/dbx-unit-tests/project/tests/ --recursive

# execute notebook tests
nutter list /Repos/<namespace>/dbx-unit-tests/project/tests/ --cluster_id <cluster-id> --recursive

# execute python unit tests
python -m unittest project/tests/core/**/*.py
```

You can format all code in the repo using

```bash
poetry run black .
```


