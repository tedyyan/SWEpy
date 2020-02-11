# Classify imagery from MEaSUREs

import os
import matplotlib.pyplot as plt
import jenkspy
import numpy as np
from matplotlib import colors as c


def govf(array, classes):
    """
    GVF function to assist in finding optimal number of jenks classes

    Funtion to implement a Goodness of Variance Fit to minimize
    squared deviations of the class means.

    Paramters
    ---------
    array: np.array
        SWE array that you would like to classify
    """
    # get break points
    classes = jenkspy.jenks_breaks(array, classes)
    # do classificaton
    classified = np.array([classify(i, classes) for i in array])
    # max value of zones
    maxz = max(classified)
    # nested list of zone indices
    zone_indices = [
        [idx for idx, val in enumerate(classified) if zone + 1 == val]
        for zone in range(maxz)
    ]
    # sum of squared deviations from array mean
    sdam = np.sum((array - array.mean()) ** 2)
    # sorted polygon stats
    array_sort = [
        np.array([array[index] for index in zone]) for zone in zone_indices
    ]
    # sum of squared deviations of class means
    sdcm = sum(
        [
            np.sum((classified - classified.mean()) ** 2)
            for classified in array_sort
        ]
    )
    # goodness of variance fit
    gvf = (sdam - sdcm) / sdam
    return gvf


def classify(value, breaks):
    """
    Helper function for govf

    Assign pixels to classes

    Paramaters
    ----------
    value: float
        pixel value from input image
    breaks: list
        current class breaks from govf
    """
    for i in range(1, len(breaks)):
        if value < breaks[i]:
            return i
    return len(breaks) - 1


def optimal_jenk(image, threshold, gvf=0.0, nclasses=2):
    """
    Find GVF at incrementing class numbers until threshold
    GVF is reached

    Parameters
    ----------
    image: np.array
        input image from spatial slice of swe cube
    threshold: float
        cutoff value for how high to optimize gvf
    gvf: float
        initial gvf value (default = 0.0)
    nclasses: int
        how many classes to start with
    """
    while gvf < threshold:
        gvf = govf(image, nclasses)
        nclasses += 1
    return nclasses


def plot_jenks(image, gvt):
    list_colors = [
        "blue",
        "green",
        "orange",
        "magenta",
        "cyan",
        "gray",
        "red",
        "yellow",
    ]
    classes_jenk = jenkspy.jenks_breaks(
        image.ravel(), optimal_jenk(image.ravel(), gvt)
    )
    classes = np.digitize(image, classes_jenk)
    nclasses = len(classes_jenk)
    fig, ax = plt.subplots(1, 1, figsize=(14, 5))
    xlabel = str(nclasses) + " Classes, Jenks Classification"
    ax.set_title("Jenk Classification with" + str(nclasses) + " Classes")
    ax.set_xlabel(xlabel)
    bounds = range(0, nclasses + 1)
    cmap = c.ListedColormap(list_colors[0:nclasses])
    kmp = ax.imshow(
        classes,
        interpolation="nearest",
        aspect="auto",
        cmap=cmap,
        origin="lower",
    )
    plt.colorbar(kmp, cmap=cmap, ticks=bounds, ax=ax, orientation="vertical")
    plt.show()
