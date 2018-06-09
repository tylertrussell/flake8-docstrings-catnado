# flake8-docstrings-catnado

A fork of `flake8-docstrings` that respects the `exclude_from_doctest` option.
This allows you to enforce Flake8 rules globally but exclude your tests from
doctests.

Simply install this extension:

```bash
pip install flake8-docstrings-catnado
```

and run flake8.

Report any issues on the GitHub issue tracker.

# Changelog

### Version 0.0.1dev0

* Forked from [`flake8-docstrings`](https://gitlab.com/pycqa/flake8-docstrings)
* Added support for `--ignore_decorators` and `--exclude_from_doctest`
* Switched to 2 spaces per tab because I like chaos (and 2-space tabs)
