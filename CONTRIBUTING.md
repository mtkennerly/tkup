## Development
This project is managed using [Poetry](https://python-poetry.org/).
Development requires Python 3.9+.

* If you want to take advantage of the default VSCode integration, then first
  configure Poetry to make its virtual environment in the repository:
  ```
  poetry config virtualenvs.in-project true
  ```
* After cloning the repository, activate the tooling:
  ```
  poetry install
  poetry run pre-commit install
  ```
* Run unit tests:
  ```
  poetry run pytest
  ```
