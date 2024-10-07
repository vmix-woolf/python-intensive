def my_xml(tag_name: str, content: str = '', **kwargs) -> str:
    attrs = ''.join([f' {key}="{value}"' for key, value in kwargs.items()])

    return f"<{tag_name}{attrs}>{content}</{tag_name}>"


print(my_xml('foo'))  # <foo></foo>
print(my_xml('foo', 'bar'))  # <foo>bar</foo>
print(my_xml('foo', 'bar', a=1, b=2, c=3))  # <foo "a"=1 "b"=2 "c"=3>bar</foo>
print(my_xml('foo', 'bar', a=4, b=5))