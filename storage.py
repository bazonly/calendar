from typing import List
import uuid
import model

class StorageException(Exception):
    pass


class LocalStorage:
    def __init__(self):
        self._id = None
        self._storage = {}

    def generate_id(self, prefix):
        return f'{prefix}_{uuid.uuid4()}'

    def create(self, event: model.Event) -> str:
        self._id = self.generate_id(prefix='e')
        event.id = self._id
        self._storage[event.id] = event
        return event.id

    def list(self) -> List[model.Event]:
        return list(self._storage.values())

    def read(self, _id: str) -> model.Event:
        if _id not in self._storage:
            raise StorageException(f"{_id} not found in storage")
        return self._storage[_id]

    def update(self, _id: str, event: model.Event):
        if _id not in self._storage:
            raise StorageException(f"{_id} not found in storage")
        event.id = _id
        self._storage[event.id] = event

    def delete(self, _id: str):
        if _id not in self._storage:
            raise StorageException(f"{_id} not found in storage")
        del self._storage[_id]


