from __future__ import annotations

from typing import Optional, Mapping, Sequence, MutableMapping, MutableSequence, TypeVar

KT = TypeVar("KT")
VT = TypeVar("VT")

class frozendict(Mapping[KT, VT]):
    def __init__(
            self,
            value: Optional[Mapping[KT, VT]] = None,
            recurse: bool = True,
            frozen: bool = False,
    ) -> None:
        self.frozen = frozen
        self.recurse = recurse
        self._value = dict(value) if value else {}
        if self.recurse:
           self._recurse()

    def _recurse(self):

        def _freeze(obj):
            if isinstance(obj, Mapping):
                obj = dict(obj)
                for key, obj_i in obj.items():
                    obj[key] = _freeze(obj_i)
                obj = frozendict(obj, recurse=self.recurse, frozen=self.frozen)
            elif isinstance(obj, Sequence) and not isinstance(obj, (str, bytes)):
                obj = list(obj)
                for idx, obj_i in enumerate(obj):
                    obj[idx] = _freeze(obj_i)
                obj = tuple(obj)
            return obj

        for key, obj in self._value.items():
            if isinstance(obj, (Mapping, Sequence)):
                self._value[key] = _freeze(obj)

    def asdict(self):
        return self._value

    to_dict = asdict

    def items(self):
        return self._value.items()

    def keys(self):
        return self._value.keys()

    def values(self):
        return self._value.values()

    def update(self, other=None):
        if other is None:
            return
        if not isinstance(other, (dict, frozendict)):
            return NotImplemented
        if self.frozen:
            raise AttributeError(f"Update on a frozen frozendict")
        if isinstance(other, frozendict):
            other = other._value
        else:
            other = frozendict(other, self.recurse, self.frozen)._value
        self._value.update(other)

    def get(self, key, default=None):
        return self._value.get(key, default)

    def __iter__(self):
        return self._value.__iter__()

    def __getitem__(self, key):
        return self._value.__getitem__(key)

    def __repr__(self):
        return self._value.__repr__()

    def __str__(self):
        return self._value.__str__()

    def __hash__(self):
        return hash(tuple((k, v) for k, v in self._value.items()))

    def __eq__(self, other):
        if isinstance(other, frozendict):
            other = other._value
        return self._value == other

    def __ne__(self, other):
        return not self == other

    def __len__(self):
        return self._value.__len__()

    def __setitem__(self, key, value):
        if self.frozen:
            raise AttributeError(f"Attempting to set value on frozen frozendict.")
        self._value.__setitem__(key, value)

    def __or__(self, other):
        new = frozendict(self._value)
        new.update(other)
        return new

    def __ior__(self, other):
        self.update(other)
        return self

    def __ror__(self, other):
        return NotImplemented