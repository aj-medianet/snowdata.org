import React, { Component } from 'react';
import ReactMarkdown from 'react-markdown';
import Button from 'react-bootstrap/Button';
import source from '../docs/quickstart.md';
import source2 from '../docs/quickstart2.md';

// displays website quickstart guide
class QuickStart extends Component {
    state = {
        text : null,
        text2 : null,
    }

    componentDidMount() {
        Promise.all([
            fetch(source)
            .then(res => res.text())
            .then(text => this.setState((state) => ({ ...state, text })))
            .catch((err) => console.error(err)),

            fetch(source2)
            .then(res => res.text())
            .then(text2 => this.setState((state) => ({ ...state, text2 })))
            .catch((err) => console.error(err))

        ]);
    }

    render() {
        const { text } = this.state;
        const { text2 } = this.state;

        return (
            <div className="mt-5">
                <h1 className="mb-3">QuickStart</h1>
                <div className="text-left m-3">
                    <ReactMarkdown source={text} />
                    <Button href="/account" className="" variant="primary">Create Account</Button>
                    <br></br><br></br><br></br>
                    <ReactMarkdown source={text2} />
                    <Button href="/api-documentation" className="" variant="primary">View API Documentation</Button>
                </div>   

            </div>
            
        )
    }
}

export default QuickStart