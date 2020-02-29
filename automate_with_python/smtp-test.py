import smtplib

smtp_obj = smtplib.SMTP_SSL('smtp.mail.ru', 465)

if smtp_obj.ehlo()[0] == 250:
    print("Successfully connected to SMTP server")
else:
    print("Connection error")
    quit()

print("Specify your e-mail for authentication:")
sender_mail = input()
print("Specify your password for authentication:")
sender_password = input()

if smtp_obj.login(sender_mail, sender_password)[0] == 235:
    print('Authentication is successful')
else:
    print('Wrong login/password!')
    quit()

print("Specify receiver's e-mail:")
receiver_mail = input()

if smtp_obj.sendmail(sender_mail, receiver_mail, 'Subject: \n Simple test message') == {}:
    print('Successfully sent message from {0} to {1}'.format(sender_mail, receiver_mail))
smtp_obj.quit()