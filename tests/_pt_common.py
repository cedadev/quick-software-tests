import os
import subprocess as sp
import iris_sample_data

SAMPLE_DATA_DIR = iris_sample_data.path

def _run(cmd):
    bytes = sp.check_output(cmd, shell=True, executable='/bin/bash', stderr=sp.STDOUT)
    import pdb
    return bytes.decode('utf-8').replace('\n', '')


def _setup():
    import iris_sample_data as isd
    _sample_data_dir = os.path.join(os.path.dirname(isd.__file__), 'sample_data')
    global SAMPLE_DATA_DIR
    SAMPLE_DATA_DIR = _sample_data_dir 

def _fpath(fname):
    return os.path.join(SAMPLE_DATA_DIR, fname)

def _check_output(cmd, match):
    resp = _run(cmd)
    assert(match in resp)
