import React from 'react';
import 'bootstrap/dist/js/bootstrap.bundle';

// site navigation bar
const Navigation = () => {
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
                            <li className="nav-item dropdown">
                                <a className="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button"
                                    data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                    Ski Area
                                </a>
                                <div className="dropdown-menu" aria-labelledby="navbarDropdown">
                                    {/*<a className="dropdown-item" href="/allareas">All Areas</a>*/}
                                    <a className="dropdown-item" href="/skiareas/Snowbird">Snowbird</a>
                                    <a className="dropdown-item" href="/skiareas/Bridger Bowl">Bridger Bowl</a>
                                    <a className="dropdown-item" href="/skiareas/Mt Baker">Mt Baker</a>
                                    <a className="dropdown-item" href="/skiareas/Mt Bachelor">Mt Bachelor</a>
                                </div>
                            </li>

                            <li className="nav-item dropdown">
                                <a className="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button"
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

export default Navigation;