import React, { Component } from 'react';
import Highcharts from 'highcharts';
import HighchartsReact from 'highcharts-react-official';

class MainChart extends Component {
    getYAxis(type) {
        switch (type) {
          case 'wind': return 'Wind Speed (mph)'
          case 'temp': return 'Degrees (fahrenheit)'
          case 'ytd': return 'Snowfall (inches)'
          case 'depth': return 'Snowfall (inches)'
        }
    }
    getTitle(type) {
        switch (type) {
            case 'wind': return 'Current Wind Speed'
            case 'temp': return 'Current Temperature'
            case 'ytd': return 'Year To Date'
            case 'depth': return 'Snow Depth'
        }
    }
    getTooltip(type) {
        switch (type) {
            case 'wind': return '<b>{point.y:f} mph</b>'
            case 'temp': return '<b>{point.y:f} °F</b>'
            case 'ytd': return '<b>{point.y:f}"</b>'
            case 'depth': return '<b>{point.y:f}"</b>'
        }
    }
    getDataset(type) {
        switch (type) {
            case 'wind': return this.getTopFive('wind_speed')
            case 'temp': return this.getTopFive('cur_temp')
            case 'ytd': return this.getTopFive('ytd')
            case 'depth': return this.getTopFive('cur_depth')
        }
    }
    getTopFive(variable) {
        const depth = this.props.data.filter(area => {
            return area[variable] !== "";
            }).map(area => {
                const data = {}
                data.name = area.name;
                data.val = Number(area[variable]);
                return data;
        })
        const depth_arr_big = depth.map(Object.values).sort(function(x,y) {
            return y[1] - x[1];
        })
        let depth_arr = [];
        for(let i=0; i<5; i++) {
            depth_arr.push(depth_arr_big[i]);
        }
        return depth_arr
    }

    cleanOptions() {
        const options = {
            chart: {
                type: 'column'
            },
            credits: {
                enabled: false,
            },
            title: {
            text: this.getTitle(this.props.type)
            },
            xAxis: {
                type: 'category',
                labels: {
                    rotation: -45,
                    style: {
                        fontSize: '13px',
                        fontFamily: 'Verdana, sans-serif'
                    }
                }
            },
            yAxis: {
                min: 0,
                title: {
                    text: this.getYAxis(this.props.type)
                }
            },
            legend: {
                enabled: false
            },
            tooltip: {
                pointFormat: this.getTooltip(this.props.type)
            },
            series: [{
                name: this.props.type,
                data: this.getDataset(this.props.type)
            }
            ]         
        } 
        return options
    }

    render() {
        return ( 
            <div>
            <HighchartsReact highcharts={Highcharts} options={this.cleanOptions()} />
            </div>
        )
    }
      
}

export default MainChart