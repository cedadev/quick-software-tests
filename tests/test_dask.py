
import dask.array as da

def main():
    x = da.arange(6)
    assert x.sum().compute() == 15
    print('ran dask test')

if __name__ == '__main__':
    main()

