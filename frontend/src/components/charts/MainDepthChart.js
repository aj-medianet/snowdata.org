import React, { Component } from 'react';
import Highcharts from 'highcharts';
import HighchartsReact from 'highcharts-react-official';

class MainDepthChart extends Component {
    // constructor(props) {
    //     super(props);
        
    // }

    cleanOptions(){
        const depth = this.props.data.filter(area => {
            return area.cur_depth !== "";
            }).map(area => {
            const data = {}
            data.name = area.name;
            data.val = Number(area.cur_depth);
            return data;
        })
        const depth_arr_big = depth.map(Object.values).sort(function(x,y) {
            return y[1] - x[1];
        })

        let depth_arr = [];
        for(let i=0; i<5; i++) {
            depth_arr.push(depth_arr_big[i]);
        }
        
        const options = {
            chart: {
                borderColor: "#000000",
                borderWidth: 2,
                type: 'line',
                type: 'column'
            },
            credits: {
                enabled: false,
            },
            title: {
              text: 'Snow Depth'
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
                pointFormat: '<b>{point.y:f} inches</b>'
            },
            series: [{
                name: 'Depth',
                data: 
                    depth_arr
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
export default MainDepthChart