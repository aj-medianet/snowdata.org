import React, { Component } from 'react';
import { BrowserRouter, Route, Switch, } from  'react-router-dom';

//import logo from './logo.svg';
import './App.css';

import Navigation from './components/Nav'
import MainContent from './components/MainContent'
import About from './components/About'
import Account from './components/Account'
import QuickStart from './components/QuickStart'
import Documentation from './components/Documentation'
import Pricing from './components/Pricing'
import SkiAreas from './components/SkiAreas'
import Footer from './components/FooterContent'
import TC from './components/TC'

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
              <Route path="/api-quick-start" component={QuickStart}/>
              <Route path="/api-documentation" component={Documentation}/>
              <Route path="/api-pricing" component={Pricing}/>
              <Route path="/tc" component={TC}/>
              <Route path="/skiareas/:skiArea" component={SkiAreas}/>
            </Switch>
          <Footer/>
        </div>
      </BrowserRouter>
    );
  }
}
export default App