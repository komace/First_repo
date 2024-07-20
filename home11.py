def format_string(string, length):
    cur_length = len(string)
    if cur_length >= length:
        return string
    spaces = (length - len(string))//2
    format_string2 = " " * spaces + string
    return format_string2
