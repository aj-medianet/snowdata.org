import React, { Component } from 'react';
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'
//import Cookies from 'js-cookie';

// displays user account info
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
    }
  }

  componentDidMount() {
    if (sessionStorage.getItem('status') === 'loggedIn') {
      console.log("logged in Username: " + sessionStorage.getItem("username"))
    }
    else {
      console.log("logged out Username: " + sessionStorage.getItem("username"))
    }
  }

  changeHandler = (event) => {
    let key = event.target.name
    let val = event.target.value
    this.setState({ [key]: val })
  }

  checkEmailAddress = (event) => {
    
    let re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

    if ( re.test(this.state.email) ) {
      //emaill address is valid so update it
      return true;
    }
    else {
        // invalid email, maybe show an error to the user.
        this.setState({ errMessage: "Please enter a valid email address" })
        return false;
    }
  }

  // check that the password length and has special chacters etc
  checkPassword = () => {
    if (this.state.password.length < 10) {
      this.setState({ passwordError: true })
      return false
    }
    this.setState({ passwordError: false })
    return true
  }

  // makes sure form is filled out
  checkEmptyFields = () => {
    if (this.state.username === "" || this.state.email === "" || this.state.password === "") {
      this.setState({ errMessage: "Please fill in all fields" })
      return false;
    }
    this.setState({ errMessage: "" })
    return true;
  }

  createUser = (event) => {
    event.preventDefault()
    if (!this.checkEmptyFields()) { return; }
    if (!this.checkPassword()) { return; }
    if (!this.checkEmailAddress()) { return; }

    const data = {
      username: this.state.username,
      email: this.state.email,
      password: this.state.password
    }
    
    //fetch('http://localhost:7082/create-user', {
    fetch('https://api.snowdata.org/create-user', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', },
      body: JSON.stringify(data),
    }).then((response) => {
      return response.json()
    }).then((data) => {
      if (data["message"] !== "Success") {
        this.setState({ errMessage: "Account creation failed. Please try a different username" });
        this.setState({ successMessage: "" });
        sessionStorage.setItem('status', null);
      } else {
        sessionStorage.setItem('status', 'loggedIn');
        sessionStorage.setItem('username', this.state.username);
        sessionStorage.setItem('password', this.state.password);
        sessionStorage.setItem("apiKey", data["api_key"]);
        this.setState({ errMessage: "" });
      }
    }).catch((err) => {
      this.setState({ errMessage: err })
    })

  }

  login = (event) => {
    event.preventDefault()
    if (!this.checkEmptyFields()) { return; }
    if (!this.checkPassword()) { return; }
    if (!this.checkEmailAddress()) { return; }

    const data = {
      username: this.state.username,
      password: this.state.password
    }
    
    //fetch('http://localhost:7082/login', {
    fetch('https://api.snowdata.org/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', },
      body: JSON.stringify(data),
    }).then((response) => {
      return response.json()
    }).then((data) => {
      if (data["message"] !== "Success") {
        this.setState({ errMessage: "Failed to login. Please check username and password" })
        this.setState({ successMessage: "" });
        sessionStorage.setItem('status', null);
      } else {
        sessionStorage.setItem('status', 'loggedIn');
        sessionStorage.setItem('username', this.state.username);
        sessionStorage.setItem('password', this.state.password);
        sessionStorage.setItem("apiKey", data["api_key"])
        this.setState({ errMessage: "" });
      }
    }).catch((err) => {
      this.setState({ errMessage: err })
      return
    })

  }

  logout = (event) => {
    sessionStorage.setItem('status', null);
    sessionStorage.setItem('username', '');
    sessionStorage.setItem('password', '');
    this.setState({username: ""});
    this.setState({password: ""});
    window.location.reload();
  }

  reloadWindow = () => {
    window.location.reload()
  }


  deleteAccount = (event) => {
    const data = {
      username: sessionStorage.getItem("username"),
      password: sessionStorage.getItem("password")
    }

    //fetch('http://localhost:7082/delete-user', {
    fetch('https://api.snowdata.org/delete-user', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', },
      body: JSON.stringify(data),
    }).then((response) => {
      return response.json()
    }).then((data) => {
      if (data["message"] !== "Success") {
        this.setState({ errMessage: "Failed to delete account. Please log back in and retry." })
        this.setState({ successMessage: "" });
        this.logout()
      } else {
        this.setState({ successMessage: "Account Deleted" });
        sessionStorage.setItem('status', null);
        sessionStorage.setItem('username', '');
        sessionStorage.setItem('password', '');
        window.setTimeout(this.reloadWindow, 2000);
        
      }
    }).catch((err) => {
      this.setState({ errMessage: err })
    })
  }

  render() {

    return (
      <>
        <div className="container-fluid pt-5" >
          <div className="row">
            <div className="col text-center">
              <h1 className="mb-3">Account</h1>
            </div>
          </div>

          <div className="row">
            <div className="col text-left m-3">
              <p className="text-danger">{this.state.passwordError ? 'Password must be at least 10 characters' : ''}</p>
              <p className="text-danger">{this.state.errMessage ? this.state.errMessage : ''}</p>
              <p className="text-success">{this.state.successMessage ? this.state.successMessage : ""}</p>


              {sessionStorage.getItem("status") === "loggedIn" ?

                <>
                  <h2>Hello {sessionStorage.getItem("username")}</h2>

                  <p>API Key: {sessionStorage.getItem("apiKey")}</p>

                  <Button className="" variant="primary" onClick={this.logout}>
                    Logout
                  </Button>
                  <Button className="ml-3" variant="danger" onClick={() => { if (window.confirm('Are you sure you want to delete your account?')) { this.deleteAccount() }; }}>
                    Delete Account
                  </Button>
                </>

                :

                <>
                  <h2>Create Account or Login</h2>
                  <Form>
                    <Form.Group controlId="formBasicUsername">
                      <Form.Label>Username</Form.Label>
                      <Form.Control onChange={this.changeHandler} type="text" name="username" placeholder="Enter Username" required />
                    </Form.Group>

                    <Form.Group controlId="formBasicEmail">
                      <Form.Label>Email address</Form.Label>
                      <Form.Control onChange={this.changeHandler} type="email" name="email" placeholder="Enter Email" required />
                    </Form.Group>


                    <Form.Group controlId="formBasicPassword">
                      <Form.Label>Password</Form.Label>
                      <Form.Control onChange={this.changeHandler} type="password" name="password" placeholder="Enter Password" required />
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