import React, { Component } from 'react';
import ReactMarkdown from 'react-markdown';
import source from '../docs/quickstart.md';

// displays website quickstart guide
class QuickStart extends Component {
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
                <h1 className="m-5">QuickStart</h1>
                <div className="text-left">
                    <ReactMarkdown source={text} />
                </div>   
            </div>
            
        )
    }
}

export default QuickStart