import smtplib

class NotificationManager:
    """
    Handles sending email notifications for flight deals.
    Uses SMTP (Gmail) to send emails.
    """
    
    def __init__(self, email : str, password : str):
        self.email = email
        self.password = password

    def send_mail(self, email_list : list, subject : str, body : str):
        """
        Sends flight deal email to all emails in the email list.
        """
        
        with smtplib.SMTP("smtp.gmail.com") as server:
            server.starttls()
            server.login(self.email, self.password)

            message = f"Subject: {subject}\n\n{body}"
            
            for to_addr in email_list:
                server.sendmail(from_addr = self.email, to_addrs = to_addr, msg = message)
            