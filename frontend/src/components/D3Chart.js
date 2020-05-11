//TODO figure out less to import
import * as d3 from 'd3';

const MARGIN = { TOP: 20, BOTTOM: 50, LEFT: 70, RIGHT: 10 }
const WIDTH = 800 - MARGIN.LEFT - MARGIN.RIGHT
const HEIGHT = 600 - MARGIN.TOP - MARGIN.BOTTOM

class D3Chart {
    constructor(element, data) {
        const vis = this
        //console.log(data)
        vis.data = data
        vis.svg = d3.select(element)
          .append("svg") // attach svg canvas to page
            .attr("width", WIDTH + MARGIN.LEFT + MARGIN.RIGHT)
            .attr("height", HEIGHT + MARGIN.TOP + MARGIN.BOTTOM)
          .append("g")
            .attr("transform", `translate(${MARGIN.LEFT}, ${MARGIN.TOP})`)
        
            vis.xAxisGroup = vis.svg.append("g")
            .attr("transform", `translate(0, ${HEIGHT})`) 
            
            vis.yAxisGroup = vis.svg.append("g")

            const ytd = data.filter(area => {
            return area.ytd != "";
            }).map(area => {
            const data = {}
            data.name = area.name;
            data.val = area.ytd;
            return data;
            })

            const cur_depth = data.filter(area => {
            return area.cur_depth != "";
            }).map(area => {
            const data = {}
            data.name = area.name;
            data.val = area.cur_depth;
            return data;
            })

            const cur_temp = data.filter(area => {
            return area.temp != "";
            }).map(area => {
            const data = {}
            data.name = area.name;
            data.val = area.cur_temp;
            return data;
            })

            const wind_speed = data.filter(area => {
            return area.wind_speed != "";
            }).map(area => {
            const data = {}
            data.name = area.name;
            data.val = area.wind_speed;
            return data;
            })

            vis.data = ytd
            vis.update()
            //console.log(ytd)
            //console.log(cur_depth)
            //let flag = true
            /*d3.interval(() => {
                vis.data = flag ? ytd : cur_depth  //turn
                vis.update()
                flag =! flag    // set flag to opposite
                }, 3000)        //update every 1 sec  */
    }

    update() {
        let vis = this
        const y = d3.scaleLinear()
        .domain([
            d3.min(vis.data, d => d.val) * 0.97, // returns 97% min height for y axis
            d3.max(vis.data, d => d.val)  // returns largest height from data
        ]) 
        .range([HEIGHT, 0])
    
    
    const x = d3.scaleBand()
        .domain(vis.data.map(d => d.name))
        .range([0, WIDTH])
        .padding(0.4) // space between bars

    const xAxisCall = d3.axisBottom(x)
    vis.xAxisGroup
        .transition().duration(500)
        .call(xAxisCall)

    const yAxisCall = d3.axisLeft(y)
    vis.yAxisGroup
        .transition().duration(500)
        .call(yAxisCall)

    // 1 DATA JOIN
    const rects = vis.svg.selectAll("rect")
        .data(vis.data)
    
    // 2 EXIT
    rects.exit()
        .transition().duration(500)
        .attr("height", 0)
        .attr("y", HEIGHT)
        .remove()

    // 3 UPDATE
    rects.transition().duration(500)
        .attr("x", d => x(d.name))
        .attr("y", d => y(d.val))
        .attr("width", x.bandwidth)
        .attr("height", d => HEIGHT - y(d.val))
    
    // 4 ENTER
    rects.enter().append("rect")
        .attr("x", d => x(d.name))
        .attr("width", x.bandwidth)
        .attr("fill", "steelblue")
        .attr("y", HEIGHT)
        .transition().duration(500)
        .attr("height", d => HEIGHT - y(d.val))
        .attr("y", d => y(d.val))
    }
}

export default D3Chart
       


/////////// NOTES BELOW /////////////
/*const temperatureData = [ 
    { "cur_depth": "121", "cur_temp": "50", "name": "Alpental", "new_snow_12": "0", "new_snow_24": "0", "new_snow_48": "2", "ts": "Thu, 07 May 2020 00:00:00 GMT", "wind_dir": "", "wind_speed": "5", "ytd": "336" },
    { "cur_depth": "", "cur_temp": "", "name": "Big Sky", "new_snow_12": "", "new_snow_24": "", "new_snow_48": "", "ts": "Mon, 04 May 2020 00:00:00 GMT", "wind_dir": "", "wind_speed": "", "ytd": "" }, 
    { "cur_depth": "", "cur_temp": "", "name": "Bridger Bowl", "new_snow_12": "", "new_snow_24": "", "new_snow_48": "", "ts": "Mon, 04 May 2020 00:00:00 GMT", "wind_dir": "", "wind_speed": "", "ytd": "" }, 
    { "cur_depth": "92", "cur_temp": "27", "name": "Jackson Hole", "new_snow_12": "", "new_snow_24": "", "new_snow_48": "", "ts": "Thu, 07 May 2020 00:00:00 GMT", "wind_dir": "", "wind_speed": "", "ytd": "358" }, 
    { "cur_depth": "95", "cur_temp": "40", "name": "Mt Bachelor", "new_snow_12": "", "new_snow_24": "0", "new_snow_48": "", "ts": "Thu, 07 May 2020 00:00:00 GMT", "wind_dir": "NE", "wind_speed": "6", "ytd": "333" }, 
    { "cur_depth": "136", "cur_temp": "39", "name": "Mt Hood", "new_snow_12": "0", "new_snow_24": "0", "new_snow_48": "0", "ts": "Thu, 07 May 2020 00:00:00 GMT", "wind_dir": "", "wind_speed": "13", "ytd": "329" }, 
    { "cur_depth": "122", "cur_temp": "32", "name": "49 Degrees North", "new_snow_12": "0", "new_snow_24": "0", "new_snow_48": "0", "ts": "Thu, 07 May 2020 00:00:00 GMT", "wind_dir": "", "wind_speed": "", "ytd": "226" }, 
    { "cur_depth": "103", "cur_temp": "36", "name": "Snowbird", "new_snow_12": "0", "new_snow_24": "0", "new_snow_48": "0", "ts": "Thu, 07 May 2020 00:00:00 GMT", "wind_dir": "WNW", "wind_speed": "34", "ytd": "545" }, 
    { "cur_depth": "128", "cur_temp": "34", "name": "Whitefish", "new_snow_12": "6", "new_snow_24": "", "new_snow_48": "", "ts": "Thu, 07 May 2020 00:00:00 GMT", "wind_dir": "SE", "wind_speed": "3", "ytd": "252" } ];

d3 scales are functions that map from an input domain to an output range

d3.select("css selector") often d3.select("body")
//returns d3 selection

d3.append("") 
returns d3 selection 

.attr("attribute", set value)*/

