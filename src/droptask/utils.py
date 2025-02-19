from datetime import datetime

from src.droptask.exceptions import InvalidDatetimeFormat


def parse_str_to_dt(str_time: str) -> datetime:
    try:
        if ":" not in str_time:
            return datetime.strptime(str_time, "%d-%m-%Y")
        else:
            return datetime.strptime(str_time, "%d-%m-%Y %H:%M:%S")
    except ValueError:
        raise InvalidDatetimeFormat(str_time)


def parse_dt_to_str(dt: datetime) -> str:
    return dt.strftime("%d-%m-%Y %H:%M:%S")


def is_dt_past(dt: datetime) -> bool:
    now = datetime.now()
    td = dt - now
    if td.days < 0 or td.seconds < 0:
        return True
    return False



