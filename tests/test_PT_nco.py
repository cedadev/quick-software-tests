from _pt_common import _run, _setup, _fpath, _check_output


def test_nco_ncks_help():
    cmd = 'ncks --help'
    _check_output(cmd, 'cheatsheet')

    
#@pytest.mark.xfail
def test_nco_ncks_subset(tmpdir):
    fin = _fpath('A1B_north_america.nc')
    fout = tmpdir.mkdir("test-outputs").join('fout.nc')
    _run('ncks -d latitude,,,20 -d longitude,,,20 -d time,,,6 {} {}'.format(
                   fin, fout))

    # Check ncdump output
    resp = _run('ncdump -h {}'.format(fout)) 
    assert('latitude = 2 ;' in resp)
    assert('longitude = 3 ;' in resp)

