"use strict";

import FetchData from "../services/FetchData";
import Debounce from "../services/Debounce";

const Fetch = () => {
    console.log("dadsdsas");
    const data = Debounce(FetchData("dog"));
    console.log("Data", data);
    return <div></div>;
};

const container = document.getElementById("search-form");
const root = ReactDOM.createRoot(container);
root.render(<Fetch />);
