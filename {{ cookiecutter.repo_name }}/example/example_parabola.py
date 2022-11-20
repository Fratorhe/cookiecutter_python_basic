import numpy as np
from matplotlib import pyplot as plt

from {{ cookiecutter.package_dist_name }} import Parabola

a = 1
b = 4
c = 20
x = np.linspace(-10, 10, num=50)
parabola_obj = Parabola(a, b, c, x)

parabola_obj.plot_y()

plt.show()
