# click-sample

Sample code for CLI tool which generates YAML file, 
using Python package [Click](https://github.com/pallets/click).

## Usage

### Prepare

```bash
$ python3 -m venv venv
$ source env/bin/activate
$ python --version 
$ pip install -r requirements.txt
```

```bash
$ git clone git@github.com:takp/click-sample.git
$ cd click-sample
$ pip install --editable .
$ click --help
```

### Run

```bash
$ click
Your project name: sample project
Created output.yml.
```
