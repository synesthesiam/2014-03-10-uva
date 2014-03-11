from glob import glob
from my_module import get_letter_counts, plot_letter_counts

def task_counts():
    # Files to process
    dict_files = ["dictionaries/small-dictionary.txt",
                  "dictionaries/big-dictionary.txt"]
    # Files to create
    count_files = ["counts/small-counts.txt",
                   "counts/big-counts.txt"]

    def do_counts():
        # Dictionary file -> count file
        for dict_file, count_file in zip(dict_files, count_files):
            # Extract counts from dictionary
            counts = get_letter_counts(dict_file)
            # Write to count file (overwrite if it exists)
            with open(count_file, "w") as out:
                for letter, count in counts.iteritems():
                    print >>out, letter, count

    return {
        "file_dep" : dict_files,
        "targets" : count_files,
        "actions": [do_counts]
    }


def task_plots():
    # Files to process
    count_files = ["counts/small-counts.txt",
                   "counts/big-counts.txt"]
    # Files to create
    plot_files = ["plots/small-counts.png",
                  "plots/big-counts.png"]

    def do_plots():
        # Dictionary file -> count plot
        for count_file, plot_file in zip(count_files, plot_files):
            title = "Letter Counts for {0}".format(count_file)
            ax = plot_letter_counts(count_file, title)
            # Write to plot file (overwrite if exists)
            ax.figure.savefig(plot_file)

    return {
        "file_dep" : count_files,
        "targets" : plot_files,
        "actions": [do_plots]
    }
