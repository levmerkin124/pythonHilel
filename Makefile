name: test with poetry

on: pull_request

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      #----------------------------------------------
      #       check-out repo and set-up python
      #----------------------------------------------
      - name: Check out repository
        uses: actions/checkout@v3
      - name: Set up python
        id: setup-python
        uses: actions/setup-python@v4
        with:
          python-version: '3.12'
      #----------------------------------------------
      #  -----  install & configure poetry  -----
      #----------------------------------------------
      - name: Install Poetry
        uses: snok/install-poetry@v1
        with:
          virtualenvs-create: true
          virtualenvs-in-project: true
          installer-parallel: true
      #----------------------------------------------
      #       load cached venv if cache exists
      #----------------------------------------------
      - name: Load cached venv
        id: cached-poetry-dependencies
        uses: actions/cache@v3
        with:
          path: .venv
          key: venv-${{ runner.os }}-${{ steps.setup-python.outputs.python-version }}-${{ hashFiles('**/poetry.lock') }}
      #----------------------------------------------
      # install dependencies if cache does not exist
      #----------------------------------------------
      - name: Install dependencies
        run: poetry install --no-interaction --no-root
      #----------------------------------------------
      # install your root project, if required
      #----------------------------------------------
      - name: Install project
        run: poetry install --no-interaction
      #----------------------------------------------
      #              run test suite
      #----------------------------------------------
      - name: Run tests
        run: |
          source .venv/bin/activate
          isort .
          flake8 .