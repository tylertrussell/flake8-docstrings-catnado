from setuptools import setup
from flake8_docstrings import __version__

def get_long_description():
  descr = []
  for fname in ('README.md'):
    with open(fname) as f:
      descr.append(f.read())
  return '\n\n'.join(descr)


setup(
  name='flake8-docstrings-catnado',
  version=__version__,
  description='a fork of flake8-docstrings-catnado',
  long_description=get_long_description(),
  license='MIT License',
  author='Tyler Trussell',
  author_email='tigertrussell@gmail.com',
  url='https://github.com/tylertrussell/flake8-docstrings-catnado',
  entry_points={
    'flake8.extension': [
      'D = flake8_docstrings:pep257Checker',
    ],
  },
  install_requires=['flake8', 'pydocstyle >= 2.1', 'flake8-polyfill'],
  provides=['flake8_docstrings'],
  py_modules=['flake8_docstrings'],
)
