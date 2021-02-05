# sending an email using gmail in Python

# practice Work

import smtplib
server = smtplib.SMTP_SSL('smtp.gmail.com',465)
server.login(username,password)
server.sendmail(FROM_EMAIL_ADDRESS,TO_EMAIL_ADDRESS,MESSAGE)
