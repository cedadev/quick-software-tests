import numpy as np
import matplotlib.pyplot as plt
import geocat.viz as gv

import _confirm_images as CI


def make_plot():

    #======================================================================================
    # This example copied from
    # https://geocat-examples.readthedocs.io/en/latest/gallery/Bar/NCL_bar_14.html#sphx-glr-gallery-bar-ncl-bar-14-py
    #======================================================================================
    
    # Generate 12 numbers from 0 to 100 in a uniform distribution
    y1 = np.random.uniform(0, 100, 12)

    # Generate 12 numbers with an average of 30 and a standard deviation of 10
    y2 = np.random.normal(30, 10, 12)

    # Create an array from 1 to 12 with 12 numbers
    months = np.linspace(1, 12, 12)

    # Create figure with figure size (width, height) in inches and create axes
    fig = plt.figure(figsize=(6, 5.25))
    ax = plt.axes()

    # Plot the bar chart, line chart, and a horizontal line with varying colors and linewidths
    plt.bar(months, y1, color="yellow", edgecolor="k", linewidth=0.5)
    plt.plot(months, y2, color="b", linewidth=1)
    plt.hlines(40, 0, 13, color="b", linewidth=1)

    # Use geocat.viz.util convenience function to add titles and set their size
    gv.set_titles_and_labels(
        ax,
        maintitle="XY curve over a bar chart",
        maintitlefontsize=16,
        ylabel="mm",
        labelfontsize=14,
    )

    # Use geocat.viz.util convenience function to set axes tick values and labels
    gv.set_axes_limits_and_ticks(
        ax,
        xticks=np.linspace(0, 12, 5),
        xticklabels=np.linspace(0, 12, 5),
        xlim=(0, 13),
        yticks=np.linspace(0, 100, 6),
        ylim=(0, 100),
    )

    # Create the right axis
    axRHS = ax.twinx()

    # Set the right axis title and size while rotating it 270 degrees and adding a whitespace padding
    axRHS.set_ylabel(("\u00b0" + "C"), size=14, rotation=270, labelpad=25)

    # Use geocat.viz.util convenience function to set axes tick values and labels for the right axis
    gv.set_axes_limits_and_ticks(
        axRHS, yticks=np.linspace(0, 100, 6), yticklabels=np.linspace(0, 50, 6, dtype=int)
    )

    # Use geocat.viz.util convenience function to add major and minor tick lines
    gv.add_major_minor_ticks(ax, x_minor_per_major=3, y_minor_per_major=4)

    # Adjust tick and ticklabel sizes for each axis
    ax.tick_params(axis="x", size=12, labelsize=12)
    ax.tick_params(axis="y", size=12, labelsize=12)
    axRHS.tick_params(axis="y", size=12, labelsize=12)

    # Display plot
    plt.tight_layout()
    plt.show()


CI.images_follow(['geocat_viz.png'])
make_plot()
CI.image_confirm('geocat_viz')
