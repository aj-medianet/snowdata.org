import React, { Component } from 'react';
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'

class Account extends Component {
  constructor() {
    super()
    this.state = {
      returnData: "",
      username: "",
      email: "",
      password: "",
      passwordError: false,
      errMessage: "",
      successMessage: "",
      apiKey: "",
      loggedIn: false,
    }
  }

  changeHandler = (event) => {
    let key = event.target.name
    let val = event.target.value
    this.setState({ [key]: val })
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

  checkEmptyFields = () => {
    if (this.state.username === "" || this.state.email === "" || this.state.password === "") {
      this.setState({errMessage: "Please fill in all fields"})
      return false;
    }
    this.setState({errMessage: ""})
    return true;
  }

  createUser = (event) => {
    event.preventDefault()
    if (!this.checkEmptyFields()) { return; }
    if (!this.checkPassword()) { return; }

    const data = {
      username: this.state.username,
      email: this.state.email,
      password: this.state.password
    }

    fetch('https://api.snowdata.org/create-user', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', },
      body: JSON.stringify(data),
    }).then((response) => {
      return response.json()
    }).then((data) => {
      if (data === "Invalid Username") {
        this.setState({ errMessage: data })
      } else {
        this.setState({ apiKey: data }); 
        this.setState({ errMessage: "" });
      }
    }).catch((err) => {
      this.setState({ errMessage: err })
      return
    })

  }


  login = (event) => {
    event.preventDefault()
    if (!this.checkEmptyFields()) { return; }
    if (!this.checkPassword()) { return; }

    const data = {
      username: this.state.username,
      password: this.state.password
    }

    fetch('https://api.snowdata.org/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', },
      body: JSON.stringify(data),
    }).then((response) => {
      return response.json()
    }).then((data) => {
      if (data === "Failed") {
        this.setState({ errMessage: data })
        this.setState({ successMessage: "" });
      } else {
        this.setState({ errMessage: "" });
        this.setState({ successMessage: data });
        this.setState({ loggedIn: true });

      }
    }).catch((err) => {
      this.setState({ errMessage: err })
      return
    })

  }

  render() {
    return (
      <>
        <div className="container-fluid p-5" >
          <div className="row">
            <div className="col text-center">
              <h1>Account</h1>
            </div>
          </div>

          <div className="row">
            <div className="col text-left">
              <p className="text-danger">{this.state.passwordError ? 'Password must be at least 10 characters' : ''}</p>
              <p className="text-danger">{this.state.errMessage ? this.state.errMessage : ''}</p>
              <p className="text-success">{this.state.apiKey ? 'Success! API Key: ' + this.state.apiKey : ""}</p>


              {this.state.loggedIn ? 
              
              <>
              <h2>Hello {this.state.username}</h2>



              </>
              
              
              
              
              : 
            
              <>
              <h2>Create Account or Login</h2>
              <Form>
                <Form.Group controlId="formBasicUsername">
                  <Form.Label>Username</Form.Label>
                  <Form.Control onChange={this.changeHandler} type="text" name="username" placeholder="Enter Username" required/>
                </Form.Group>

                <Form.Group controlId="formBasicEmail">
                  <Form.Label>Email address</Form.Label>
                  <Form.Control onChange={this.changeHandler} type="text" name="email" placeholder="Enter Email" required />
                </Form.Group>


                <Form.Group controlId="formBasicPassword">
                  <Form.Label>Password</Form.Label>
                  <Form.Control onChange={this.changeHandler} type="text" name="password" placeholder="Enter Password" required />
                </Form.Group>

                <Button variant="primary" onClick={this.createUser}>
                  Create Account
                </Button>
                <Button className="ml-3" variant="primary" onClick={this.login}>
                  Login
              </Button>
              </Form>
              </>
              }
              
            </div>

          </div>
        </div>
      </>
    )
  }
}
export default Account