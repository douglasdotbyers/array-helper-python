# Array Helper

An array helper, in Python, which provides a method to divide an array into n parts.


 - Where the size of the array _can_ be divided equally by n:
    - All n parts are of the same size.


 - Where the size of the array _cannot_ be divided equally by n:
    - The first n-1 parts are of the same size.
    - The last part contains the remaining array items.


Tested with `pytest (3.2.2)`.

## Setup

Ensure `python (3.6.2)` is installed:

```bash
python --version
```

If `python (3.6.2)` is not installed, install it using, for example, [pyenv](https://github.com/pyenv/pyenv).

Ensure `pipenv` is installed:

```bash
pipenv --version
```

If `pipenv` is not installed, see installation instructions at [https://pipenv.org/](https://pipenv.org/).

Clone the repository:

```bash
git clone https://github.com/douglasdotbyers/array-helper-python.git
```

Change to the repository directory:

```bash
cd array-helper-python
```

Install required dependencies with `pipenv install`:

```bash
pipenv install
```

This will install `pytest (3.2.2)`.

## Usage

Run the tests:

```bash
pipenv run pytest test/test_array_helper.py
```

To run at the command line, with the `python` REPL:

```bash
pipenv run python
```

```python
> from app.array_helper import ArrayHelper
>
> ArrayHelper().divide([1, 2, 3, 4, 5], 3)
[[1, 2], [3, 4], [5]]
> ArrayHelper().divide([1, 2, 3, 4, 5], 4)
[[1], [2], [3], [4, 5]]
> ArrayHelper().divide([1, 2, 3, 4, 5], 5)
[[1], [2], [3], [4], [5]]
```
