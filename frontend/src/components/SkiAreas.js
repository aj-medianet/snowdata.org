import React, { Component } from 'react';
//import { useState, useEffect } from 'react';


// TODO
// dynamically loads a ski area depending on user choice from nav dropdown
class SkiAreas extends Component {
  constructor(props) {
    super(props);
    this.state = {
      skiArea : "",
    }
  }

  async componentDidMount() {
    const url = 'https://api.snowdata.org/get-ski-area';
    const dataIn = { 
      skiareaname : this.props.match.params.skiArea,
      api_key : "tmpkey"
    }
    this.setState({ skiArea: this.props.match.params.skiArea })
    console.log(this.state.skiArea)

    const response = await fetch(url, 
      { method: 'POST', headers: {'Content-Type': 'application/json',},
      body: JSON.stringify(dataIn)})
    const dataOut = await response.json();
    this.setState({ skiArea: dataOut, loading: false });
    console.log(dataOut)
  }

  render() {
    return (
      <>
        <h1>{this.props.match.params.skiArea}</h1>
        <div>
            <div>Current temperature: {this.state.skiArea.cur_temp}</div>
            <div>Wind speed: {this.state.skiArea.wind_speed}</div>
            <div>Wind direction: {this.state.skiArea.wind_dir}</div>
            <div>12 Hour snowfall: {this.state.skiArea.new_snow_12}</div>
            <div>24 Hour snowfall: {this.state.skiArea.new_snow_24}</div>
            <div>48 Hour snowfall: {this.state.skiArea.new_snow_48}</div>
            <div>Current snow depth: {this.state.skiArea.cur_depth}</div>
            <div>YTD: {this.state.skiArea.ytd}</div>
        </div>
      </>
      
    );
  }
}


export default SkiAreas;
