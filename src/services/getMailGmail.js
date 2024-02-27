import {eel} from "../eel.js";

export default function getMailGmail(gmailAccount, gmailPassword, keyword, outputDir, getAttachment=true, fromDate, toDate, mailFolder="INBOX") {
    return eel.get_mail_gmail(gmailAccount, gmailPassword, keyword, outputDir, getAttachment, fromDate, toDate, mailFolder)
}