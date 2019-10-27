from ufaker import uFaker


def test():
    """
    uFaker passes through calls to seed() to its wrapped faker instance.
    Seeding with 4321 gives True, True, True, True for boolean.
    """
    ufake = uFaker()

    result = ufake.seed(4321)

    assert result is None
    assert [ufake.pyint(max_value=10) for _ in range(5)] == [4, 0, 6, 1, 2]
