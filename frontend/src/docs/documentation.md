
Access ski areas snow and weather data directly from the source. 
Users get 20 API calls per day for free and our dataset is updated every 20 minutes.
Create an account to receive an API key.



### Get all ski area data
***
Description: 

You can get all of the current ski area data from our dataset with a GET request API call. 

API call: 

http://api.snowdata.org/get-all-data/{api_key}



### Get a single ski area's data
***
Description: 

You can get a single ski areas current data using a POST request that includes the ski area name and your api key.

API call: 

http://api.snowdata.org/get-ski-area

POST request body:
```
{
	"skiareaname" : "{ski_area_name}",
	"api_key" : "{api_key}"
}
```


### Get all monthly data 
***
Description:

You can get all monthly data with one GET request API call.

API call:

https://api.snowdata.org/get-all-monthly-data/{api_key}


### Get monthly data for a ski area
***
Description:

You can get all of the monthly data for one ski area with one POST request API call.

API call:

https://api.snowdata.org/get-ski-area-monthly-data

POST request body:
```
{
	"skiareaname" : "{ski_area_name}",
	"api_key" : "{api_key}"
}
```

### Get one months data for a ski area
***
Description:

You can get just one month of data for a ski area with a POST request API call.

API call:

https://api.snowdata.org/get-ski-area-month-year

POST request body:
```
{
	"skiareaname" : "{ski_area_name}",
	"api_key" : "{api_key}",
	"month" : "{month}",
	"year" : "{year}"
}
```

Where month is an integer, 1 being January and 12 being December. Year is full 4 digit year.