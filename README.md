# Array Helper

An array helper, in Python, which provides a method to divide an array into n parts.


 - Where the size of the array _can_ be divided equally by n:
    - All n parts are of the same size.


 - Where the size of the array _cannot_ be divided equally by n:
    - The first n-1 parts are of the same size, as large as possible.
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

If `pipenv` is not installed, see installation instructions at [https://docs.pipenv.org/](https://docs.pipenv.org/).

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

Then:

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

## Notes

`ArrayHelper` is intended to be readable through use of sensible class / method / variable names, and documentation is provided via unit tests, but some further explanation of `ArrayHelper`'s private methods is given below:


```python
def __get_part_size(self, array_length, parts):
```

`__get_part_size` initially calculates the part size as the number of whole times `parts` fits into `array_length`, then increments it by one if the remainder can be distributed evenly among the first n-1 parts of the result.


```python
def __get_divisions(self, array, parts, part_size):
```

`__get_divisions` returns a result of length `parts`, with the first n-1 parts containing exactly `part_size` items, and the last part containing at most `part_size` items.


```python
def __get_remainder(self, array, parts, part_size):
```

`__get_remainder` returns the remaining array items, if any exist, which are then added to the last part of the result in the `divide` method.

### Assumptions

 - It has been assumed that where the size of the array cannot be divided equally by n, the first n-1 parts of the result must be as large as possible, whilst remaining equal in size – e.g., dividing `[1, 2, 3, 4, 5]` into 3 parts will yield `[[1, 2], [3, 4], [5]]`, and not `[[1], [2], [3, 4, 5]]`.

 - It has been assumed that where the size of the array cannot be divided equally by n, the last part of the result must contain at least one item – e.g., dividing `[1, 2, 3, 4, 5, 6]` into 4 parts will yield `[[1], [2], [3], [4, 5, 6]]`, and not `[[1, 2], [3, 4], [5, 6], []]`.

 - It has been assumed that the result should always contain n parts, even when starting with an empty array – e.g., dividing `[]` into 3 parts will yield `[[], [], []]`.
