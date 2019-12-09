import smtplib as smt
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email = "xxx@gmail.com"
pas = "xx"

# Using att as an exmaple here. This works with other carriers as well.
send_to = "xx@txt.att.net"

# Using gmail for this example. For another email service, the port number will be different.
smtp_client = "smtp.gmail.com"
port_number = 465

# This will start our email server
server = smt.SMTP_SSL(smtp_client, port_number)
server.login(email, pas)
print("login successful")

# Attaching message
message = MIMEMultipart()
message["Subject"] = "You can insert anything"
body = "You can insert message here"
message.attach(MIMEText(body, "plain"))
sms = message.as_string()

server.sendmail(email, send_to, sms)
print("message sent")
server.quit()
