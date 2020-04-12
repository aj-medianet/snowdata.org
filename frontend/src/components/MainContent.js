import React, { Component } from 'react'
import '../App.css';

class MainContent extends Component {
    constructor() {
      super()
      this.state = {
  
      }
    }
  
    getTest = (event) => {
      event.preventDefault()
      fetch("http://localhost:7082")
      .then((response) => {
        return response.json()
      })
      .then((data) => {
        console.log(data)
      })
    }
  
    getAllData = (event) => {
      event.preventDefault()
      fetch('http://localhost:7082/get-all-data')
      .then((response) => {
        return response.json()
      }).then((data) => {
        console.log(data)
      })
    }
  
    getSkiAreaData = (event) => {
      event.preventDefault()
      const data = { skiareaname : "Snowbird" }
      //console.log(data)
      //console.log(JSON.stringify(data))
      fetch('http://localhost:7082/get-ski-area', {
        method: 'POST',
        headers: {'Content-Type': 'application/json',},
        body: JSON.stringify(data),
      }).then((response) => {
        return response.json()
      }).then((data) => {
        console.log('Success:', data);
      })
      .catch((error) => {
        console.error('Error:', error);
      });
    }
  
    render() {
      return (
        <div className="container-fluid p-5">
          <div className="row">
            <div className="col text-center">
              <h1>API Test</h1>
              <button className="btn btn-primary mt-3 mr-2" onClick={this.getTest}>GET Request Test</button>
              <button className="btn btn-primary mt-3 ml-2 mr-2" onClick={this.getAllData}>Get All Data</button>
              <button className="btn btn-primary mt-3 ml-2" onClick={this.getSkiAreaData}>Get Snowbird Data</button>
            </div>
          </div>
        </div>
      )
    }
  }


export default MainContent