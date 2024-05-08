from __future__ import annotations

from dataclasses import dataclass

import matplotlib.pyplot as plt
import numpy as np


@dataclass
class Parabola:
    """
    Class used to generate parabolas of the type y = a*x**2 + b*x + c.

    :param a: parameter a of the formula
    :param b: parameter b of the formula
    :param c: parameter c of the formula
    :param x: array of the x variable.
    """

    a: float = 1
    b: float = 1
    c: float = 1
    x: tuple = (1,1,2)

    def __post_init__(self):
        """
        Initizalize the y in the post init to avoid user setting it.
        """
        self.y = None
        self._compute_y()

    def _compute_y(self):
        """
        Private function to compute the y.
        :return: None.
        """
        self.y = self.a * self.x**2 + self.b * self.x + self.c

    def plot_y(self, fig=None, ax=None) -> (plt.figure, plt.axis):
        """
        Plot function for the parabola. It can take the arguments of figure and axis to plot in an exisiting figure.
        Otherwise, they will be generated and returned.

        :param fig:
        :param ax:
        :return: None.
        """
        if (fig and ax) is None:
            fig, ax = plt.subplots()

        ax.plot(self.x, self.y)
        return fig, ax
