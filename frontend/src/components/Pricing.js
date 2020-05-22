import React, { Component } from 'react'
import ReactMarkdown from 'react-markdown';
import source from '../docs/pricing.md';
import '../App.css'

// displays website pricing info
class Pricing extends Component {
    state = {
        text : null,
    }

    componentDidMount() {
        fetch(source)
            .then(res => res.text())
            .then(text => this.setState((state) => ({ ...state, text })))
            .catch((err) => console.error(err));
    }

    render() {
        const { text } = this.state;

        return(
            <div className="mt-5">
                <h1 className="mb-3">Pricing</h1>
                <br></br>
                <h3><ReactMarkdown source={text} /></h3>
                {/*
                <div className="rowP">
                    <div className="columnP">
                        <div className="card">
                            <h1>Tier 1</h1>
                            <p className="textP">This is a description of the specifics of this pricing tier.</p>
                            <div className="price-bullets">
                                <li>API Calls per Day</li>
                                <li>Other Limitation</li>
                                <li>Price</li>
                            </div>
                            <br></br>
                            <button className="btn btn-primary btn-lg">Select</button>
                        </div>
                    </div>
                    <div className="columnP">
                        <div className="card">
                            <h1>Tier 2</h1>
                            <p className="textP">This is a description of the specifics of this pricing tier.</p>
                            <div className="price-bullets">
                                <li>API Calls per Day</li>
                                <li>Other Limitation</li>
                                <li>Price</li>
                            </div>
                            <br></br>
                            <button className="btn btn-primary btn-lg">Select</button>
                        </div>
                    </div>
                    <div className="columnP">
                        <div className="card">
                            <h1>Tier 3</h1>
                            <p className="textP">This is a description of the specifics of this pricing tier.</p>
                            <div className="price-bullets">
                                <li>API Calls per Day</li>
                                <li>Other Limitation</li>
                                <li>Price</li>
                            </div>
                            <br></br>
                            <button className="btn btn-primary btn-lg">Select</button>
                        </div>
                    </div>
                </div>
                */}
            </div>

        )




    }
}
export default Pricing;