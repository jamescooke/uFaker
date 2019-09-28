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

    >>> ufake.boolean()
    True

Each call to a method will generate data different to previous calls. For the
second call to ``boolean()``, uFaker guarantees that a new unique value will be
generated so we know this will be ``False``::

    >>> ufake.boolean()
    False

When a method can no longer generate unique data, it raises an exception::

    >>> ufake.boolean()
    Traceback (most recent call last):
    ...
    GeneratorExhaustedError: boolean has run out of unique values. Tried: [True, False]

Ban lists
---------

When you want to prevent data from being generated, you can pass a ban list to
a generator method. No values in the ban list will be returned by the generator
for this or subsequent calls::

    >>> from ufaker import uFaker

    >>> ufake = uFaker()

    >>> ufake.boolean(ban=[True])
    False

    >>> ufake.boolean()
    Traceback (most recent call last):
    ...
    GeneratorExhaustedError: boolean has run out of unique values. Tried: [True, False]

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

The ban list is additive, so calling a generator method multiple times with
additional values adds them to the ban list.

Say we had a ``dice()`` generator method that generates dice rolls from 1 to 6
inclusive::

    >>> from ufaker import uFaker

    >>> ufake = uFaker()

    >>> ufake.dice(ban=[1])
    6

So at this stage both 1 and 6 are banned. Now we call it again adding bans for
2, 3 and 4. The only unique value that can be found is 5 which is returned::

    >>> ufake.dice(ban=[2, 3, 4])
    5

Calling ``dice()`` once more raises an exception because there are no more
unique values available::

    >>> ufake.dice()
    Traceback (most recent call last):
    ...
    GeneratorExhaustedError: dice has run out of unique values. Tried: [1, 6, 2, 3, 4, 5]
