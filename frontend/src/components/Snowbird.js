import React, { Component } from 'react';

class Snowbird extends Component {
    state = {
        loading: true,
        ski_area: null
      };

    async componentDidMount() {
      const url = 'http://localhost:7082/get-ski-area';
      const dataIn = { 
        skiareaname : "Snowbird",
        api_key : "tmpkey"
      }
      
      const response = await fetch(url, 
        { method: 'POST', headers: {'Content-Type': 'application/json',},
        body: JSON.stringify(dataIn)})
      const dataOut = await response.json();
      this.setState({ ski_area: dataOut, loading: false });
      console.log(dataOut)
    }

    render() {
      if (this.state.loading) {
        return <div>Loading ski area. . .</div>;
      }
      if (!this.state.ski_area) {
        return <div>No data . . .</div>
      }
      return (
        <div>
            <h1>{this.state.ski_area.name}</h1>
            <div>Current temperature: {this.state.ski_area.cur_temp}</div>
            <div>Wind speed: {this.state.ski_area.wind_speed}</div>
            <div>Wind direction: {this.state.ski_area.wind_dir}</div>
            <div>12 Hour snowfall: {this.state.ski_area.new_snow_12}</div>
            <div>24 Hour snowfall: {this.state.ski_area.new_snow_24}</div>
            <div>48 Hour snowfall: {this.state.ski_area.new_snow_48}</div>
            <div>Current snow depth: {this.state.ski_area.cur_depth}</div>
            <div>YTD: {this.state.ski_area.ytd}</div>
        </div>
      );
    }
  }

  export default Snowbird
