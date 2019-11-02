uFaker
======

Generate fake data using Faker, but prevent duplicate data being generated.
This is helpful when used with factories where unique data is required for a
particular attribute like ``'username'``.

Getting started
---------------

    **WARNING** Nothing below works as yet, this is just a draft of the API
    that I'm planning for this tool. Please give feedback by creating an Issue
    or adding to this discussion which includes a use-case in the context of
    username generation: https://github.com/jamescooke/factory_djoy/issues/20

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

Let's use Faker's ``pyint()`` generator to return some random single digit
integers::

    >>> from ufaker import uFaker

    >>> ufake = uFaker()

    >>> ufake.pyint(max_value=6)
    2

So at this stage 2 is banned because it's been generated. Now we call it again
adding bans for 3, 4 and 5. The only unique value that can be found is 0
which is returned:: 

    >>> ufake.pyint(max_value=6, ban=[3, 4, 5])
    0

Calling ``pyint(max_value=6)`` once more raises an exception because there are
no more unique values available::

    >>> ufake.pyint(max_value=6)
    Traceback (most recent call last):
    ...
    GeneratorExhaustedError: pyint has run out of unique values. Tried: [2, 3, 4, 5, 0]
