# fastapi-kickstart

## Prerequisites
Conda

## Installation

```bash
conda env create --file environment.yml
```

## Activate Environment

```bash
conda activate fastapi-kickstart
```

## Start uvicorn

```bash
uvicorn main:app --reload
```

## Run tests

```bash
python -m pytest
```

Show Coverage Results in Terminal
```bash
python -m pytest --cov-config=.coveragerc --cov=./
```

Generate HTML Coverage Report
```bash
python -m pytest --cov-config=.coveragerc --cov=./ --cov-report=html
```