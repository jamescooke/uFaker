import pytest

from ufaker import uFaker
from ufaker.exceptions import GeneratorExhausted


def test_init():
    result = uFaker()

    assert result._caches == {}


def test_boolean():
    ufake = uFaker()

    result = ufake.boolean()

    assert result in (True, False)


def test_boolean_full():
    """
    Two calls to boolean provides one of each
    """
    ufake = uFaker()
    # TODO Make seed do pass through
    ufake.faker.seed(4321)  # Gives True, True

    result = [ufake.boolean(), ufake.boolean()]

    assert sorted(result) == [False, True]


def test_boolean_exhausted():
    """
    boolean() generator can create no more unique instances
    """
    ufake = uFaker()
    ufake.boolean()
    ufake.boolean()

    with pytest.raises(GeneratorExhausted):
        ufake.boolean()
