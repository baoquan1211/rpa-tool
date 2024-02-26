from pathlib import Path
import datetime
import eel

import win32com.client

# Create output folder
output_dir = Path.cwd() / "Output"
output_dir.mkdir(parents=True, exist_ok=True)

# Connect to outlook
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")


@eel.expose
def get_mail_outlook(num_of_mail=5):
    # Connect to folder
    # inbox = outlook.Folders("youremail@provider.com").Folders("Inbox")
    inbox = outlook.GetDefaultFolder(6)
    # https://docs.microsoft.com/en-us/office/vba/api/outlook.oldefaultfolders
    # DeletedItems=3, Outbox=4, SentMail=5, Inbox=6, Drafts=16, FolderJunk=23

    # Get messages
    messages = inbox.Items
    messages.Sort("[ReceivedTime]", True)

    # Filter messages
    # today = datetime.date.today()
    # yesterday = today - datetime.timedelta(days=1)
    # messages = messages.Restrict("[ReceivedTime] >= '" + yesterday.strftime('%m/%d/%Y %H:%M:%S') + "'")

    # Filter by keyword in subject
    # messages = messages.Restrict("[Subject] = 'Test'")

    print(messages)

    i = 0
    for message in messages:
        subject = message.Subject
        body = message.body
        attachments = message.Attachments

        if i > 5:
            break
        else:
            i += 1

        return f"Subject: {subject}"

        # return (f"Body: {body}")
