from astral import Astral
from datetime import date

def main():
    a = Astral()
    location = a['London']
    d = date(2009,4,22)
    sun = location.sun(local=True, date=d)
    assert sun['dawn'].hour == 5
    assert sun['dawn'].minute == 13
    print('ran astral test')


if __name__ == '__main__':
    main()
