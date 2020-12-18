def epend_line(line, prefix, suffix):
    return(prefix+line+suffix)

def truncate_line(line, length, end_chars):
    return(line[:length] + end_chars)

#this is pseudo code
def render(list, location, settings):
    render_target=click.open_file(location)
    render_data=list
    for line in render_data:
        line= epend_line(line, setting[prefix], settings[suffix])
        line= truncate_line(line, settings[length], settings[end_chars])
    render_data="".join(render_data)
    render_target.write(render_data)
