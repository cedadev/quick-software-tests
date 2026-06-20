from __future__ import annotations

import os

import _confirm_images as CI

import matplotlib as mpl
import geovista as gv
from geovista.pantry.data import icon_soil
import geovista.theme

fname = "test_geovista.png"

def do_plot(fname):
    # copied from
    # https://geovista.readthedocs.io/en/stable/generated/gallery/unstructured/icon.html#sphx-glr-generated-gallery-unstructured-icon-py
    # (as also are the relevant imports above)
    
    # Load the sample data.
    sample = icon_soil()

    # Create the mesh from the sample data.
    mesh = gv.Transform.from_unstructured(sample.lons, sample.lats, data=sample.data)

    # Plot the unstructured mesh.
    plotter = gv.GeoPlotter()
    sargs = {"title": f"{sample.name} / {sample.units}", "shadow": True}
    cmap = mpl.colormaps.get_cmap("Spectral").resampled(lutsize=9)
    plotter.add_mesh(mesh, cmap=cmap, scalar_bar_args=sargs)
    plotter.add_coastlines()
    plotter.add_axes()
    plotter.add_text(
        "ICON 160km Resolution Triangular Mesh (10m Coastlines)",
        position="upper_left",
        font_size=10,
        shadow=True,
    )
    plotter.view_yz()
    plotter.camera.zoom(1.3)
    plotter.show(screenshot=fname)


do_plot(fname)
os.system(f"display {fname} &")
CI.images_launched([fname])
CI.image_confirm("geovista")
