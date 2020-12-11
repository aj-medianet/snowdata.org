import React, { Component } from 'react';
import MainDepthChart from './charts/MainDepthChart';
import MainTempChart from './charts/MainTempChart';
import MainWindChart from './charts/MainWindChart';
import MainYTDChart from './charts/MainYTDChart';
import Spinner from 'react-bootstrap/Spinner';
import ErrorBoundary from './ErrorBoundary';
import MainChart from './charts/MainChart';

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
    //fetch('http://localhost:7082/get-all-data/tmpkey')
    fetch('https://api.snowdata.org/get-all-data/tmpkey')
      .then(response => response.json())
      .then((skiareas) => {
        this.setState({ skiareas })
        this.setState({ isLoading: false })
      })

    //fetch('http://localhost:7082/get-all-data/tmpkey')
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
        <h1 className="mt-5">SnowData</h1>
        <div className="m-5">
          {this.state.isLoading ? <div className="pt-5 pb-5"><this.LoadingSpinner /></div> :
            <div className="pt-5 pb-5">


              {/*
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
                */}
              <ErrorBoundary>
              <div className="row">
              <div className="col-sm m-4 mainCard">
                  <MainChart data={this.state.skiareas} type="ytd"/>
                </div>

                <div className="col-sm m-4 mainCard">
                  <MainChart data={this.state.skiareas} type="depth"/>
                </div>
              </div>

              <div className="row">
              <div className="col-sm m-4 mainCard">
                  <MainChart data={this.state.skiareas} type="temp"/>
                </div>

                <div className="col-sm m-4 mainCard">
                  <MainChart data={this.state.skiareas} type="wind"/>
                </div>
              </div>
              </ErrorBoundary>
            </div>
          }
        </div>
      </>
    )
  }
}
export default MainContent 
