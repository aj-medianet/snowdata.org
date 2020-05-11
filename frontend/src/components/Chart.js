import React, { Component } from 'react';
//import BarChart wrapper comp
import BarChart from './BarChart';
import Container from 'react-bootstrap/Container';

class Chart extends Component {
  render() {
    return (
      <Container>
         <BarChart />
      </Container>
     
    );
  }
}
export default Chart