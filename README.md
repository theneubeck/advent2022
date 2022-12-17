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

## dotnet

```bash
dotnet new sln
cd src
dotnet new console -o day1
dotnet sln add src/day1/day1.csproj
dotnet new xunit -o tests/day1.tests
dotnet add tests/day1.tests/day1.tests.csproj reference src/day1/day1.csproj
dotnet sln add tests/day1.tests/day1.tests.csproj

```
