import React, { Component } from 'react';
import { BrowserRouter, Route, Switch, } from  'react-router-dom';
import back from './images/back.jpg'

//import logo from './logo.svg';
import './App.css';

import Navigation from './components/Nav'
import MainContent from './components/MainContent'
import About from './components/About'
import Account from './components/Account'
import APITest from './components/APITest'
import QuickStart from './components/QuickStart'
import Documentation from './components/Documentation'
import Pricing from './components/Pricing'
import MtBaker from './components/MtBaker'
import MtBachelor from './components/MtBachelor'
import Bridger from './components/Bridger'
import Snowbird from './components/Snowbird'
import SkiAreas from './components/SkiAreas'

class App extends Component {
  constructor() {
    super()
    this.state = {

    }
  }
  render() {
    return (
      <BrowserRouter>
        <div className="App">
          <Navigation/>
            <Switch>
              <Route path="/" component={MainContent} exact/>
              <Route path="/about" component={About}/>
              <Route path="/account" component={Account}/>
              <Route path="/apitest" component={APITest}/>
              <Route path="/api-quick-start" component={QuickStart}/>
              <Route path="/api-documentation" component={Documentation}/>
              <Route path="/api-pricing" component={Pricing}/>
              <Route path="/mtbaker" component={MtBaker}/>
              <Route path="/mtbachelor" component={MtBachelor}/>
              <Route path="/bridger" component={Bridger}/>
              <Route path="/snowbird" component={Snowbird}/>
              <Route path="/allareas" component={SkiAreas}/>
            </Switch>
        </div>
      </BrowserRouter>
    );
  }
}
export default App