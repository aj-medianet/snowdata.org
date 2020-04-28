import React, { Component } from 'react';

class About extends Component {
    constructor() {
      super()
      this.state = {
        
      }
    }
    render() {
      return (
        <div>
            <h1>About Us</h1>
            <p>The goal of the project is to create an application that allows the public
            to access real time mountain snow data by scraping ski resorts web pages.
            The application will provide a website with all of the data (charts/graphs etc)
            as well as an API for people to access the data themselves. The project will look
            to provide real time data, monthly averages and totals as well as data analysis
            pertaining to weather, snow quality/quantity and trends.</p>

            <p>Current snow data collection methods are an expensive and time consuming process.
            Researchers have to obtain grants and purchase expensive equipment, then gather 
            the data and make sure the equipment works. Mountain snowpacks are especially hard
            to get data on because the terrain makes them hard to access. By using ski areas 
            resources we can gather data using existing infrastructure and could provide a useful
            resource to scientists. We’ve looked at other instruments that collect mountain snow data
            like the SNOTEL program. By comparing a SNOTEL site to the ski area at the same location,
            the measurements can be quite different. Having more data to add to the total picture can
            help improve the accuracy. Another project we looked at is a crowd sourced solution through 
            the Community Snow Observations (CSO) group. By comparing our data with other sources 
            we can look for bias and account for it.</p>
            <p>Authors:</p>
            <ul>
                <li>Andrew Joseph</li>
                <li>Rustin Winger</li>
                <li>Robert Pringsten</li>
            </ul>
            <a href="github.com/aj-medianet/snowdata.org">GitHub Repository</a>
        </div>
      )
    }
  }
  export default About