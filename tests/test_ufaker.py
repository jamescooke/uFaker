from ufaker import uFaker


def test_init():
    result = uFaker()

    assert result._caches == {}
