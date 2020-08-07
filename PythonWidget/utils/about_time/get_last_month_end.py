def get_last_month_end(date):
    """
    :param date: 格式 20200101
    """
    from datetime import date as _date

    date = str(date)
    year, month, day = date[:4], date[4:6], "01"
    target_next_day = _date(*map(int, [year, month, day])) - timedelta(days=1)
    return int(target_next_day.strftime("%Y%m%d"))

