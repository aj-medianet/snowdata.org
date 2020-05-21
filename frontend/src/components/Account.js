import React, { Component } from 'react';
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'
import Spinner from 'react-bootstrap/Spinner'
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
      isLoading: false,
    }
  }

  componentDidMount() {
    if (sessionStorage.getItem('status') === 'loggedIn') {
      console.log("logged in Username: " + sessionStorage.getItem("username"))
      console.log("logged in Password: " + sessionStorage.getItem("password"))
    }
    else {
      console.log("logged out Username: " + sessionStorage.getItem("username"))
    }
  }

  // handles loading spinner
  LoadingSpinner = () => {
    return this.state.isLoading ? <Spinner className="ml-2" animation="border" variant="success" /> : ''
  }

  changeHandler = (event) => {
    let key = event.target.name
    let val = event.target.value
    this.setState({ [key]: val })
  }

  checkEmailAddress = (event) => {

    let re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

    if (re.test(this.state.email)) {
      return true;
    }
    else {
      // invalid email, maybe show an error to the user.
      this.setState({ errMessage: "Please enter a valid email address" })
      this.setState({ successMessage: "" });
      this.setState({ isLoading: false })
      return false;
    }
  }

  // check that the password length and has special chacters etc
  checkPassword = () => {
    if (this.state.password.length < 10) {
      this.setState({ passwordError: true })
      this.setState({isLoading: false})
      return false
    }
    this.setState({ passwordError: false })
    this.setState({isLoading: false})
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

  updateEmail = (event) => {
    event.preventDefault()
    this.setState({ isLoading: true })
    if (!this.checkEmailAddress()) { return; }
    this.setState({ successMessage: "" });

    const data = {
      username: sessionStorage.getItem("username"),
      newemail: this.state.email,
      password: sessionStorage.getItem("password")
    }

    fetch('https://api.snowdata.org/update-email', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', },
      body: JSON.stringify(data),
    }).then((response) => {
      return response.json()
    }).then((data) => {
      if (data["message"] !== "Success") {
        this.setState({ errMessage: "Update email failed." });
        this.setState({ successMessage: "" });
        this.setState({ isLoading: false })
      } else {
        this.setState({ errMessage: "" });
        this.setState({ successMessage: "Email Updated Successfully" });
        this.setState({ isLoading: false })
      }
    })
  }

  updatePassword = (event) => {
    event.preventDefault()
    this.setState({ isLoading: true })
    if (!this.checkPassword()) { return; }
    this.setState({ successMessage: "" });
    const data = {
      username: sessionStorage.getItem("username"),
      newpassword: this.state.password,
      password: sessionStorage.getItem("password")
    }

    fetch('https://api.snowdata.org/update-password', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', },
      body: JSON.stringify(data),
    }).then((response) => {
      return response.json()
    }).then((data) => {
      if (data["message"] !== "Success") {
        this.setState({ errMessage: "Update password failed." });
        this.setState({ successMessage: "" });
        this.setState({ isLoading: false })
      } else {
        sessionStorage.setItem("password", this.state.password)
        this.setState({ errMessage: "" });
        this.setState({ successMessage: "Password Updated Successfully" });
        this.setState({ isLoading: false })
      }
    })

  }

  createUser = (event) => {
    event.preventDefault()
    this.setState({ isLoading: true })
    if (!this.checkEmptyFields()) { return; }
    if (!this.checkPassword()) { return; }
    if (!this.checkEmailAddress()) { return; }
    this.setState({ successMessage: "" });

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
      if (data["message"] !== "Success") {
        this.setState({ errMessage: "Account creation failed. Please try a different username." });
        this.setState({ successMessage: "" });
        sessionStorage.setItem('status', null);
        this.setState({ isLoading: false })
      } else {
        sessionStorage.setItem('status', 'loggedIn');
        sessionStorage.setItem('username', this.state.username);
        sessionStorage.setItem('password', this.state.password);
        sessionStorage.setItem("apiKey", data["api_key"]);
        this.setState({ errMessage: "" });
        this.setState({ isLoading: false })
      }
    })
  }

  login = (event) => {
    event.preventDefault()
    this.setState({ isLoading: true })
    if (!this.checkEmptyFields()) { return; }
    if (!this.checkPassword()) { return; }
    if (!this.checkEmailAddress()) { return; }

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
      if (data["message"] !== "Success") {
        this.setState({ errMessage: "Failed to login. Please check username and password." })
        this.setState({ successMessage: "" });
        sessionStorage.setItem('status', null);
        this.setState({ isLoading: false })
      } else {
        sessionStorage.setItem('status', 'loggedIn');
        sessionStorage.setItem('username', this.state.username);
        sessionStorage.setItem('password', this.state.password);
        sessionStorage.setItem("apiKey", data["api_key"])
        this.setState({ errMessage: "" });
        this.setState({ isLoading: false })
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
    this.setState({ username: "" });
    this.setState({ password: "" });
  }

  reloadWindow = () => {
    window.location.reload()
  }


  deleteAccount = (event) => {
    this.setState({ isLoading: true })
    const data = {
      username: sessionStorage.getItem("username"),
      password: sessionStorage.getItem("password")
    }

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
        this.setState({ isLoading: false })
      } else {
        this.setState({ successMessage: "Account Deleted" });
        sessionStorage.setItem('status', null);
        sessionStorage.setItem('username', '');
        sessionStorage.setItem('password', '');
        this.setState({ isLoading: false })
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

          <>
            {this.state.isLoading ? <div className="pt-5 pb-5"><this.LoadingSpinner /></div> :

              <div className="row">
                <div className="col text-left m-3">
                  <p className="text-danger">{this.state.passwordError ? 'Password must be at least 10 characters' : ''}</p>
                  <p className="text-danger">{this.state.errMessage ? this.state.errMessage : ''}</p>
                  <p className="text-success">{this.state.successMessage ? this.state.successMessage : ""}</p>


                  {sessionStorage.getItem("status") === "loggedIn" ?

                    <>
                      <h2>Hello {sessionStorage.getItem("username")}</h2>
                      <div className="row">
                        <div className="col-sm my-3">
                          <p className=""><b>API Key:</b> {sessionStorage.getItem("apiKey")}</p>
                          <Button className="" variant="primary" onClick={this.logout}>
                            Logout
                          </Button>
                          <Button className="ml-3" variant="danger" onClick={() => { if (window.confirm('Are you sure you want to delete your account?')) { this.deleteAccount() }; }}>
                            Delete Account
                          </Button>
                        </div>
                      </div>
                      <div className="row">
                        <div className="col-sm my-3">
                          <Form>
                            <Form.Group controlId="formBasicEmail" >
                              <Form.Label>Update Email</Form.Label>
                              <Form.Control className="w-25" onChange={this.changeHandler} type="email" name="email" placeholder="Enter New Email" required />
                            </Form.Group>
                          </Form>
                          <Button className="" variant="primary" onClick={this.updateEmail}>
                            Update Email
                          </Button>
                        </div>
                      </div>
                      <div className="row">
                        <div className="col-sm my-3">
                          <Form>
                            <Form.Group controlId="formBasicPassword">
                              <Form.Label>Update Password</Form.Label>
                              <Form.Control className="w-25" onChange={this.changeHandler} type="password" name="password" placeholder="Enter New Password" required />
                            </Form.Group>
                          </Form>
                          <Button className="" variant="primary" onClick={this.updatePassword}>
                            Update Password
                          </Button>

                        </div>
                      </div>
                    </>

                    :

                    <>
                      <h2>Create Account or Login</h2>
                      <Form>
                        <Form.Group controlId="formBasicUsername">
                          <Form.Label>Username</Form.Label>
                          <Form.Control className="w-25" onChange={this.changeHandler} type="text" name="username" placeholder="Enter Username" required />
                        </Form.Group>

                        <Form.Group controlId="formBasicEmail">
                          <Form.Label>Email address</Form.Label>
                          <Form.Control className="w-25" onChange={this.changeHandler} type="email" name="email" placeholder="Enter Email" required />
                        </Form.Group>

                        <Form.Group controlId="formBasicPassword">
                          <Form.Label>Password</Form.Label>
                          <Form.Control className="w-25" onChange={this.changeHandler} type="password" name="password" placeholder="Enter Password" required />
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
            }
          </>
        </div>
      </>
    )
  }
}
export default Account