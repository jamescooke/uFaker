from typing import Dict

from faker import Faker

from .exceptions import GeneratorExhausted


class uFaker:
    def __init__(self):
        self._caches: Dict[str, set] = {}
        self.faker = Faker()

    def _add_ban(self, gen_name: str, items: list) -> set:
        """
        For provided generator, add the items provided to the banned set. If
        the banned set has not been instantiated, then create it.

        Args:
            gen_name: Name of faker provider method.
            items: An iterable of items to be added to the ban list.

        Returns:
            Banned set after new items have been added.

        Raises:
            TypeError: When a non-iterable is passed for `items`.
                TODO: improve the API of this to give help on the error.
        """
        new_items = set(items)

        try:
            self._caches[gen_name] = self._caches[gen_name].union(new_items)
        except KeyError:
            self._caches[gen_name] = new_items

        return self._caches[gen_name]

    def seed(self, *args, **kwargs):
        return self.faker.seed(*args, **kwargs)

    def boolean(self, *args, **kwargs):
        gen_name = "boolean"
        self._add_ban(gen_name, kwargs.get("ban", set()))
        attempts = 0
        while True:
            value = self.faker.boolean()
            used = value in self._caches[gen_name]
            if not used:
                self._caches[gen_name].add(value)
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
