#! python3

import sys
import pyperclip

def add_pass(account, password, dictionary):
    # Add new account, password and copy the password
    dictionary[account] = password
    pyperclip.copy(dictionary[account])
    print('Password for ' + account + ' is added and copied to clipboard')

PASSWORDS = {} # dictionary for passwords

# import passwords from txt into dict - not secure scheme
with open('passwords.txt') as f:
    for line in f:
        (key, val) = line.split()
        PASSWORDS[key] = val
PASSWORDS_OLD = PASSWORDS

# case of incorrect usage
if len(sys.argv) not in (2, 3):
    print('Usage:\n'
          'python pw.py [account] - copy account password for existing account\n'
          'python pw.py [new_account] [password] - add new credentials and copy password\n')
    sys.exit()

# Copy password to clipboard only
elif len(sys.argv) == 2:

    account = sys.argv[1]

    if account in PASSWORDS:
        pyperclip.copy(PASSWORDS[account])
        print('Password for ' + account + ' copied to clipboard')
    else:
        print('There is no account named ' + account)

# Add new account\password and cpoy the password
elif len(sys.argv) == 3:

    account = sys.argv[1]
    password = sys.argv[2]
    if account in PASSWORDS:
        print('Account already exists. Do you want to update the password? Y/N')
        a = input()
        if a == 'Y':
            add_pass(account, password, PASSWORDS)
        else:
            sys.exit()
    else:
        add_pass(account, password, PASSWORDS)
        
f = open('passwords.txt', 'w')
for k, v in PASSWORDS.items():
    if k not in PASSWORDS_OLD.items():
        f.write(k + ' ' + v + '\n')
