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
            <div>
                <br></br>
                <h1>Pricing</h1>
                <br></br>
                <h3><ReactMarkdown source={text} /></h3>
                <div class="row">
                    <div class="column">
                        <div class="card">
                            <h1>Tier 1</h1>
                            <p>This is a description of the specifics of this pricing tier.</p>
                            <div class="price-bullets">
                                <li>API Calls per Day</li>
                                <li>Other Limitation</li>
                                <li>Price</li>
                            </div>
                            <br></br>
                            <a href="#" class="btn btn-primary">Go</a>
                        </div>
                    </div>
                    <div class="column">
                        <div class="card">
                            <h1>Tier 2</h1>
                            <p>This is a description of the specifics of this pricing tier.</p>
                            <div class="price-bullets">
                                <li>API Calls per Day</li>
                                <li>Other Limitation</li>
                                <li>Price</li>
                            </div>
                            <br></br>
                            <a href="#" class="btn btn-primary">Go</a>
                        </div>
                    </div>
                    <div class="column">
                        <div class="card">
                            <h1>Tier 3</h1>
                            <p>This is a description of the specifics of this pricing tier.</p>
                            <div class="price-bullets">
                                <li>API Calls per Day</li>
                                <li>Other Limitation</li>
                                <li>Price</li>
                            </div>
                            <br></br>
                            <a href="#" class="btn btn-primary">Go</a>
                        </div>
                    </div>
                </div>
            </div>

        )




    }
}
export default Pricing;