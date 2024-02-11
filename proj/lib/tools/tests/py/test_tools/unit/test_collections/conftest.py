import pytest
from qfi.tools.collections import frozendict


@pytest.fixture
def fzdict():
    return frozendict({"x": 1, "y": 2})


@pytest.fixture
def nested_fzdict():
    return frozendict(
        {"x": [1, 2, 3], "y": {"a": 2, "b": frozendict({"z": [4, 5, 6]})}}
    )
