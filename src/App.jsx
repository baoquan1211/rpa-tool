import { useState, useEffect } from 'react'
import { eel } from "./eel.js";
import logo from "./assets/react.svg"
import './index.css';


function App() {
  const [msg, setMsg] = useState("Loading...");

  useEffect(() => {
    // eel.get_mail("quachbaoquan123@gmail.com", "aordkzcmxzcydlwd")(res => setMsg(res));
    eel.get_mail_outlook() (res => setMsg(res))
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
