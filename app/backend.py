from RPA.Email.ImapSmtp import ImapSmtp
from settings import Settings
from email.message import Message
from datetime import datetime, timedelta
import eel
# from send_message_kafka import send_message
import json

settings = Settings()


@eel.expose
def get_mail():
    gmail_account = settings.gmail_account
    gmail_password = settings.gmail_password

    mail = ImapSmtp(smtp_server="smtp.gmail.com", smtp_port=587)

    mail.authorize(account=gmail_account, password=gmail_password)

    mail.select_folder("INBOX")
    yesterday = datetime.now() - timedelta(days=1)

    time_str = yesterday.strftime("%d/%m/%Y")
    list_mail = mail.list_messages(
        criterion=settings.gmail_criterion + " after:" + time_str, readonly=False
    )

    for _mail in list_mail:
        mail_message: Message = _mail["Message"]
        body = mail.get_decoded_email_body(mail_message)
        if body[1]:
            attachment = mail.save_attachment(
                target_folder="attachments",
                message=mail_message,
                overwrite=False,
            )
        else:
            attachment = None

        message = json.dumps(
            {
                "uid": _mail["uid"],
                "from": _mail["From"],
                "body": body[0],
                "attachment": attachment,
            }
        )

        print(message)
