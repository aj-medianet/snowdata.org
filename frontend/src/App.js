import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  constructor() {
    super()
    this.state = {

    }
  }

  getTest = (event) => {
    console.log("GET test")
    event.preventDefault()
    fetch("http://localhost:7082")
      .then((response) => {
        return response.json()
      })
      .then((data) => {
        console.log(data)
      })
  }

  postTest = (event) => {
    console.log("POST test")
    event.preventDefault()
  }

  render() {
    return (
      <div className="container-fluid p-5">
        <div className="row">
          <div className="col text-center">
            <h1>API Test</h1>
            <button className="btn btn-primary mt-3 mr-2" onClick={this.getTest}>GET Request Test</button>
            <button className="btn btn-primary mt-3 ml-2" onClick={this.postTest}>POST Request Test</button>
          </div>
        </div>
      </div>
    )
  }
}

export default App;

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;
