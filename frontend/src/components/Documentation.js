import React, { Component } from 'react'
import ReactMarkdown from 'react-markdown';
import source from '../docs/documentation.md';

// displays website documentation info
class Documentation extends Component {
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
                <h1 className="mb-3">API Documentation</h1>
                <br></br>
                <div className="text-left m-3">
                    <ReactMarkdown source={text} />
                </div>   
            </div>
            
        )
    }
}

export default Documentation;