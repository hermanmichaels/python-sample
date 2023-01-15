import numpy as np
import numpy.typing as npt
import pytest

from utils.math_utils import exponentiate


@pytest.mark.parametrize(
    "base, exponent, expected",
    [
        (2, np.zeros(3), np.ones(3)),
        (2, np.linspace(1, 4, 4), np.asarray([1, 4, 8, 16])),
    ],
)
def test_sum(base: int, exponent: npt.NDArray, expected: npt.NDArray) -> None:
    assert np.allclose(exponentiate(base, exponent), expected)
