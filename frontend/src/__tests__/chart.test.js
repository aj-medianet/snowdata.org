import React from 'react';
import ReactDom from 'react-dom';
import { render, cleanup } from '@testing-library/react';
import { extend } from '@testing-library/jest-dom'

import renderer from 'react-test-renderer'

import MainYTDChart from './../components/charts/MainYTDChart';
import MainDepthChart from './../components/charts/MainDepthChart';
import MainWindChart from './../components/charts/MainWindChart';
import MainTempChart from './../components/charts/MainTempChart';

const fakeData = [
    {name: "Alpental", cur_depth: "100", ytd: "300", cur_temp: "30", wind_speed: "5"}
]

afterEach(cleanup);

it("MainYTDChart renders without crashing", ()=> {
    const div = document.createElement("div");
    ReactDom.render(<MainYTDChart data={fakeData}></MainYTDChart>, div)
})

it("MainDepthChart renders without crashing", ()=> {
    const div = document.createElement("div");
    ReactDom.render(<MainDepthChart data={fakeData}></MainDepthChart>, div)
})

it("MainWindChart renders without crashing", ()=> {
    const div = document.createElement("div");
    ReactDom.render(<MainWindChart data={fakeData}></MainWindChart>, div)
})

it("MainTempChart renders without crashing", ()=> {
    const div = document.createElement("div");
    ReactDom.render(<MainTempChart data={fakeData}></MainTempChart>, div)
})

//TODO
/*it("renders MainYTD correctly", ()=> {
    render(<MainYTDChart data=""></MainYTDChart>)
})*/