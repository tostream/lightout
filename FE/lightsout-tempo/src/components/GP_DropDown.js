import React from 'react';
import 'react-dropdown/style.css';
function GP_DropDown() {
    const options = [

        { label: 'Fruit', value: 'fruit' },

        { label: 'Vegetable', value: 'vegetable' },

        { label: 'Meat', value: 'meat' },

    ];

    const [value, setValue] = React.useState('fruit');

    const handleChange = (event) => {

        setValue(event.target.value);

    };
    return (
        <div>
            <select value={value} onChange={handleChange}>
                {options.map((option) => (
                    <option value={option.value}>{option.label}</option>
                ))}
            </select>
        </div>
    )
}

export default GP_DropDown