import React from 'react'

const Footer = () => {
    return (
        <footer className="footer mt-5 pt-3 pb-5 bg-secondary text-light">
            <div className="row">
                <div className="col-sm text-left m-5">
                    <h5>Site Navigation</h5>
                    <a className="text-light text-left" href="/">Home</a><br />
                    <a className="text-light text-left" href="/api-quick-start">Quick Start</a><br />
                    <a className="text-light text-left" href="/api-documentation">Documentation</a><br />
                    <a className="text-light text-left" href="/api-pricing">Pricing</a><br />
                    <a className="text-light text-left" href="/about">About</a><br />
                    <a className="text-light text-left" href="/account">Account</a><br />
                </div>
                <div className="col-sm text-left m-5">
                    <h5>Info</h5>
                    <a className="text-light text-left" href="https://github.com/aj-medianet/snowdata.org" target="_blank" rel="noopener noreferrer">GitHub</a><br />
                    <a className="text-light text-left" href="mailto:snowdataorg@gmail.com" target="_blank" rel="noopener noreferrer">snowdataorg@gmail.com</a><br />
                    <a className="text-light text-left" href="/tc">Terms & Conditions</a><br />
                </div>
                <div className="col-sm text-left m-5">
                    <h5>Social</h5>
                    <a className="text-light text-left" href="https://twitter.com/SnowData_org" target="_blank" rel="noopener noreferrer">Twitter</a><br />
                    <a className="text-light text-left" href="https://www.youtube.com/channel/UCEE0T6FcHpqePZKtu0WyTwg" target="_blank" rel="noopener noreferrer">YouTube</a><br />
                    <a className="text-light text-left" href="https://www.instagram.com/snowdataorg/" target="_blank" rel="noopener noreferrer">Instagram</a><br />
                    <a className="text-light text-left" href="https://stackoverflow.com/questions/tagged/snowdata" target="_blank" rel="noopener noreferrer">Stack Overflow</a><br />
                </div>
            </div>
            <div className="row">
                <div className="col-sm text-center">
                    &copy; SnowData.org | {new Date().getFullYear()}
                </div>
            </div>


        </footer>
    )
}

export default Footer