import React, { Component } from 'react';

const getTest = (event) => {
    event.preventDefault()
    fetch('https://api.snowdata.org')
    //fetch("http://localhost:7082")
    .then((response) => {
      return response.json()
    })
    .then((data) => {
      console.log(data)
    })
}

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

const getSkiAreaData = (event) => {
    event.preventDefault()
    const data = { 
      skiareaname : "Snowbird",
      api_key : "tmpkey"
    }
    //console.log(data)
    //console.log(JSON.stringify(data))
    fetch('https://api.snowdata.org/get-ski-area', {
      method: 'POST',
      headers: {'Content-Type': 'application/json',},
      body: JSON.stringify(data),
    }).then((response) => {
      return response.json()
    }).then((data) => {
      console.log(data)
    })
    .catch((error) => {
      console.error('Error:', error);
    });
  }

class APITest extends Component {
  constructor() {
    super()
    this.state = {
      
    }
  }
  render() {
    return (
      <div className="container-fluid p-5">
        <div className="row">
          <div className="col text-center">
            <h1>API Test</h1>
            <button className="btn btn-primary mt-3 mr-2" onClick={getTest}>GET Request Test</button>
            <button className="btn btn-primary mt-3 ml-2 mr-2" onClick={getAllData}>Get All Data</button>
            <button className="btn btn-primary mt-3 ml-2" onClick={getSkiAreaData}>Get Snowbird Data</button>
          </div>
        </div>
        <div className="APIResults">
          <p>
            API Call Results
          </p>
        </div>
      </div>
    )
  }
}

class ResultList extends Component {
  render() {
    return (
      <div className="APIResult"></div>
    )
  }
}

export default APITest