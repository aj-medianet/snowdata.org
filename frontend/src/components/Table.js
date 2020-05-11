import React, { Component } from 'react';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Button from 'react-bootstrap/Button';

class Table extends Component {
    renderRows() {
        return (
            this.props.data.map(area => {
            return (
                <Row>
                    <Col xs={2}>{area.name}</Col>
                    <Col xs={1}>{area.cur_temp}</Col>
                    <Col xs={1}>{area.wind_speed}</Col>
                    <Col xs={1}>{area.wind_dir}</Col>
                    <Col xs={1}>{area.ytd}</Col>
                    <Col xs={1}>{area.cur_depth}</Col>
                    <Col xs={1}>{area.new_snow_12}</Col>
                    <Col xs={1}>{area.new_snow_24}</Col>
                    <Col xs={1}>{area.new_snow_48}</Col>
                </Row> 
                )  
            })
        )      
    }
    
    render() {
        return (
            <div>
            <Row>
            <Col xs={2}>Ski Area</Col>
            <Col xs={1}>Temperature</Col>
            <Col xs={1}>Wind Speed</Col>
            <Col xs={1}>Wind Direction</Col>
            <Col xs={1}>YTD</Col>
            <Col xs={1}>Depth</Col>
            <Col xs={1}>12H Snow</Col>
            <Col xs={1}>24H Snow</Col>
            <Col xs={1}>48H Snow</Col>
            </Row>
            {this.renderRows()}
            </div>    
        )
    }
}
export default Table