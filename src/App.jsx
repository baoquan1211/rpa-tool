import { useState, useEffect } from 'react'
import './index.css';
import getMailOutlook from "./services/getMailOutlook.js";
import getMailGmail from "./services/getMailGmail.js";

function App() {
  const [msg, setMsg] = useState("Loading...");

  useEffect(() => {
    getMailGmail("quachbaoquan123@gmail.com", "aordkzcmxzcydlwd", "RPAFujinet", "gmail")(res => setMsg(res));
    getMailOutlook("outlook", "test_rpa")(res => setMsg(res))
  }, []);

  return (
    <div className="mt-1">
      <h1 className="text-red-400">
        {msg}
      </h1>
    </div>
  )
}

export default App
