import template
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# Duplicate code left in for clarity
def plot_gmm(x, means, stds, xlabel, filename):

    plt.figure(figsize=(3, 2))
    assert len(means) == len(stds) == 2, "Only 2-component supported"
    combined = np.zeros_like(x)
    for (mean, std, color) in zip(means, stds, (template.blue, template.red)):
        y = stats.norm.pdf(x, mean, std)
        plt.plot(x, y, color, linestyle='--')
        combined += y

    combined /= len(means)
    plt.plot(x, combined, 'k')
    plt.xlabel(xlabel)
    # make x-axis nice
    ax = plt.axis()
    (ymin, ymax) = (ax[2], ax[3])
    xrange = x[-1] - x[0]
    pad = xrange * .01
    plt.axis((x[0] - pad, x[-1] + pad, ymin, ymax))

    plt.tight_layout()
    plt.savefig(filename)

def books():
    plt.figure(figsize=(3, 2))

    prices = np.arange(3, 27, .01)

    paperback = stats.norm.pdf(prices, 10, 1.5)
    hardback = stats.norm.pdf(prices, 17, 2)

    plt.plot(prices, hardback, color=template.blue, linestyle='--')
    plt.plot(prices, paperback, color=template.red, linestyle='--')

    combined = 0.5 * (hardback + paperback)
    plt.plot(prices, combined, 'k')

    plt.xlabel('Price (dollars)')
    plt.tight_layout()

    plt.savefig('gmm-books.pdf')

def heights():
    plt.figure(figsize=(3, 2))

    # in inches
    heights = np.arange(54, 80, .1)

    male = stats.norm.pdf(heights, 69.5, 2.5)
    female = stats.norm.pdf(heights, 64.5, 2.5)

    plt.plot(heights, male, color=template.blue, linestyle='--')
    plt.plot(heights, female, color=template.red, linestyle='--')

    combined = 0.5 * (male + female)

    plt.plot(heights, combined, 'k')

    plt.xlabel('Height (inches)')

    plt.tight_layout()
    plt.savefig('gmm-heights.pdf')

if __name__ == '__main__':
    # Books
    plot_gmm(np.arange(3, 27, .01), (10, 17), (1.5, 2), 'Price (dollars)', 'gmm-books.pdf')
    # Heights
    plot_gmm(np.arange(54, 80, .1), (64.5, 69.5), (2.5, 2.5), 'Height (inches)', 'gmm-heights.pdf')
