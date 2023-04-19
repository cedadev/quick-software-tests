import os
import pytest

def test_import_iris():
    import iris
    assert (iris.__version__.count(".") == 2)

def test_import_netCDF4():
    import netCDF4
    assert (netCDF4.__version__.count(".") == 2)

@pytest.mark.skip
def test_import_netcdftime():
    import netcdftime
    assert (netcdftime.__version__.count(".") == 2)

def test_import_matplotlib():
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.plot(range(5))

    plotfile = '/tmp/test.png'
    plt.savefig(plotfile)
    assert(os.path.isfile(plotfile))
