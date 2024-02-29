import React from "react";

const HomePage = React.lazy(() => import("./pages/home"));

function App() {
  return <HomePage />;
}

export default App;
