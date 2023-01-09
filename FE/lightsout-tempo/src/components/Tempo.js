
import { useState } from 'react';
import LineChart from "./LineChart";

function Tempo({ chartData }) {

    const [LapData, setUserData] = useState({
        labels: chartData.map((data) => data.LapNumber),
        datasets: [
            {
                label: 'Driver',
                data: chartData.map((data) => data.LapTime),
                borderColor: "black",
                borderWidth: 2,
            },
        ],
    });
    return <LineChart chartData={LapData} />
}

export default Tempo