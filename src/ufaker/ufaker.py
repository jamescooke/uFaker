from typing import Dict
from faker import Faker


class uFaker:
    def __init__(self):
        self._caches: Dict[str, set] = {}
        self.faker = Faker()

    def boolean(self):
        return self.faker.boolean()
