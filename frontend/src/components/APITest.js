import React, { Component } from 'react';
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'

const URL = 'https://api.snowdata.org/'
//const URL = 'http://localhost:7082/'

// displays website API test
class APITest extends Component {
  constructor(props) {
    super(props)
    this.state = {
      returnData: "",
      username: "",
      email: "",
      password: "",
      passwordError: false,
      errMessage: "",
      apiKey: "",
    }
  }

  //check that the password length and has special chacters etc
  checkPassword = () => {
    if (this.state.password.length < 10) {
      this.setState({ passwordError: true })
      return false
    }
    this.setState({ passwordError: false })
    return true
  }

  createUser = (event) => {
    event.preventDefault()
    if (!this.checkPassword()) {
      return
    }

    const data = {
      username: this.state.username,
      email: this.state.email,
      password: this.state.password
    }

    fetch(URL + 'create-user', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', },
      body: JSON.stringify(data),
    }).then((response) => {
      return response.json()
    }).then((data) => {
      if (data === "Invalid Username") {
        this.setState({ errMessage: data})
      } else {
        this.setState({ apiKey: data }); this.setState({ errMessage: ""}) 
      }
    }).catch((err) => {
      this.setState({ errMessage: err })
      return
    })

  }

  changeHandler = (event) => {
    let key = event.target.name
    let val = event.target.value
    this.setState({ [key]: val })
  }

  resetAPICount = (event) => {
    event.preventDefault()
    fetch(URL)
      .then((response) => {
        return response.json()
      })
      .then((data) => {
        console.log(data)
        this.setState({ returnData: "count reset" })
      });
  }

  getAllData = (event) => {
    event.preventDefault()
    fetch(URL + 'get-all-data/tmpkey')
      .then((response) => {
        return response.json()
      }).then((data) => {
        console.log(data)
        this.setState({ returnData: data })
      })
  }

  getSkiAreaData = (event) => {
    event.preventDefault()
    const data = {
      skiareaname: "Snowbird",
      api_key: "tmpkey"
    }
    fetch(URL + 'get-ski-area', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', },
      body: JSON.stringify(data),
    }).then((response) => {
      return response.json()
    }).then((data) => {
      console.log(data)
      this.setState({ returnData: data })
    })
      .catch((error) => {
        console.error('Error:', error);
      });
  }



  render() {
    return (
      <div className="container-fluid p-5" >
        <div className="row">
          <div className="col text-center">
            <h1>API Test</h1>
            <button className="btn btn-primary mt-3 mr-2" onClick={this.resetAPICount}>Reset API Key Count</button>
            <button className="btn btn-primary mt-3 ml-2 mr-2" onClick={this.getAllData}>Get All Data</button>
            <button className="btn btn-primary mt-3 ml-2" onClick={this.getSkiAreaData}>Get Snowbird Data</button>

            <p className="text-left m-5">{this.state.returnData ? JSON.stringify(this.state.returnData, null, 1) : ""}</p>


          </div>
        </div>

        <div className="row">
          <div className="col text-left">
            <p className="text-danger">{this.state.passwordError ? 'Password must be at least 10 characters' : ''}</p>
            <p className="text-danger">{this.state.errMessage ? this.state.errMessage : ''}</p>
            <p className="text-success">{this.state.apiKey ? 'Success! API Key: '+ this.state.apiKey : ""}</p>

            <h2>Create Account</h2>
            <Form onSubmit={this.createUser}>
              <Form.Group controlId="formBasicUsername">
                <Form.Label>Username</Form.Label>
                <Form.Control onChange={this.changeHandler} type="text" name="username" placeholder="Enter Username" />
              </Form.Group>

              <Form.Group controlId="formBasicEmail">
                <Form.Label>Email address</Form.Label>
                <Form.Control onChange={this.changeHandler} type="text" name="email" placeholder="Enter Email" />
              </Form.Group>


              <Form.Group controlId="formBasicPassword">
                <Form.Label>Password</Form.Label>
                <Form.Control onChange={this.changeHandler} type="text" name="password" placeholder="Enter Password" />
              </Form.Group>

              <Button variant="primary" type="submit">
                Submit
              </Button>
            </Form>
          </div>

        </div>

      </div>
    )
  }
}

export default APITest