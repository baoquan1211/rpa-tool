from pathlib import Path
import datetime
import eel

import win32com.client

default_folder = {
    "DeletedItems": 3,
    "Outbox": 4,
    "SentMail": 5,
    "Inbox": 6,
    "Drafts": 16,
    "FolderJunk": 23
}


@eel.expose
def get_mail_outlook(output_dir: str | None = None,
                     get_attachments=True, mail_folder="Inbox", from_date=None, to_date=None,
                     keyword: str | None = None):
    # Create output folder
    if output_dir is None:
        output_dir = Path.cwd() / "output" / "gmail"
    else:
        output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Connect to outlook
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

    # Connect to folder
    try:
        folder = outlook.GetDefaultFolder(default_folder[mail_folder])  # Default is INBOX Folder
    except:
        raise Exception("Can't open folder")

    # Get messages
    messages = folder.Items
    messages.Sort("[ReceivedTime]", True)

    # Filter messages
    if from_date is not None:
        _from_date = datetime.datetime.strptime(from_date, '%d/%m/%Y')
    else:
        _from_date = datetime.datetime.now()
    messages = messages.Restrict("[ReceivedTime] >= '" + _from_date.strftime('%d/%m/%Y') + "'")

    if to_date is not None:
        _to_date = datetime.datetime.strptime(to_date, '%m/%d/%Y')
        messages = messages.Restrict("[ReceivedTime] <= '" + _to_date.strftime('%d/%m/%Y') + "'")

    # Filter by keyword in subject
    if keyword is not None:
        messages = messages.Restrict(f"@SQL=(urn:schemas:httpmail:subject LIKE '%{keyword}%')")

    try:
        for message in messages:
            send_date = message.SentOn
            sender = message.Sender.Address
            date_folder = output_dir / send_date.strftime('%m-%d-%Y')
            date_folder.mkdir(parents=True, exist_ok=True)
            message_folder = date_folder / sender
            message_folder.mkdir(parents=True, exist_ok=True)

            with open(message_folder.absolute().as_posix() + '/' + "body.txt", "w", encoding="utf-8") as text_file:
                text_file.write(message.Subject + '\n' + message.body.strip())

            if get_attachments:
                for att in message.Attachments:
                    att.SaveAsFile(message_folder.absolute().as_posix() + '\\' + att.FileName)
        return None
    except Exception as ex:
        return ex
