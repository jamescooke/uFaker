from ufaker import uFaker


def test_ban():
    ufake = uFaker()
    ufake.seed(4321)

    result = ufake.pyint(max_value=6)

    assert result == 2


def test_bad_additive():
    ufake = uFaker()
    ufake.seed(4321)
    ufake.pyint(max_value=6)

    result = ufake.pyint(max_value=6, ban=[3, 4, 5])

    assert result == 0
