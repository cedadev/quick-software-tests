
from _pt_common import _run, _setup, _fpath, _check_output

def test_ncdump():
    cmd = 'ncdump -h {}'.format(_fpath('A1B_north_america.nc'))
    _check_output(cmd, 'Data from Met Office Unified Model 6.05')

