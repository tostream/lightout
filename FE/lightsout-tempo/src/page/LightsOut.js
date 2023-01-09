
import TempDropdown from "../components/dropdown";
import Tempo from "../components/Tempo";

function LightsOut({ year_data, gp_data, session_data, gp_data, UserData }) {
    return (
        <div className="LightsOut">
            <div><TempDropdown option_data={year_data} placeholder='Year' /></div >
            <div><TempDropdown option_data={gp_data} placeholder='GP' /></div>
            <div><TempDropdown option_data={session_data} placeholder='Session' /></div>
            <div><TempDropdown option_data={gp_data} placeholder='Drivers' /></div>
            <div style={{ width: 700 }} >
                <Tempo chartData={UserData} />
            </div>
        </div>
    )
}

export default LightsOut
