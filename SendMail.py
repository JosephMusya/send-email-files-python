import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

sender_address = ''
password = ''
receiver_address = ''

def SendMail(name,ImgFileName):
    img_data = open(ImgFileName, 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = 'SECURITY CAMERA'
    msg['From'] = sender_address
    msg['To'] = receiver_address

    text = MIMEText(name)
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
    msg.attach(image)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(sender_address, password)
    s.sendmail(sender_address, receiver_address, msg.as_string())
    s.quit()
    print("Sent :)")
if __name__ == "__main__":
    SendMail()