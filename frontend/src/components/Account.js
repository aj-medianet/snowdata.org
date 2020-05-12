import React, { Component } from 'react';
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'
import Cookies from 'js-cookie';

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
      loggedIn: false,
    }
  }

  componentDidMount() {
    if (sessionStorage.getItem('status') === 'loggedIn') {
      this.setState({ loggedIn: true});
      this.setState({ username: sessionStorage.getItem('name')});
      console.log("Username: " + this.state.username)
    }
    else {
      this.setState({ loggedIn: false});
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

    const data = {
      username: this.state.username,
      email: this.state.email,
      password: this.state.password
    }

    fetch('https://api.snowdata.org/create-user', {
      method: 'POST',
      mode: 'cors',
      withCredentials: 'true',
      headers: { 'Content-Type': 'application/json', },
      body: JSON.stringify(data),
    }).then((response) => {
      return response.json()
    }).then((data) => {
      if (data === "Fail") {
        this.setState({ errMessage: data })
      } else {
        this.setState({ apiKey: data });
        this.setState({ errMessage: "" });
        this.setState({ loggedIn: true });
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
      mode: 'cors',
      withCredentials: 'include',
      headers: { 'Content-Type': 'application/json', },
      body: JSON.stringify(data),
    }).then((response) => {
      return response.json()
    }).then((data) => {
      console.log("data: " + data)
      if (data === "Fail") {
        this.setState({ errMessage: data })
        this.setState({ successMessage: "" });
      } else {
        this.setState({ apiKey: data });
        //sessionStorage.setItem('status', 'loggedIn');
        //sessionStorage.setItem('name', this.state.username);
        this.setState({ errMessage: "" });
        this.setState({ loggedIn: true });
        //let cookies = Cookies.get("token")
        //console.log("cookies: " + cookies)
      }
    }).catch((err) => {
      this.setState({ errMessage: err })
      return
    })

  }

  logout = (event) => {
    event.preventDefault()
    const data = {
      username: this.state.username,
    }
    fetch('https://api.snowdata.org/logout', {
      method: 'POST',
      mode: 'cors',
      withCredentials: 'include',
      headers: { 'Content-Type': 'application/json', },
      body: JSON.stringify(data),
    }).then((response) => {
      return response.json()
    }).then((data) => {
      if (data === "Fail") {
        this.setState({ errMessage: "Failed to logout" })
        this.setState({ successMessage: "" });
      } else {        
        this.setState({ loggedIn: false });
      }
    }).catch((err) => {
      this.setState({ errMessage: err })
      return
    })


    sessionStorage.setItem('status', null);
    window.location.reload();

  }

  areYouSure = () => {
    return false;
  }

  deleteAccount = (event) => {
    event.preventDefault()
    if (this.areYouSure()) {
      const data = {
        username: this.state.username,
      }
      fetch('https://api.snowdata.org/delete-user', {
        method: 'POST',
        mode: 'cors',
        withCredentials: 'include',
        headers: { 'Content-Type': 'application/json', },
        body: JSON.stringify(data),
      }).then((response) => {
        return response.json()
      }).then((data) => {
        if (data === "Fail") {
          this.setState({ errMessage: "Failed to delete account" })
          this.setState({ successMessage: "" });
        } else {        
          this.setState({ loggedIn: false });
          this.setState({ successMessage: "Account Deleted" });
        }
      }).catch((err) => {
        this.setState({ errMessage: err })
        return
      })
  
  
      sessionStorage.setItem('status', null);
      window.location.reload();
    }


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


              {this.state.loggedIn ?

                <>
                  <h2>Hello {this.state.username}</h2>
                  
                  <p>API Key: {this.state.apiKey}</p>

                  <Button className="" variant="primary" onClick={this.logout}>
                      Logout
                  </Button>
                  <Button className="ml-3" variant="danger" onClick={this.deleteAccount}>
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