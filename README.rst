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

    >>> ufake.pybool()
    True

Each call to a method will generate data different to previous calls. For the
second call to ``pybool()``, uFaker guarantees that a new unique value will be
generated so we know this will be ``False``::

    >>> ufake.pybool()
    False

When a method can no longer generate unique data, it raises an exception::

    >>> ufake.pybool()
    Traceback (most recent call last):
    ...
    GeneratorExhaustedError: pybool has run out of unique values. Tried: [True, False]

Ban lists
---------

When you want to prevent data from being generated, you can pass a ban list to
a generator method. No values in the ban list will be returned by the generator
for this or subsequent calls::

    >>> from ufaker import uFaker

    >>> ufake = uFaker()

    >>> ufake.pybool(ban=[True])
    False

    >>> ufake.pybool()
    Traceback (most recent call last):
    ...
    GeneratorExhaustedError: pybool has run out of unique values. Tried: [True, False]

This can be helpful when writing tests that assert behaviour against a set of
values excluding some particular ones. For example, if you want to prove that
any ``Account`` where the username is not ``"admin"`` can be disabled, then we
can use the ``user_name()`` generator and ban the name ``"admin"``::

    def test()
        """
        Any non-admin Account can be disabled
        """
        ufake = uFaker()
        account = Account(
            username=ufake.user_name(ban=["admin"],
        )

        result = account.disable()

        assert result is True
