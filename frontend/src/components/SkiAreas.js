import React, { Component } from 'react';
import Spinner from 'react-bootstrap/Spinner'
//import { useState, useEffect } from 'react';


// dynamically loads a ski area depending on user choice from nav dropdown
class SkiAreas extends Component {
  constructor(props) {
    super(props);
    this.state = {
      skiArea: "",
      skiAreaMonthly: "",
      data: true,
      isLoading: false,
      errMessage: "",
    }
  }

  async componentDidMount() {
    this.setState({ isLoading: true })
    const dataIn = {
      skiareaname: this.props.match.params.skiArea,
      api_key: "tmpkey"
    }

    fetch('https://api.snowdata.org/get-ski-area', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', },
      body: JSON.stringify(dataIn),
    }).then((response) => {
      return response.json()
    }).then((data) => {
      if (data["message"] !== "Fail") {
        this.setState({ skiArea: data })
        this.checkNoData()
        this.setState({ isLoading: false })
      } else {
        this.setState({ errMessage: data })
        this.setState({ isLoading: false })
      }
    })

    fetch('https://api.snowdata.org/get-ski-area-monthly-data', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', },
      body: JSON.stringify(dataIn),
    }).then((response) => {
      return response.json()
    }).then((data) => {
      if (data["message"] !== "Fail") {
        this.setState({ skiAreaMonthly: data })
        this.setState({ isLoading: false })
        console.log(data)
      } else {
        this.setState({ errMessage: data })
        this.setState({ isLoading: false })
      }
    })
  }



  // handles loading spinner
  LoadingSpinner = () => {
    return this.state.isLoading ? <Spinner className="ml-2" animation="border" variant="success" /> : ''
  }

  checkNoData = () => {
    var hasData = false;
    for (var key in this.state.skiArea) {
      if (this.state.skiArea[key] !== "" && key !== "name" && key !== "ts") {
        hasData = true;
      }
    }
    this.setState({ data: hasData })
  }

  render() {
    return (
      <>
        <h1 className="pt-5 pb-3">{this.props.match.params.skiArea}</h1>
        {this.state.isLoading ? <div className="pt-5 pb-5"><this.LoadingSpinner /></div> :
          <>

            {this.state.data ?
              <div >

                <div>Current temperature: {this.state.skiArea.cur_temp}</div>
                <div>Wind speed: {this.state.skiArea.wind_speed}</div>
                <div>Wind direction: {this.state.skiArea.wind_dir}</div>
                <div>12 Hour snowfall: {this.state.skiArea.new_snow_12}</div>
                <div>24 Hour snowfall: {this.state.skiArea.new_snow_24}</div>
                <div>48 Hour snowfall: {this.state.skiArea.new_snow_48}</div>
                <div>Current snow depth: {this.state.skiArea.cur_depth}</div>
                <div>YTD: {this.state.skiArea.ytd}</div>

              </div>

              :

              <h3 >This Ski Area has stopped reporting Snow Data for the season</h3>
            }
          </>
        }
      </>

    );
  }
}


export default SkiAreas;
