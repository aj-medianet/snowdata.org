import React, { Component } from 'react'

class HeaderContent extends Component {
    render() {
        return (
            <header className="">
                <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
                    <a class="navbar-brand" href="/">SnowData</a>
                    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
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
                                    <a className="dropdown-item" href="/ski-area/snowbird">Snowbird</a>
                                    <a className="dropdown-item" href="/ski-area/bridgerbowl">Bridger Bowl</a>
                                    <a className="dropdown-item" href="/ski-area/mtbaker">Mt Baker</a>
                                    <a className="dropdown-item" href="/ski-area/mtbachelor">Mt Bachelor</a>
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
}

export default HeaderContent