import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("science.reactor85@gmail.com", "c@rrot007")
 
msg = "adrak maha chutiya hai"
server.sendmail("your email adresss", "ahmadraja32@gmail.com", msg)
server.quit()
