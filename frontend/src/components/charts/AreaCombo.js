//////// TODO /////////////
import React, { Component } from 'react';
import Highcharts from 'highcharts';
import HighchartsReact from 'highcharts-react-official';

class AreaCombo extends Component {
    
    cleanOptions() {
        
        //TODO hook up to actual site
        var month_data = [
            {"avg_temp":"20","id":0,"month":"5","ski_area_name":"Alpental","snow_depth":"10","total_new_snow":"10",year:"2020","ytd":"100"},
            {"avg_temp":"20","id":1,"month":"12","ski_area_name":"Alpental","snow_depth":"10","total_new_snow":"10",year:"2019","ytd":"50"},
            {"avg_temp":"20","id":2,"month":"1","ski_area_name":"Alpental","snow_depth":"10","total_new_snow":"10",year:"2020","ytd":"60"},
            {"avg_temp":"20","id":3,"month":"2","ski_area_name":"Alpental","snow_depth":"10","total_new_snow":"10",year:"2020","ytd":"70"},
            {"avg_temp":"20","id":4,"month":"4","ski_area_name":"Alpental","snow_depth":"10","total_new_snow":"10",year:"2020","ytd":"80"},
            {"avg_temp":"20","id":5,"month":"3","ski_area_name":"Alpental","snow_depth":"10","total_new_snow":"10",year:"2020","ytd":"90"}
        ]; 

        // convert to nums 
        const season = month_data.map(month => {
            var grouped = {}
            grouped.avg_temp = Number(month.avg_temp);
            grouped.month = Number(month.month);
            grouped.year = Number(month.year);
            grouped.ytd = Number(month.ytd);
            return grouped
        })

        // sort array by year and month
        let sorted = season.sort((a, b) => (a.year > b.year) ? 1 : (a.year === b.year) ? ((a.month > b.month) ? 1 : -1) : -1 )
        
        // convert month numbers into month names
        const month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
        const sorted_month_name = sorted.map(element => {
            element.month = month_names[element.month-1];
            return element;
        })
        
        // create arrays for highcahrts
        const months = sorted_month_name.map(x => x.month)
        const ytds = sorted_month_name.map(x => x.ytd)
        const temps = sorted_month_name.map(x => x.avg_temp)

        // Get max year - useful when working with multiple seasons
        /*const max_year = years.reduce(function(x,y) {
            return (x > y ? x : y)
        })*/

        const options = {
        //src: https://www.highcharts.com/demo/combo-multi-axes
        chart: {
            zoomType: 'xy'
        },
        credits: {
            enabled: false,
        },
        title: {
            text: '',
        },
        xAxis: [{
            categories: months,
            crosshair: true
        }],
        yAxis: [{ // Primary yAxis
            labels: {
                format: '{value}°F',
                style: {
                    color: Highcharts.getOptions().colors[1]
                }
            },
            title: {
                text: 'Temperature',
                style: {
                    color: Highcharts.getOptions().colors[1]
                }
            },
            opposite: true

        }, { // Secondary yAxis
            gridLineWidth: 0,
            title: {
                text: 'YTD',
                style: {
                    color: Highcharts.getOptions().colors[0]
                }
            },
            labels: {
                format: '{value} in',
                style: {
                    color: Highcharts.getOptions().colors[0]
                }
            }

        }],
        tooltip: {
            shared: true
        },
        legend: {
            layout: 'vertical',
            align: 'left',
            x: 80,
            verticalAlign: 'top',
            y: 55,
            floating: true
        },
        series: [{
            name: 'YTD',
            type: 'column',
            yAxis: 1,
            data: ytds,
            tooltip: {
                valueSuffix: '"'
            }

        }, {
            name: 'Temperature',
            type: 'spline',
            data: temps,
            tooltip: {
                valueSuffix: ' °F'
            }
        }],
        responsive: {
            rules: [{
                condition: {
                    maxWidth: 500
                },
                chartOptions: {
                    legend: {
                        floating: false,
                        layout: 'horizontal',
                        align: 'center',
                        verticalAlign: 'bottom',
                        x: 0,
                        y: 0
                    },
                    yAxis: [{
                        labels: {
                            align: 'right',
                            x: 0,
                            y: -6
                        },
                        showLastLabel: false
                    }, {
                        labels: {
                            align: 'left',
                            x: 0,
                            y: -6
                        },
                        showLastLabel: false
                    }, {
                        visible: false
                    }]
                }
            }]
        }
        }
        return options;
    }
    
        render() {
        return (
            <div>
                <HighchartsReact highcharts={Highcharts} options={this.cleanOptions()} />
            </div>
        )
    }
}



export default AreaCombo