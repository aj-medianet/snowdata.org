import React, { Component } from 'react';
//import { useState, useEffect } from 'react';

// displays individual skiareas
class SkiAreas extends React.Component {
    constructor(props) {
        super(props);
          this.state = {
              skiareas: []
        }
      }
    
      componentDidMount() {  
        const url = 'https://api.snowdata.org/get-all-data/tmpkey';
        //const url = 'http://localhost:7082/get-all-data/tmpkey';
      fetch(url)
      .then(response => response.json())
      .then(skiareas => this.setState({skiareas}));
      }
      
    render() {
      return (
        <div>
          <ul>
            {
              this.state.skiareas.map(area => 
                <div key={area.id}>
                  {
                    <div>
                    <h1>{area.name}</h1>
                    <div>Current temperature: {area.cur_temp}</div>
                    <div>Wind speed: {area.wind_speed}</div>
                    <div>Wind direction: {area.wind_dir}</div>
                    <div>12 Hour snowfall: {area.new_snow_12}</div>
                    <div>24 Hour snowfall: {area.new_snow_24}</div>
                    <div>48 Hour snowfall: {area.new_snow_48}</div>
                    <div>Current snow depth: {area.cur_depth}</div>
                    <div>YTD: {area.ytd}</div>
                    </div>
                  }
                  </div>
              )
            }
          </ul>
        </div>
      );
    }
    }


export default SkiAreas;
    