import React, { Component } from 'react';
import Highcharts from 'highcharts';
import HighchartsReact from 'highcharts-react-official';

class MainYTDChart extends Component {
    // constructor(props) {
    //     super(props);

    // }
    cleanOptions() {
        const ytd = this.props.data.filter(area => {
            return area.ytd !== "";
        }).map(area => {
            const data = {}
            data.name = area.name;
            data.val = Number(area.ytd);
            return data;
        })
        const ytd_arr_big = ytd.map(Object.values).sort(function(x,y) {
            return y[1] - x[1];
        })

        let ytd_arr = [];
        for(let i=0; i<5; i++) {
            ytd_arr.push(ytd_arr_big[i]);
        }

        //console.log(ytd_arr);

        const options = {
            chart: {
                type: 'column'
            },
            credits: {
                enabled: false,
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
