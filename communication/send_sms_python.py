import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email = "xxx@gmail.com"
pas = "xx"

# Using att as an exmaple here. This works with other carriers as well.
send_to = "xx@txt.att.net"

# The server we use to send emails in our case it will be gmail but every email provider has a different smtp # and port is also provided by the email provider.
smtp = "smtp.gmail.com"
port = 465

# This will start our email server
server = smtplib.SMTP_SSL(smtp, port)
server.login(email, pas)
print("login successful")

# Attaching message
msg = MIMEMultipart()
msg["Subject"] = "You can insert anything"
body = "You can insert message here"
msg.attach(MIMEText(body, "plain"))
sms = msg.as_string()

server.sendmail(email, send_to, sms)
print("message sent")
server.quit()

