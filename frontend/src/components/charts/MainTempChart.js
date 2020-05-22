import React, { Component } from 'react';
import Highcharts from 'highcharts';
import HighchartsReact from 'highcharts-react-official';

class TempChart extends Component {
    // constructor(props) {
    //     super(props);
    // }
    cleanOptions(){
    
        const temp = this.props.data.filter(area => {
            return area.cur_temp !== "";
            })
            .map(area => {
            const data = {}
            data.name = area.name;
            data.y = Number(area.cur_temp);
            return data;
        })
        const temp_arr_big = temp.map(Object.values).sort(function(x,y) {
            return y[1] - x[1];
        })

        let temp_arr = [];
        for(let i=0; i<5; i++) {
            temp_arr.push(temp_arr_big[i]);
        }
        
        const options = {
            chart: {
                type: 'column'
            },
            credits: {
                enabled: false,
            },
            title: {
            text: 'Current Temperature'
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
                    text: 'Degrees (F)'
                }
            },
            legend: {
                enabled: false
            },
            tooltip: {
                pointFormat: '<b>{point.y:f} degrees F</b>'
            },
            series: [{
                name: 'Temp',
                data: temp_arr
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

export default TempChart
