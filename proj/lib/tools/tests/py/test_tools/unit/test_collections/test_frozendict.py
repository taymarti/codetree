from qfi.tools.collections import frozendict


def test_init(fzdict):
    assert isinstance(fzdict, frozendict), ""


def test_hash(fzdict):
    _ = hash(fzdict)
    assert isinstance(_, int), ""


def test_recursive(nested_fzdict):
    v = nested_fzdict
    assert isinstance(v["x"], tuple), ""
    assert isinstance(v["y"], frozendict), ""
    assert isinstance(v["y"]["b"], frozendict), ""
    assert isinstance(v["y"]["b"]["z"], tuple), ""
    _ = hash(nested_fzdict)
    assert isinstance(_, int), ""


def test_update(nested_fzdict):
    v = nested_fzdict | {"a": [4, 4, 6]}
    assert v["a"] == (4, 4, 6), ""
