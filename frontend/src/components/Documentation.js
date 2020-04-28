import React, { Component } from 'react'
import ReactMarkdown from 'react-markdown';
import source from '../docs/documentation.md';


class Documentation extends Component {
    state = {
        doc : null,
    }

    componentDidMount() {
        fetch(source)
            .then(res => res.text())
            .then(doc => this.setState((state) => ({ ...state, doc })))
            .catch((err) => console.error(err));
    }

    render() {
        const { doc } = this.state;

        return (
            <div className="m-5">
                <h1 className="m-5">API Documentation</h1>
                <div className="text-left">
                    <ReactMarkdown source={doc} />
                </div>   
            </div>
            
        )
    }
}

export default Documentation;