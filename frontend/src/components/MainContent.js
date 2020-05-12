import React, { Component } from 'react';
//import '../App.css';
import BarChart from './BarChart';
import Table from './Table';
//import Row from 'react-bootstrap/Row';
//import Col from 'react-bootstrap/Col';

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

  renderChart() {
    if (this.state.skiareas.length === 0) {
      return "no data"
    }
    return <BarChart data={this.state.skiareas}/>
  }

  render() {
    return (

      <div className="pt-5 pb-5">
        
          {
            this.state.skiareas.map(area =>
              <div key={area.id}>
                {
                  <div>
                    <h1 className="pt-3 pb-3">{area.name}</h1>
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
          <div>{this.renderChart()}</div>
          <Table data={this.state.skiareas} />
      </div>

    )
  }
}
export default MainContent 
