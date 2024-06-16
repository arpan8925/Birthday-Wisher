import smtplib

email = "sbxp1966@gmail.com"
password = "nefavshikuecxvbg"
Message = input("Write your Message: ")

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(
        from_addr=email,
        to_addrs="arpansathi2003@gmail.com",
        msg=f"Subject:Test Main\n\n{Message}"
    )