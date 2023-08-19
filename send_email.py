import smtplib
import ssl
def send_email(message)
    host="smpt.gmail.com"
    port=465
    
    username="fyuskas@gmail.com"
    password="mnhyetkppmpfdjpu"
    receiver="fyuskas@gmail.com"
    context=ssl.create_default_context()
    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,message)

send_email()
