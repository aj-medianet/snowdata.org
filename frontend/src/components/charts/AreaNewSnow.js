import React, { Component } from 'react';
import Highcharts from 'highcharts';
import HighchartsReact from 'highcharts-react-official';

class AreaNewSnow extends Component {
    
    cleanOptions() {
        var data = this.props.data
        
        let values = []
        let catagories = []
        if(data.new_snow_12 !== "") {
            values.push(Number(data.new_snow_12));
            catagories.push("12 Hour")
        }
        
        if(data.new_snow_24 !== "") {
            values.push(Number(data.new_snow_24));
            catagories.push("24 Hour")
        }

        if(data.new_snow_48 !== "") {
            values.push(Number(data.new_snow_48));
            catagories.push("48 Hour")
        }

        const options = {
            chart: {
            type: 'column'
            },
            title: {
                text: 'Recent Snowfall'
            },
            credits: {
                enabled: false,
            },
            xAxis: {
                categories: catagories,
                crosshair: true
            },
            yAxis: {
                min: 0,
                title: {
                    text: 'Snowfall (inches)'
                }
            },
            tooltip: {
                headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
                pointFormat: '<b> {point.y:f}"</b></td></tr>',
                footerFormat: '</table>',
                shared: true,
                useHTML: true
            },
            plotOptions: {
                column: {
                    pointPadding: 0.2,
                    borderWidth: 0
                }
            },
            series: [{
                name: data.name,
                data: values
        
            }]
        }
    return options
    }
        
    render() {
        return (
            <div>
                <HighchartsReact highcharts={Highcharts} options={this.cleanOptions()}  />
            </div>
        )
    }
}



export default AreaNewSnow