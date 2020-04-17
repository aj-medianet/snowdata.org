import React, { Component } from 'react';
//import logo from './logo.svg';
import './App.css';

import HeaderContent from './components/HeaderContent'
import MainContent from './components/MainContent'
import FooterContent from './components/FooterContent'

class App extends Component {
  constructor() {
    super()
    this.state = {

    }
  }

  render() {
    return (
      <div>
        <HeaderContent />
        <MainContent />
        <FooterContent />
      </div>
    )
  }
}

export default App;

