import React, { Component } from 'react';
import Highcharts from 'highcharts';
import HighchartsReact from 'highcharts-react-official';



//const cardinal = { N:0, NNE: 15, NE: 45, ENE: 75,  E: 90, ESE: 105, SE: 135, SSE: 165,  S: 180, SSW: 195, SW: 225, WSW: 255,  W: 270, WNW: 295, NW: 315, NNW: 345 }
//"N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"

class WindChart extends Component {
    constructor(props) {
        super(props);
    }

    cleanOptions(){
    
        const wind = this.props.data.filter(area => {
            return area.wind_dir !== "" && area.wind_speed !=="";
            })
            .map(area => {
            const data = {}
            data.name = area.name;
            data.y = Number(area.wind_speed);
            //data.dir = area.wind_dir;
            return data;
        })
    
        
        //wind_arr = [area name, wind speed, wind direction]
        const wind_arr_big = wind.map(Object.values).sort(function(x,y) {
            return y[1] - x[1];
        })

        let wind_arr = [];
        for(let i=0; i<5; i++) {
            wind_arr.push(wind_arr_big[i]);
        }

        const options = {
            chart: {
            type: 'column'
            },
            credits: {
                enabled: false,
            },
            title: {
            text: 'Current Wind Speed'
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
                    text: 'Wind speed (mph)'
                }
            },
            legend: {
                enabled: false
            },
            tooltip: {
                pointFormat: '<b>{point.y:f} mph</b>'
            },
            series: [{
                name: 'Wind',
                data: wind_arr
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

export default WindChart


