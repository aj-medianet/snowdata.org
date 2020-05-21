import React, { Component } from 'react';
import { withRouter } from 'react-router-dom';
import 'bootstrap/dist/js/bootstrap.bundle';
import Select from 'react-select';


const skiAreaChoices = [
    { label: "Alpental" },
    { label: "Big Sky" },
    { label: "Bridger Bowl" },
    { label: "Jackson Hole" },
    { label: "Mt Bachelor" },
    { label: "Mt Hood" },
    { label: "49 Degrees North" },
    { label: "Snowbird" },
    { label: "Whitefish" },
];

class Navigation extends Component {

    render() {
        return (
            <header className="">
                <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
                    <a className="navbar-brand" href="/">SnowData</a>
                    <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
                        aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                        <span className="navbar-toggler-icon"></span>
                    </button>
                    <div className="collapse navbar-collapse" id="navbarSupportedContent">
                        <ul className="navbar-nav ml-auto">
                        <li>
                                <div className="" style={{ width: '250px' }}>
                                    <Select
                                        onChange={opt => window.location.href = "/skiareas/" + opt.label}
                                        placeholder={'Search Ski Areas'}
                                        menuPlacement="auto"
                                        menuPosition="fixed"
                                        options={skiAreaChoices} />
                                </div>
                            </li>
                            <li className="nav-item dropdown">
                                <a className="nav-link dropdown-toggle" href="/#" id="navbarDropdown" role="button"
                                    data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                    API
                                </a>
                                <div className="dropdown-menu" aria-labelledby="navbarDropdown">
                                    <a className="dropdown-item" href="/api-quick-start">Quick Start</a>
                                    <a className="dropdown-item" href="/api-documentation">Documentation</a>
                                    <a className="dropdown-item" href="/api-pricing">Pricing</a>
                                </div>
                            </li>
                            <li className="nav-item">
                                <a className="nav-link" href="/about">About</a>
                            </li>
                            <li className="nav-item">
                                <a className="nav-link" href="/account">Account</a>
                            </li>
                        </ul>
                    </div>
                </nav>
            </header>
        )
    }
}

export default Navigation;