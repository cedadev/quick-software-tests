
from _pt_common import _run, _setup, _fpath, _check_output

def test_cdo_infov():
    cmd = 'cdo infov {}'.format(_fpath('A1B_north_america.nc'))
    _check_output(cmd, 'Processed 435120 values from 1 variable over 240 timesteps')


