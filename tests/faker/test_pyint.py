from faker import Faker


def test():
    fake = Faker()
    fake.seed(4321)

    result = [fake.pyint(max_value=10) for _ in range(5)]

    assert result == [4, 0, 6, 1, 2]
