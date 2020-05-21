//////// TODO /////////////
import React, { Component } from 'react';
import Highcharts from 'highcharts';
import HighchartsReact from 'highcharts-react-official';

class AreaCombo extends Component {
    constructor(props) {
        super(props);

    }
    cleanOptions() {

        //console.log(this.props.cur_data);
        //console.log(this.props.month_data);
        var month_data = [
        {"avg_temp":"20","id":0,"month":"5","ski_area_name":"Alpental","snow_depth":"10","total_new_snow":"10","year":"2020","ytd":"100"},
        {"avg_temp":"20","id":1,"month":"12","ski_area_name":"Alpental","snow_depth":"10","total_new_snow":"10","year":"2019","ytd":"50"},
        {"avg_temp":"20","id":2,"month":"1","ski_area_name":"Alpental","snow_depth":"10","total_new_snow":"10","year":"2020","ytd":"60"},
        {"avg_temp":"20","id":3,"month":"2","ski_area_name":"Alpental","snow_depth":"10","total_new_snow":"10","year":"2020","ytd":"70"},
        {"avg_temp":"20","id":4,"month":"4","ski_area_name":"Alpental","snow_depth":"10","total_new_snow":"10","year":"2020","ytd":"80"},
        {"avg_temp":"20","id":5,"month":"3","ski_area_name":"Alpental","snow_depth":"10","total_new_snow":"10","year":"2020","ytd":"90"}
        ];

        const options = {
            //src: https://www.highcharts.com/demo/combo-multi-axes
        chart: {
            zoomType: 'xy'
        },
        credits: {
            enabled: false,
        },
        title: {
            text: 'Monthly Weather Data',
        },
        xAxis: [{
            categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
            crosshair: true
        }],
        yAxis: [{ // Primary yAxis
            labels: {
                format: '{value}°C',
                style: {
                    color: Highcharts.getOptions().colors[2]
                }
            },
            title: {
                text: 'Temperature',
                style: {
                    color: Highcharts.getOptions().colors[2]
                }
            },
            opposite: true

        }, { // Secondary yAxis
            gridLineWidth: 0,
            title: {
                text: 'Rainfall',
                style: {
                    color: Highcharts.getOptions().colors[0]
                }
            },
            labels: {
                format: '{value} mm',
                style: {
                    color: Highcharts.getOptions().colors[0]
                }
            }

        }, { // Tertiary yAxis
            gridLineWidth: 0,
            title: {
                text: 'Sea-Level Pressure',
                style: {
                    color: Highcharts.getOptions().colors[1]
                }
            },
            labels: {
                format: '{value} mb',
                style: {
                    color: Highcharts.getOptions().colors[1]
                }
            },
            opposite: true
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
            floating: true,
            backgroundColor:
                Highcharts.defaultOptions.legend.backgroundColor || // theme
                'rgba(255,255,255,0.25)'
        },
        series: [{
            name: 'Rainfall',
            type: 'column',
            yAxis: 1,
            data: [49.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4],
            tooltip: {
                valueSuffix: '"'
            }

        }, {
            name: 'Sea-Level Pressure',
            type: 'spline',
            yAxis: 2,
            data: [1016, 1016, 1015.9, 1015.5, 1012.3, 1009.5, 1009.6, 1010.2, 1013.1, 1016.9, 1018.2, 1016.7],
            marker: {
                enabled: false
            },
            dashStyle: 'shortdot',
            tooltip: {
                valueSuffix: ' mb'
            }

        }, {
            name: 'Temperature',
            type: 'spline',
            data: [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6],
            tooltip: {
                valueSuffix: ' °C'
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
                <div>{JSON.stringify(this.props.month_data)}</div>
                <HighchartsReact highcharts={Highcharts} options={this.cleanOptions()} />
            </div>
        )
    }
}



export default AreaCombo