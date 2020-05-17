import React from 'react';
import Dropdown from 'react-bootstrap/Dropdown';

export default function ChartSelect({chartSelected}) {
    return (
        <Dropdown>
            <Dropdown.Toggle variant="primary" id="dropdown-basic">
                Select View
            </Dropdown.Toggle>
            <Dropdown.Menu>
                <Dropdown.Item onSelect={() => chartSelected("ytd")}>YTD</Dropdown.Item>
                <Dropdown.Item onSelect={() => chartSelected("depth")}>Snow Depth</Dropdown.Item>
            </Dropdown.Menu>
        </Dropdown>
    );
}