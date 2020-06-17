import os

from pymc3 import  *

import numpy as np
import matplotlib.pyplot as plt
import matplotlib


def regression_plot():

    size = 200
    true_intercept = 1
    true_slope = 2

    x = np.linspace(0, 1, size)

    # y = a + b*x
    true_regression_line = true_intercept + true_slope * x

    # add noise
    y = true_regression_line + np.random.normal(scale=.5, size=size)

    data = dict(x=x, y=y)

    fig = plt.figure(figsize=(7, 7))

    ax = fig.add_subplot(111, xlabel='x', ylabel='y', title='Generated data and underlying model')
    ax.plot(x, y, 'x', label='sampled data')
    ax.plot(x, true_regression_line, label='true regression line', lw=2.)

    plt.legend(loc=0)

    plot_dir = os.environ['PLOT_DIR']
    png = os.path.join(plot_dir, 'pymc3.1.png')

    plt.savefig(png)
    print(f'Wrote: {png}')


if __name__ == '__main__':

    regression_plot()
