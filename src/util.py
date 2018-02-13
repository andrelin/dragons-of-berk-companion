from datetime import timedelta


def parse_amount(amount):
    pass


def get_timedelta(timestr):
    if 'd' in timestr:
        d, rest = timestr.split('d')
    if 'h' in timestr:
        h, rest = timestr.split('h')
    if 'm' in timestr:
        m, rest = timestr.split('m')

    if 'd' in timestr:
        d = int(d)
        if 'h' in timestr:
            h = int(h)
            if 'm' in timestr:
                delta = timedelta(days=d, hours=h, minutes=int(m))
            else:
                delta = timedelta(days=d, hours=h)
        else:
            delta = timedelta(days=d)

    elif 'h' in timestr:
        h = int(h)
        if 'm' in timestr:
            delta = timedelta(hours=h, minutes=int(m))
        else:
            delta = timedelta(hours=h)

    elif 'm' in timestr:
        delta = timedelta(minutes=int(m))

    else:
        raise ValueError('Can not parse time string: {}'.format(timestr))

    return delta
