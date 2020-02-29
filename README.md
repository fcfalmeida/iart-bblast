# Bubble Blast Solver

Solver for Bubble Blast game using search algorithms. First project of the IART course unit of MIEIC-FEUP.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Python 3
* virtualenv

```
Give examples
```

### Installing

Since the project is setup to work as a package, it is recommended to user virtualenv.

On the root folder of the project, start by creating a virtual environment by running 

```
virtualenv venv
```

And then activate it using

```
source venv/bin/activate
```

Install dependencies by running

```
pip3 install -r requirements/dev.txt
```

If you want to deactivate the virtual environment, you can do so by running

```
deactivate
```

## Running the tests

This project uses `pytest` to run unit tests. After making sure you've installed all dev dependencies, simply run

```
pytest
```
