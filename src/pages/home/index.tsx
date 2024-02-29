import { useState, useEffect } from "react";
import getMailOutlook from "@/services/getMailOutlook.ts";
import getMailGmail from "@/services/getMailGmail.ts";

function HomePage() {
  const [msg, setMsg] = useState("Loading...");

  useEffect(() => {
    getMailGmail({
      gmailAccount: "quachbaoquan123@gmail.com",
      gmailPassword: "aordkzcmxzcydlwd",
      keyword: "RPAFujinet",
    })((res: string) => setMsg(res));

    getMailOutlook({ keyword: "test_rpa" })((res: string) => setMsg(res));
  }, []);

  return (
    <div className="mt-1">
      <h1 className="text-purple-700">{msg}</h1>
    </div>
  );
}

export default HomePage;
