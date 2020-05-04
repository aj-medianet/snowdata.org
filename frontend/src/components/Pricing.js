import React, { Component } from 'react'
import ReactMarkdown from 'react-markdown';
import source from '../docs/pricing.md';

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

        return (
            <div className="m-5">
                <h1 className="m-5">Pricing</h1>
                <div>
                   <h3><ReactMarkdown source={text} /></h3> 
                </div>   
            </div>
            
        )
    }
}
export default Pricing;