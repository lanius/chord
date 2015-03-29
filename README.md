Chord
=====

Captures current status of keyboard.


Prerequisite
------------

- [pyHook](https://pypi.python.org/pypi/pyHook/)
- [pywin32](https://pypi.python.org/pypi/pywin32/)

And supports Python 2.7.


Install
-------

```
pip install git+https://github.com/lanius/chord.git
```


Usage
-----

```python
import time

import chord


def main():
    with chord.capture() as pressed_keys:
        while 'Escape' not in pressed_keys:
            print pressed_keys  # ['S', 'P', 'A', 'M'] for example
            time.sleep(1)


if __name__ == '__main__':
    main()
```
