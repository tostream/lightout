
import axios from 'axios';
import { useEffect, useState } from 'react';
import "./App.css";
import TempDropdown from "./components/dropdown";
import Tempo from "./components/Tempo";
import { session_data, year_data } from "./Tempdata";

function App() {
  // IF YOU SEE THIS COMMENT: I HAVE GOOD EYESIGHT

  const [gp, setGP] = useState([]);
  const [gp_value, setgp_value] = useState([]);
  const [driver_value, setdriver_value] = useState([]);
  const [driver, setDriver] = useState([]);
  const [session, setSession] = useState([]);
  const [chartData, setChartData] = useState([]);
  const [year, setYear] = useState()
  useEffect(() => {
    const url = `https://ergast.com/api/f1/${year}.json`;
    axios.get(url).then((response) => {
      setGP(response.data.MRData.RaceTable.Races);
    }).catch(err => { console.log(err) });
  }, [year]);
  useEffect(() => {
    const url = `https://ergast.com/api/f1/${year}/${gp_value}/results.json`;
    axios.get(url).then((response) => {
      setDriver(response.data.MRData.RaceTable.Races[0].Results);
    }).catch(err => { console.log(err) });
  }, [gp_value]);

  useEffect(() => {
    const url = `https://ergast.com/api/f1/${year}/${gp_value}/drivers/${driver_value}/laps.json`;
    axios.get(url).then((response) => {
      setChartData(response.data.MRData.RaceTable.Races[0].Laps);
    }).catch(err => { console.log(err) });
  }, [driver_value]);

  function setchtdata(x) {
    return x.length > 0 ? {
      labels: x.map((data) => data.number),
      datasets: [
        {
          label: 'HAM',
          data: x.map((data) => data.Timings[0].time),
          borderColor: "black",
          borderWidth: 2,
        },
      ],
    } : []
  }


  return (
    <div className="App">
      <div><h1>LightsOut Tempo</h1></div>
      <div><h1>Lap Chart</h1></div>
      <div><TempDropdown option_data={year_data} value={year}
        handleChange={(event) => {
          setYear(event.target.value);
        }}
        placeholder='Year' /></div>
      <div><TempDropdown option_data={gp !== null ? gp.map(x => {
        return ({ label: x.raceName, value: x.round });
      }) : null} placeholder='GP'
        handleChange={(event) => {
          setgp_value(event.target.value);
        }} /></div>
      <div><TempDropdown value={session} option_data={session_data} placeholder='Session'
        handleChange={(event) => {
          setSession(event.target.value);
        }} /></div>
      <div><TempDropdown option_data={driver !== null ?
        driver.map(x => {
          return ({ label: x.Driver.code, value: x.Driver.driverId });
        }) : null
      } placeholder='Drivers'
        handleChange={(event) => {
          setdriver_value(event.target.value);
        }} /></div>
      <div style={{ width: 700 }} >
        <Tempo chartData={setchtdata(chartData)} />
      </div>
      <div  >
      </div>
    </div>
  );
}

export default App;
