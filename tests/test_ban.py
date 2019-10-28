import pytest

from ufaker import uFaker


@pytest.mark.parametrize("banned", [True, False])
def test_boolean(banned):
    ufake = uFaker()

    result = ufake.boolean(ban=[banned])

    assert result is not banned
    assert ufake._caches["boolean"] == {banned, not banned}
