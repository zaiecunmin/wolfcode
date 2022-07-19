import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
class email():
    def lodin(self,from_addr,password):
        server = smtplib.SMTP()
        server.connect('smtp.qq.com', 25)
        server.login(from_addr,password)
        return srever
    def send(self,server,from_addr,to_addr,text,subject,f_name,t_name):
        msg=MIMEText(text,'plain','utf-8')
        msg['From'] = Header(f_name)
        msg['To'] = Header(t_name)
        msg['Subject'] = Header(subject)
        server.sendmail(from_addr, to_addr, msg.as_string())
        server.quit()


#gyerfrxunezicehb
#收件人邮箱&title=标题&text=内容

