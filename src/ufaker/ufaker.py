from typing import Dict

from faker import Faker

from .exceptions import GeneratorExhausted


class uFaker:
    def __init__(self):
        self._caches: Dict[str, set] = {}
        self.faker = Faker()

    def seed(self, *args, **kwargs):
        return self.faker.seed(*args, **kwargs)

    def boolean(self):
        attempts = 0
        while True:
            value = self.faker.boolean()

            try:
                used = value in self._caches["boolean"]
            except KeyError:
                self._caches["boolean"] = {value}
                return value

            if not used:
                self._caches["boolean"].add(value)
                return value

            attempts += 1
            if attempts >= 200:
                raise GeneratorExhausted()

    def pyint(self, *args, **kwargs):
        attempts = 0
        while True:
            value = self.faker.pyint(*args, **kwargs)

            try:
                used = value in self._caches["pyint"]
            except KeyError:
                self._caches["pyint"] = {value}
                return value

            if not used:
                self._caches["pyint"].add(value)
                return value

            attempts += 1
            if attempts >= 200:
                raise GeneratorExhausted()
