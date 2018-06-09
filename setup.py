from setuptools import setup


def get_version(fname='flake8_docstrings.py'):
  with open(fname) as f:
    for line in f:
      if line.startswith('__version__'):
        return eval(line.split('=')[-1])


def get_long_description():
  descr = []
  for fname in ('README.md'):
    with open(fname) as f:
      descr.append(f.read())
  return '\n\n'.join(descr)


setup(
  name='flake8-docstrings-catnado',
  version=get_version(),
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
