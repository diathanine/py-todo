def render(address_book, settings_dict):
    #settings dict has: target_length, elipsis_string, indent_strings, prefix, suffix
    target_length = int(settings_dict['line width']) - len(settings_dict['prefix']) - len(settings_dict['suffix'])
    string=''
    line_limit = int(settings_dict['line count'])
    count=1
    for key in address_book:
        indent_level = (len(key) - 1)/2
        line = address_book[key].text
        line = indent(line, indent_level, settings_dict["indent"])
        line = truncate(line, target_length, settings_dict["elipsis"])
        line = settings_dict['prefix'] + line + settings_dict['suffix']
        string = string + '\n' + line
        if count == line_limit:
            break
        else:
            count +=1
    return(string)

def truncate(line, target_length, elipsis_string):
    if len(line)>target_length:
        line = line[0:(target_length - len(elipsis_string) +1)]
        line = line + elipsis_string
    return(line)

def wrap(line, target_length):
    return(line)

def indent(line, indent_level, indent_strings):
    indent_strings = indent_strings.split(',')
    if indent_level:
        indent_string = indent_strings[0] + int(indent_level)*indent_strings[1] + indent_strings[2]
    else:
        indent_string = ''
    line = indent_string + line
    return(line)
