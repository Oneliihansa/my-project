import smtplib

my_email = "mihantilakaratne@gmail.com"
password = "..."

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user = my_email, password = password)
    connection.sendmail(
        from_addr = my_email,
        to_addrs = "mitilk2002@gmail.com",
        msg = "Subject:Test1\n\nThis is the body of my email")
