from typing import Dict


class uFaker:
    def __init__(self):
        self._caches: Dict[str, set] = {}
