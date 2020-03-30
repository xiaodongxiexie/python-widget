from datetime import datetime, date

def _escape(value):
    """
    Escape a single value of a URL string or a query parameter. If it is a list
    or tuple, turn it into a comma-separated string first.
    """

    # make sequences into comma-separated stings
    if isinstance(value, (list, tuple)):
        value = ",".join(value)

    # dates and datetimes into isoformat
    elif isinstance(value, (date, datetime)):
        value = value.isoformat()

    # make bools into true/false strings
    elif isinstance(value, bool):
        value = str(value).lower()

    # don't decode bytestrings
    elif isinstance(value, bytes):
        return value

    # encode strings to utf-8
    if isinstance(value, str):
        return value.encode("utf-8")

    return str(value)
