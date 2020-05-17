import React, { Component } from 'react';
import BarChart from './BarChart';
import Table from './Table';
import Spinner from 'react-bootstrap/Spinner'
//import Row from 'react-bootstrap/Row';
//import Col from 'react-bootstrap/Col';

class MainContent extends Component {
  constructor() {
    super()
    this.state = {
      skiareas: [],
      skiAreasMonthly: [],
      isLoading: false,
    }
  }

  componentDidMount() {
    this.setState({ isLoading: true })
    fetch('https://api.snowdata.org/get-all-data/tmpkey')
      .then(response => response.json())
      .then((skiareas) => {
        this.setState({ skiareas })
        this.setState({ isLoading: false })
      })

    fetch('https://api.snowdata.org/get-all-monthly-data/tmpkey')
      .then(response => response.json())
      .then((skiAreasMonthly) => {
        this.setState({ skiAreasMonthly })
        console.log(skiAreasMonthly)
        this.setState({ isLoading: false })
      })

  }

  // handles loading spinner
  LoadingSpinner = () => {
    return this.state.isLoading ? <Spinner className="ml-2" animation="border" variant="success" /> : ''
  }

  render() {
    return (
      <>
        {this.state.isLoading ? <div className="pt-5 pb-5"><this.LoadingSpinner /></div> :
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
            
            <Table data={this.state.skiareas} />
          </div>
        }
      </>
    )
  }
}
export default MainContent 
