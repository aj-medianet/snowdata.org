import React from 'react';
import ReactDom from 'react-dom';
import { render, cleanup } from '@testing-library/react';
import '@testing-library/jest-dom';
import renderer from 'react-test-renderer';
import MainYTDChart from './../components/charts/MainYTDChart';
import MainDepthChart from './../components/charts/MainDepthChart';
import MainWindChart from './../components/charts/MainWindChart';
import MainTempChart from './../components/charts/MainTempChart';
import AreaCombo from './../components/charts/AreaCombo';
import AreaNewSnow from './../components/charts/AreaNewSnow';

const fakeData = [
    {name: "Alpental", cur_depth: "100", ytd: "300", cur_temp: "30", wind_speed: "5", new_snow_12: "1", new_snow_24: "0", new_snow_48: ""}
]
const fakeMonthlyData = [
    {avg_temp:"20",id:0,month:"5",ski_area_name:"Alpental",snow_depth:"10",total_new_snow:"10",year:"2020",ytd:"100"}
]

afterEach(cleanup);

it("MainYTDChart renders without crashing", () => {
    const div = document.createElement("div");
    ReactDom.render(<MainYTDChart data={fakeData}></MainYTDChart>, div)
})

it("MainDepthChart renders without crashing", () => {
    const div = document.createElement("div");
    ReactDom.render(<MainDepthChart data={fakeData}></MainDepthChart>, div)
})

it("MainWindChart renders without crashing", () => {
    const div = document.createElement("div");
    ReactDom.render(<MainWindChart data={fakeData}></MainWindChart>, div)
})

it("MainTempChart renders without crashing", () => {
    const div = document.createElement("div");
    ReactDom.render(<MainTempChart data={fakeData}></MainTempChart>, div)
})

it("AreaNewSnow renders without crashing", () => {
    const div = document.createElement("div");
    ReactDom.render(<AreaNewSnow data={fakeData}></AreaNewSnow>, div)
})

it("AreaCombo renders without crashing", () => {
    const div = document.createElement("div");
    ReactDom.render(<AreaCombo data_monthly={fakeMonthlyData}></AreaCombo>, div)
})

//TODO
/*
it("renders MainYTD correctly", ()=> {
    const { getByTestId } = render(<MainYTDChart data={fakeData}></MainYTDChart>)
    expect(getByTestId('MainYTDChart')).toHaveBeenCalledTimes(1)
})*/