import React, { Component } from 'react';
//import D3Chart from './D3Chart';
//import React from 'react';
import { render } from 'react-dom';
import Highcharts from 'highcharts';
import HighchartsReact from 'highcharts-react-official';

class MainYTDChart extends Component {
    constructor(props) {
        super(props);
        
    }
    cleanOptions(){
        const ytd = this.props.data.filter(area => {
            return area.ytd !== "";
            }).map(area => {
            const data = {}
            data.name = area.name;
            data.val = Number(area.ytd);
            return data;
        })
        const ytd_arr = ytd.map(Object.values)
        
        const options = {
            chart: {
              type: 'column'
            },
            title: {
              text: 'Year To Date'
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
                    text: 'Snowfall (inches)'
                }
            },
            legend: {
                enabled: false
            },
            tooltip: {
                pointFormat: 'YTD: <b>{point.y:f} inches</b>'
            },
            series: [{
                name: 'YTD',
                data: 
                    ytd_arr
                ,
                dataLabels: {
                    enabled: true,
                    rotation: -90,
                    color: '#FFFFFF',
                    align: 'right',
                    format: '{point.y:f}', 
                    y: 15, 
                    style: {
                        fontSize: '13px',
                        fontFamily: 'Verdana, sans-serif'
                    }
                }
          }]
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
export default MainYTDChart
