import pytest

from codec import rle as mod

CASES = [
    ('rle_encode', [[1, 1, 2, 2, 2]], [[1, 2], [2, 3]], False),
    ('rle_encode', [[]], [], False),
    ('rle_decode', [[[1, 2], [2, 3]]], [1, 1, 2, 2, 2], False),
    ('varint_encode', [300], [172, 2], False),
    ('varint_decode', [[172, 2]], [300, 2], False),
    ('varint_decode', [[5, 0]], [5, 1], False),
    ('delta_encode', [[5, 7, 10]], [5, 2, 3], False),
    ('delta_encode', [[]], [], False),
    ('rle_encode', ['aab'], [['a', 2], ['b', 1]], False),
    ('rle_decode', [[]], [], False),
    ('rle_decode', [[[5, 0]]], [], False),
    ('varint_encode', [0], [0], False),
    ('varint_encode', [127], [127], False),
    ('varint_decode', [[128]], [0, 1], False),
    ('delta_encode', [[0]], [0], False),
]


@pytest.mark.parametrize("func_name,args,expected,approx", CASES)
def test_rle_contract(func_name, args, expected, approx):
    func = getattr(mod, func_name)
    result = func(*args)
    if approx:
        assert result == pytest.approx(expected)
    else:
        assert result == expected
