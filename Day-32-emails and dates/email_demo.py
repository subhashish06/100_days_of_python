from smtplib import SMTP

with SMTP("smtp.gmail.com") as mail:
    mail.starttls()
    mail.login(user="subhashish.py@gmail.com", password="Python@123")
    mail.sendmail(
                from_addr="subhashish.py@gmail.com",
                to_addrs="subhashish06@gmail.com",
                msg="Subject:New Message\n\nHello Subhashish, you got your first automated email from yourself!")

