import React, { Component } from 'react';
//import '../App.css';

// displays website main page
const getAllData = (event) => {
  event.preventDefault()
  fetch('https://api.snowdata.org/get-all-data/tmpkey')
  //fetch('http://localhost:7082/get-all-data')
  .then((response) => {
    return response.json()
  }).then((data) => {
    console.log(data)  
  })
}

class MainContent extends Component {
  constructor() {
    super()
    this.state = {
    }
  }
  render() {
    return (
      
      <h1>Snowdata.org Main Page</h1>
      
    )
  }
}
export default MainContent