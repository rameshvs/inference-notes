import matplotlib
matplotlib.use('pdf')

matplotlib.rc('figure', dpi=150, figsize=(2,2))

TICK_FONT_SIZE = 9
matplotlib.rc('xtick',labelsize=TICK_FONT_SIZE)
matplotlib.rc('ytick',labelsize=TICK_FONT_SIZE)

matplotlib.rc('font', **{'family':'serif', 'serif':['Computer Modern Roman']})
matplotlib.rcParams.update({'text.usetex':True})

# matplotlib.rc('figure', dpi=150, figsize=(2,2))
#
# TICK_FONT_SIZE = 5
#
# LEGEND_FONT_SIZE = TICK_FONT_SIZE
# LABEL_FONT_SIZE = TICK_FONT_SIZE + 1.5
# TITLE_FONT_SIZE = LABEL_FONT_SIZE + 1.5
#
# matplotlib.rc('xtick',labelsize=TICK_FONT_SIZE)
# matplotlib.rc('ytick',labelsize=TICK_FONT_SIZE)
# matplotlib.rc('axes', labelsize=LABEL_FONT_SIZE, titlesize=TITLE_FONT_SIZE)
# matplotlib.rc('legend', fontsize=LEGEND_FONT_SIZE)
# matplotlib.rc('font', **{'family':'serif', 'serif':['Computer Modern Roman']})
# matplotlib.rcParams.update({'text.usetex':True})
#
def dim(color, factor):
    """
    Dims a color (in #rrggbb hex form) by the factor given (float from 0-1):
    e.g., dim('#886644', 0.5) returns '#443322'
    """
    r = color[1:3]
    g = color[3:5]
    b = color[5:7]
    out = '#'
    for c in (r,g,b):
        out += '%x' % int(int(c, 16) * factor)
    return out

blue = '#4a99d8'
darkblue = dim(blue, 0.75)

green =  '#65cb67'
darkgreen = dim(green, 0.75)

red =  '#d9684f'
darkred = dim(red, 0.75)

yellow =  '#ffa44a'
darkyellow = dim(yellow, 0.75)

matplotlib.rc('axes', color_cycle=[blue, green, red, yellow])

def scatter(x, y, **kwargs):
    import matplotlib.pyplot as plt
    if 'c' not in kwargs:
        kwargs['c'] = blue
    if 'alpha' not in kwargs:
        kwargs['alpha'] = 0.95
    plt.scatter(x, y, edgecolors='none', **kwargs)

def equalize_axes():
    import matplotlib.pyplot as plt
    ax = plt.axis()
    mini = min(ax[0],ax[2])
    maxi = max(ax[1],ax[3])
    bounds = [mini, maxi, mini, maxi]
    plt.axis(bounds)
    return bounds

def change_xlimits(axis, xmin, xmax):
    ax = axis.axis()
    axis.axis([xmin, xmax, ax[2], ax[3]])

def change_ylimits(axis, ymin, ymax):
    ax = axis.axis()
    axis.axis([ax[0], ax[1], ymin, ymax])
def x_axis_only(axis):
    """ Removes the axis lines on the top and right/left sides """
    for (location, spine) in axis.spines.items():
        if location in ['right', 'top', 'left']:
            spine.set_color('none') # don't draw it
    axis.xaxis.set_ticks_position('bottom')
    #axis.yaxis.set_ticks_position('left')

def legend_reordered(ax, permutation_of_sorted_labels, **kwargs):
    def reorder(lst):
        return [lst[i] for i in permutation_of_sorted_labels]
    (handles, labels) = ax.get_legend_handles_labels()
    ax.legend(reorder(handles), reorder(labels), **kwargs)

def xy_axes_only(axis):
    limit_axes(axis, ['right', 'top'], 'bottom', 'left')

def _xy_axes_only(axis):
    """ Removes the axis lines on the top and right sides """
    for (location, spine) in axis.spines.items():
        if location in ['right', 'top']:
            spine.set_color('none') # don't draw it
    axis.xaxis.set_ticks_position('bottom')
    axis.yaxis.set_ticks_position('left')

def limit_axes(axis, locations_to_remove, xtick_location='none', ytick_location='none'):
    """
    Removes the axis lines at the specified locations, and puts the x/y ticks
    at the specified locations.
    locations_to_remove: a list or other iterable with a subset of:
                         ['top', 'bottom', 'left', 'right']

    xtick_location: one of 'top', 'bottom', 'left', 'right', 'none'
    """
    for (location, spine) in axis.spines.items():
        if location in locations_to_remove:
            spine.set_color('none') # don't draw it

    axis.xaxis.set_ticks_position(xlabel_location)
    axis.yaxis.set_ticks_position(ylabel_location)
