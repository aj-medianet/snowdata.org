import React, { Component } from 'react';
import D3Chart from './D3Chart';

export default class BarChart extends Component {
        //instantiate D3Chart comp
        componentDidMount() {
            this.setState({
                chart: new D3Chart(this.refs.chart, this.props.data)
            })
        }
        
        shouldComponentUpdate() {
            return false
        }

        componentWillReceiveProps(nextProps) {
            
        }

        render () {
            return <div ref="chart"></div>
        }
 }
