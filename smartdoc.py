import re

top = '<!DOCTYPE html>\n<html>\n  <head>\n    <meta charset="utf-8">\n  </head>\n  <body>\n   <pre>\n\n<p ' \
      'style="font-size: 40px;" >\n\n '

bot = '</p>\n     </pre>\n  </body>\n</html>\n'

with open("code.py", "r") as f:
    code_data = f.read()
    strings = [m.group() for m in re.finditer('{see \w*}', code_data)]

with open("srs.txt", "r") as f:
    srs_data = f.read()
    strings2 = [m.group() for m in re.finditer('\[id\s?=\s?r\w*\]', srs_data)]
with open("code.html", "w") as f:
    code2_data2 = code_data

    for string, string2 in zip(strings, strings2):
        string_to_replace = ('<a href = "srs.html#{}" id="{}">{}</a>'.format(string2, string, string))
        code2_data2 = code2_data2.replace(string, string_to_replace)

    f.write(top + code2_data2 + bot)

with open("srs.html", "w") as f:
    srs2_data2 = srs_data

    for string, string2 in zip(strings, strings2):
        string_to_replace = ('<a href = "code.html#{}" id="{}">{}</a>'.format(string, string2, string2))
        srs2_data2 = srs2_data2.replace(string2, string_to_replace)

    f.write(top + srs2_data2 + bot)
