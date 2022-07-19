# Snake Dict

## Keep your dictionary keys PEP 8 compliant

### Quick Example

```py
from snakedict import convert

my_dict = {
    "helloWorld": "test",
    "thisIsCamelCase": "hello",
    "this_is_snake_case": "world",
}

my_dict = convert(a)
print(my_dict["hello_world"])  # test
```

### Installation

#### Linux/macOS

```
python3 -m pip install -U pointers.py
```

#### Windows

```
py -3 -m pip install -U pointers.py
```

### Usage

There are 2 main functions, `convert` and `auto`.

`convert` does what was shown above, it takes in a dictionary and converts keys that are in camelCase to snake_case:

```py
from snakedict import convert

my_dict = {
    "something": "test",
    (1, 2, 3): "hello"  # you can use any key you want, snakedict won't touch it unless its in camelcase
}

print(convert(my_dict))  # no camelcase found, nothing happens
```

On the other hand, `auto` is a decorator that converts the response to snake case:

```py
from snakedict import auto

@auto()
def fetch_something():
    return {  # lets pretend this is a call to some api
        "accountName": "someone1234",
        "joinDate": "7/19/22",
    }

print(fetch_something()["account_name"])

```

`auto` has a parameter called `execute_maybe` that won't call `convert` if the response wasn't a `dict`:

If you want an error to be raised if the function returns `None`, set it to `False`:

```py
@auto(execute_maybe = False)
def fetch_something():
    return None

fetch_something()  # TypeError!
```
