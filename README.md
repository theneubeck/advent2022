# Some solutions to advent of code year 2022

## python

use poetry

```
poetry new --src <day>
cd <day>
poetry env use $(pyenv which python)
poetry add pytest --dev
poetry install
poetry run pytest
```