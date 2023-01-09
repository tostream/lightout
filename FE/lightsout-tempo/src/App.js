
import axios from 'axios';
import { useEffect, useState } from 'react';
import "./App.css";
import TempDropdown from "./components/dropdown";
import Tempo from "./components/Tempo";
import ergast from './data/ergast';
import { gp_data, session_data, UserData, year_data } from "./Tempdata";

function App() {
  // IF YOU SEE THIS COMMENT: I HAVE GOOD EYESIGHT

  const [gp, setGP] = useState(ergast);

  const [year, setYear] = useState('2021')
  console.log(year);
  useEffect(() => {
    const url =
      `https://ergast.com/api/f1/${year}.json`;
    console.log(url);
    axios.get(url).then((response) => {
      setGP(response.data.MRData.RaceTable.Races);
    });
  }, []);

  return (
    <div className="App">
      <div><h1>LightsOut Tempo</h1></div>
      <div><h1>Lap Chart</h1></div>
      <div><TempDropdown option_data={year_data} value={year}
        handleChange={(event) => {
          setYear(event.target.value);
        }}
        placeholder='Year' /></div>
      <div><TempDropdown option_data={gp ? gp.map(x => {
        return ({ label: x.raceName, value: x.round });
      }) : null} placeholder='GP'
        handleChange={(event) => {
          setGP(event.target.value);
        }} /></div>
      <div><TempDropdown option_data={session_data} placeholder='Session'
        handleChange={(event) => {
          setYear(event.target.value);
        }} /></div>
      <div><TempDropdown option_data={gp_data} placeholder='Drivers'
        handleChange={(event) => {
          setYear(event.target.value);
        }} /></div>
      <div style={{ width: 700 }} >
        <Tempo chartData={UserData} />
      </div>
      <div  >
      </div>
    </div>
  );
}

export default App;