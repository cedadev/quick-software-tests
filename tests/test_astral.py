import pytz
import astral

from datetime import date

def main():

    v = astral.__version__
    d = date(2009,4,22)
    if v.startswith('1.'):
        a = astral.Astral()
        location = a['London']
        print(location)
        s = location.sun(date=d)
        
    elif v.startswith('2.'):
        from astral.sun import sun
        city = astral.LocationInfo("London")
        print(city)
        s = sun(city.observer, date=d)
    
    else:
        raise Exception('unsupported astral version')

    dawn = s['dawn'].astimezone(pytz.utc)

    print(dawn)
    
    assert dawn.hour == 4
    assert 12 <= dawn.minute <= 13  # astral versions differ in location of 'London'
    print('ran astral test')


if __name__ == '__main__':
    main()
