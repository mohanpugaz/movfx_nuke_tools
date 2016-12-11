import smtplib

fromAdrs = "mohanpugaz@gamil.com"
toAdrs   = "mohanpugaz@gmail.com"
username = "mohanpugaz"
password = "kisses4uumma"
msg      = "Render Completed"
subject  = "render completed"

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromAdrs,toAdrs,subject,msg)
server.quit
