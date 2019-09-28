uFaker
======

Generate fake data using Faker, but prevent duplicate data being generated.
This is helpful when used with factories where unique data is required for a
particular attribute like ``'username'``.

Getting started
---------------

Install with ``pip``::

    $ pip install uFaker

Import and create a unique data generator::

    >>> from ufaker import uFaker
    >>> ufake = uFaker()

Generate data by calling generator methods as with Faker::

    >>> fake.pybool()
    True

Each call to a method will generate data different to previous calls::

    >>> fake.pybool()
    False

When a method can no longer generate unique data, it raises an exception::

    >>> fake.pybool()
    Traceback (most recent call last):
    ...
    GeneratorExhaustedError: pybool has run out of unique values. Tried: [True, False]
