from faker import Faker


def test():
    fake = Faker()
    fake.seed(4321)

    result = [fake.pyint(max_value=5) for _ in range(10)]

    assert result == [2, 0, 3, 0, 1, 5, 2, 0, 5, 0]
