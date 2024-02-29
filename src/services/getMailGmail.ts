import { eel } from "@/eel";

type getMailGmailParams = {
  gmailAccount: string;
  gmailPassword: string;
  keyword: string;
  outputDir?: string;
  getAttachment?: boolean;
  fromDate?: string;
  toDate?: string;
  mailFolder?: string;
};

export default function getMailGmail({
  gmailAccount,
  gmailPassword,
  keyword,
  outputDir,
  getAttachment = true,
  fromDate,
  toDate,
  mailFolder = "INBOX",
}: getMailGmailParams) {
  return eel.get_mail_gmail(
    gmailAccount,
    gmailPassword,
    keyword,
    outputDir,
    getAttachment,
    fromDate,
    toDate,
    mailFolder
  );
}
