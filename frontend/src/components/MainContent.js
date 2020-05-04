import React, { Component } from 'react';
//import '../App.css';

class MainContent extends Component {
  constructor() {
    super()
    this.state = {
      skiareas: []
    }
  }

  componentDidMount() {
    const url = 'https://api.snowdata.org/get-all-data/tmpkey';
    //const url = 'http://localhost:7082/get-all-data/tmpkey';
    fetch(url)
      .then(response => response.json())
      .then(skiareas => this.setState({ skiareas }));
  }

  render() {
    return (

      <div className="p-5">
        <ul>
          {
            this.state.skiareas.map(area =>
              <div key={area.id}>
                {
                  <div>
                    <h1 className="p-3">{area.name}</h1>
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

    )
  }
}
export default MainContent