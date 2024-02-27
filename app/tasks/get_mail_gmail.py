from RPA.Email.ImapSmtp import ImapSmtp
from settings import Settings
from email.message import Message
from datetime import datetime
import eel
import json
from pathlib import Path

settings = Settings()


@eel.expose
def get_mail_gmail(gmail_account: str, gmail_password: str, keyword: str,
             output_dir=None, get_attachments=True,
             from_date=None, to_date=None, select_folder="INBOX"):
    mail = ImapSmtp(smtp_server="smtp.gmail.com", smtp_port=587)

    mail.authorize(account=gmail_account, password=gmail_password)

    mail.select_folder(select_folder)

    _criterion = "gmail:" + keyword

    if from_date is not None:
        _criterion = _criterion + " after:" + from_date

    if to_date is not None:
        _criterion = _criterion + " before:" + to_date

    list_mail = mail.list_messages(
        criterion=_criterion, readonly=False
    )

    if output_dir is None:
        output_dir = Path.cwd() / "output" / "gmail"
    else:
        output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    for _mail in list_mail:
        mail_message: Message = _mail["Message"]
        body = mail.get_decoded_email_body(mail_message)
        time_string = _mail["Date"]
        time_string = time_string[:-12]  # Loại bỏ phần vùng thời gian cuối cùng
        send_date = datetime.strptime(time_string, "%a, %d %b %Y %H:%M:%S")
        date_folder = output_dir / send_date.strftime('%m-%d-%Y')
        date_folder.mkdir(parents=True, exist_ok=True)
        message_folder = date_folder / _mail["From"]
        message_folder.mkdir(parents=True, exist_ok=True)

        with open(message_folder.absolute().as_posix() + '/' + "body.txt", "w", encoding="utf-8") as text_file:
            text_file.write(body[0].strip())

        if body[1] and get_attachments:
            attachment = mail.save_attachment(
                target_folder=message_folder.absolute().as_posix(),
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
