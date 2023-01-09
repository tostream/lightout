import * as React from 'react';

const TempDropdown = ({ option_data, placeholder, handleChange = null, value }) => {


    return (

        <div>

            <Dropdown
                options={option_data}
                value={value}
                onChange={handleChange}
                placeholder={placeholder}
            />

        </div>

    );

};

const Dropdown = ({ label, value, options, onChange, placeholder }) => {

    return (

        <label>

            {label}

            <select value={value} onChange={onChange}>
                <option value="" disabled selected hidden>{placeholder}</option>
                {options.map((option) => (

                    <option value={option.value}>{option.label}</option>

                ))}

            </select>

        </label>

    );

};

export default TempDropdown;