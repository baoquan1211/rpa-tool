import {eel} from "../eel.js";

export default function getMailOutlook(outputDir = undefined, keyword = undefined, getAttachment=true,
                                       mailFolder = "Inbox", fromDate = undefined, toDate = undefined) {
    return eel.get_mail_outlook(outputDir, getAttachment, mailFolder, fromDate, toDate, keyword)
}