from typing import Dict

from faker import Faker

from .exceptions import GeneratorExhausted


class uFaker:
    def __init__(self):
        self._caches: Dict[str, set] = {}
        self.faker = Faker()

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
