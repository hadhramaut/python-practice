#! python3
# data_matcher.py - Finds phone numbers and email addresses on the clipboard.

import re
import pyperclip

s = pyperclip.paste()

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)


emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4})      # dot-something
    )''', re.VERBOSE)

reg_ph = phoneRegex.findall(s)
reg_m = emailRegex.findall(s)
lst = []

for phone_number in reg_ph:
    x = '-'.join([phone_number[1], phone_number[3], phone_number[5]])
    if phone_number[8] != '':
        x += phone_number[8]
    lst.append(x)
for email in reg_m:
    lst.append(email[0])

if len(lst) > 0:
    pyperclip.copy('\n'.join(lst))
    print("Data successfully copied!")
    print('\n'.join(lst))
else:
    print("No data extracted!")
