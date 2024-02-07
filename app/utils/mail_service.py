# import os
#
# from email.mime.text import MIMEText
# from smtplib import SMTP


class EmailSender:
    def send_email(self, message, title, to) -> None:
        # This is a dummy implementation of the email sending.
        # If you want to use real email sending, you should use the
        # commented code below and set the environment variables.

        # smtp_email = os.environ.get("SMTP_EMAIL")
        # smtp_password = os.environ.get("SMTP_PASSWORD")
        # smtp_port = int(os.environ.get("SMTP_PORT"))
        # smtp_gate = os.environ.get("SMTP_GATE")
        #
        print("Mail task")
        # message = MIMEText(message, "plain")
        # message["Subject"] = title
        # message["To"] = to
        # message["From"] = smtp_email
        # sent = False
        # try:
        #     connection = SMTP(smtp_gate, port=smtp_port)
        #     connection.command_encoding = "utf-8"
        #     connection.login(smtp_email, smtp_password)
        #     try:
        #         sent = connection.sendmail(smtp_email, to, message.as_string())
        #         sent = True
        #     except Exception as e:
        #         print(e)
        #     finally:
        #         connection.close()
        # except Exception as e:
        #     print(e)
        # return sent

        print(f"Sending email to {to} with title {title} and message {message}")


def send_email(message, title, to):
    sender = EmailSender()
    return sender.send_email(message, title, to)
