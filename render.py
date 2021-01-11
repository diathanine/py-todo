
def render(address_book, target_length, elipsis_string, indent_strings, prefix, suffix):
    target_length = target_length - len(prefix) - len(suffix)
    for key in address_book:
        indent_level = (len(key) - 1)/2
        line = address_book[key].text
        line = indent(line, indent_level, indent_strings)
        line = truncate(line, target_length, elipsis_string)
        line = prefix + line + suffix
    return(string)

def truncate(line, target_length, elipsis_string):
    if len(line)>target_length:
        line = line[0:(target_length - len(elipsis_string) +1)]
        line = line + elipsis_string
    return(line)

def wrap(line, target_length):

def indent(line, indent_level, indent_strings):
    if indent_level:
        indent_string = indent_strings[0] + 5*indent_strings[1] + indent_strings[2]
    else:
        indent_string = ''
    line = indent_string + line
    return(line)
