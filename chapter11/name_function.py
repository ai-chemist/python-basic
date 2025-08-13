def get_upper_name(first, last, middle=''):
    """Upper"""
    if middle:
        fullname = f"{first.upper()} {middle.upper()} {last.upper()}"
    else:
        fullname = f"{first.upper()} {last.upper()}"
    return fullname