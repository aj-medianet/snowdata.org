import React, { Component } from 'react';
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'
import Spinner from 'react-bootstrap/Spinner'
//import Cookies from 'js-cookie';

// displays user account info
class TestSesssion extends Component {
  constructor() {
    super()
    this.state = {
      returnData: "",
      username: "",
      email: "",
      password: "",
      errMessage: "",
      successMessage: "",
      isLoading: false,
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

  // makes sure form is filled out
  checkEmptyFields = () => {
    if (this.state.username === "" || this.state.email === "" || this.state.password === "") {
      this.setState({ errMessage: "Please fill in all fields" })
      return false;
    }
    this.setState({ errMessage: "" })
    return true;
  }

  login = (event) => {
    event.preventDefault()
    console.log("sending GET req")

    fetch('https://api.snowdata.org/test-session', {
    //fetch('http://localhost:7082/test-session', {
      method: 'GET',
      credentials: 'include',
      //headers: { 'Content-Type': 'application/json', },
    }).then((response) => {
      return response
    }).then((data) => {
      console.log("data:", data)
    }).catch((err) => {
      this.setState({ errMessage: err })
      console.log("error:", err)
      return
    })

  }



  reloadWindow = () => {
    window.location.reload()
  }

  render() {
    return (
      <>
        <div className="container-fluid pt-5" >
          

          <>
            {this.state.isLoading ? <div className="pt-5 pb-5"><this.LoadingSpinner /></div> :

              <div className="row">
                <div className="col text-left m-3">
                  <p className="text-danger">{this.state.errMessage ? this.state.errMessage : ''}</p>
                  <p className="text-success">{this.state.successMessage ? this.state.successMessage : ""}</p>
                    <>
                      <h2>Test Session</h2>
                      <Form>
                        
                        <Button className="ml-3" variant="primary" onClick={this.login}>
                          Get Test Session Data
                        </Button>
                      </Form>
                    </>
                </div>
              </div>
            }
          </>
        </div>
      </>
    )
  }
}
export default TestSesssion