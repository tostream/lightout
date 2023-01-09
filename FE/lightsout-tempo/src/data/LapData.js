import { useState } from "react";

function LapData({ UserData }) {
    const [LapData, setUserData] = useState({
        labels: UserData.map((data) => data.LapNumber),
        datasets: [
            {
                label: 'Driver',
                data: UserData.map((data) => data.LapTime),
                backgroundColor: [
                    "rgba(75,192,192,1)",
                    "#ecf0f1",
                    "#50AF95",
                    "#f3ba2f",
                    "#2a71d0",
                ],
                borderColor: "black",
                borderWidth: 2,
            },
        ],
    });
}


export default LapData