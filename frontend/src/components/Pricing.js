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
            <div className="mt-5">
                <h1 className="mb-3">Pricing</h1>
                <div className="m-3">
                   <h3><ReactMarkdown source={text} /></h3> 
                </div>   
            </div>
            
        )
    }
}
export default Pricing;