

def time_delta_specifier(time: str):
    """
    Function which accepts time delta specifier as a string argument and returns time interval in seconds as an integer.
    Supported time units:
        s – seconds,
        m – minute,
        h – hour,
        d – day,
    with seconds being default unit and 1 being default value
    Examples:
        time_delta_specifier("30")  ->	30
        time_delta_specifier("30s") ->	30

    :param time: string with format digit value and time unit. Ex "20d"
    :return: integer: time interval in seconds
    """
    if time == '':
        raise ValueError("Empty time value")

    if time == 's':
        return 1

    if time.isdigit():
        return int(time)

    check = [unit in time for unit in ["d", "h", "m", "s"]]
    if check.count(True) > 1:
        raise ValueError("Incorrect time value")
    elif check.count(True) == 1:
        return {
            "s": int(float(time[:-1])),
            "m": int(float(time[:-1]) * 60),
            "h": int(float(time[:-1]) * 360),
            "d": int(float(time[:-1]) * 360 * 12)
        }[time[-1]]
    raise ValueError("Incorrect time value")
