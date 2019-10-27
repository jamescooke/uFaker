import pytest

from ufaker import uFaker


def test_empty_passed_list():
    ufake = uFaker()

    result = ufake._add_ban("pyint", [17])

    assert result == {17}
    assert ufake._caches["pyint"] == {17}


def test_empty_passed_set():
    """
    pyint generator will never generate strings, but they can be banned all the
    same.
    """
    ufake = uFaker()

    result = ufake._add_ban("pyint", {"a", "b"})

    assert result == {"a", "b"}
    assert ufake._caches["pyint"] == {"a", "b"}


def test_initialised_passed_list():
    ufake = uFaker()
    ufake._caches["user_name"] = {"alpha", "beta"}

    result = ufake._add_ban("user_name", {"gamma", "delta"})

    assert result == {"alpha", "beta", "gamma", "delta"}
    assert ufake._caches["user_name"] == {"alpha", "beta", "gamma", "delta"}


# --- FAILURES ---


def test_empty_passed_int():
    """
    Ints and strings and bools can not be added
    """
    ufake = uFaker()

    with pytest.raises(TypeError):
        ufake._add_ban("pyint", 17)
