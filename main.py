import matplotlib.pyplot as plt
import numpy as np

from utils.math_utils import exponentiate


def main() -> None:
    x = np.linspace(0, 10, 10)
    y = exponentiate(2, x)
    plt.plot(x, y, "ro")
    plt.savefig("plot.png")


if __name__ == "__main__":
    main()
