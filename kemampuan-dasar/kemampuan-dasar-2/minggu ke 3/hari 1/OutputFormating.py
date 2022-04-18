# import reprlib
# print(reprlib.repr(set('supercalifragilisticexpiallidocious')))
# import pprint
# t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]
# pprint.pprint(t, width=30)

# import textwrap
# doc = """The Wrap() method is just like fill() except that it returns 
# a list of string instead of one big string with newlines to separate
# the wrapped lines."""
# print(textwrap.fill(doc, width=40))

# import locale
# # locale.setlocale(locale.LC_ALL, 'English_United States.1252')
# conv = locale.localeconv()
# x = 1234567.8
# locale.format("%d", x, grouping=True)
# locale.format_string("s%.*f", (conv['currency_symbol'], conv['frac_digits'], x), grouping=True)

from string import Template
t = Template('${village}folk send $$10 to #cause.')
t.substitute(village='Nottingham', cause='the ditch fund')

