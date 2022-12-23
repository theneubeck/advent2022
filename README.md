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
dotnet new console -o src/Day1
dotnet sln add src/Day1/Day1.csproj
dotnet new xunit -o tests/Day1.Tests
dotnet add tests/Day1.Tests/Day1.Tests.csproj reference src/Day1/Day1.csproj
dotnet sln add tests/Day1.Tests/Day1.Tests.csproj

```
