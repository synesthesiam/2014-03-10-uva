import numpy as np
from collections import Counter
from matplotlib import pyplot

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f',
           'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x'
           'y', 'z']

def get_letter_counts(dict_file):
    """Returns a Counter with letter frequencies from a dictionary file"""
    counts = Counter()
    for word in open(dict_file, "r"):
        word = word.strip()  # Remove '\n'
        for letter in word:
            if letter in LETTERS:
                counts[letter] += 1
    return counts

def plot_letter_counts(counts_file, title=None):
    """Plots a histogram of letter frequencies in a counts file"""
    counts = Counter()
    for line in open(counts_file, "r"):
        # e.g., c 100
        letter, count = line.split(" ")
        counts[letter] = count

    # Create bar plot with bar heights being letter frequencies
    fig, ax = pyplot.subplots()
    left = np.arange(len(counts)) + 0.5
    heights = [float(v) for v in counts.values()]
    ax.bar(left, heights, width=1)
    ax.grid()

    # Show labels for each letter centered horizontally on the bar.
    ax.set_xticks(left + 0.5)
    ax.set_xticklabels(counts.keys())

    # Set figure title if provided
    if title is not None:
        ax.set_title(title)

    return ax

