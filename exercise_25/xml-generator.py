def my_xml(tag: str, value: str = '', *argv: str) -> None:
    if len(argv) != 0:
        result_line = '<' + tag
        for elem in argv:
            attr_name, attr_value = elem.split('=')
            result_line = result_line + ' ' + attr_name + '="' + attr_value + '"'
        result_line = result_line + '>' + value + '</' + tag + '>'
    else:
        result_line = '<' + tag + '>' + value + '</' + tag + '>'

    return print(result_line)


my_xml('foo')  # <foo></foo>
my_xml('foo', 'bar')  # <foo>bar</foo>
my_xml('foo', 'bar', 'a=1', 'b=2', 'c=3')  # <foo "a"=1 "b"=2 "c"=3>bar</foo>
my_xml('foo', 'bar', 'a=4', 'b=5')  # <foo "a"=4 "b"=5>bar</foo>