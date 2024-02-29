import { eel } from "@/eel.ts";

type getMailOutlookParams = {
  keyword: string;
  outputDir?: string;
  getAttachment?: boolean;
  mailFolder?: string;
  fromDate?: string;
  toDate?: string;
};

export default function getMailOutlook({
  outputDir,
  keyword,
  getAttachment = true,
  mailFolder = "Inbox",
  fromDate,
  toDate,
}: getMailOutlookParams) {
  return eel.get_mail_outlook(
    outputDir,
    getAttachment,
    mailFolder,
    fromDate,
    toDate,
    keyword
  );
}
