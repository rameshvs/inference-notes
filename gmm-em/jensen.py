from __future__ import division

import template
import sys
import numpy as np
import matplotlib.pyplot as plt

L = 2
def get_y_of(xval, x, y):
    """
    Given corresponding ordered arrays x and y, returns the y-value closest to
    the given x-value
    """
    return y[np.argmin((x - xval)**2)]

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: %s <range/width> <minimum>")
    # Illustrates Jensen's inequality with a 'triangular' distribution starting
    # at x_min and with width x_range
    x_range = float(sys.argv[1])
    x_min = float(sys.argv[2])

    # generate range of x, and normalized p_X(x)
    # note that the var x goes from 0 to range, but we add x_min everywhere
    # for convenience
    x = np.arange(0, x_range, .01)
    px = x * (x < (x_range/2)) + (x_range - x) * (x >= (x_range/2))
    px = px / np.max(px) / (x_range/2)

    # plot p_X(x)

    f = plt.figure(dpi=150,figsize=(2.0,1.6))
    plt.axis([0,5,0,1.6])
    plt.plot(x + x_min, px, color=template.red, linewidth=L)

    plt.xlabel('$x$')
    plt.ylabel('$z = \log x')

    plt.tight_layout()
    plt.savefig('px_only.pdf')

    # plot the curve y = log(x) for x > 1
    xlog = np.arange(1, 8, .01)
    ylog = np.log(xlog)

    plt.plot(xlog, ylog, 'k-', linewidth=L)

    # show where each x point maps to on z = log(x) using several values
    y = np.log(x + x_min)
    values = x_min + np.linspace(0, x_range, 5)

    for Ex in values:
        ylog_value = get_y_of(Ex,xlog,ylog)
        plt.plot((Ex, Ex), (get_y_of(Ex, x+x_min,px), ylog_value), 'k--')
        plt.plot((get_y_of(ylog_value, y, px), Ex), (ylog_value, ylog_value), 'k--')

    plt.tight_layout()
    plt.savefig('px_log.pdf')

    plt.plot(px, y, color=template.blue, linewidth=L)
    plt.tight_layout()
    plt.savefig('px_py_full.pdf')
