import requests
import sys

def get_data(query,params=None):
	if params is None:
		url = 'http://realtime.mbta.com/developer/api/v2/' + query + '?api_key=wX9NwuHnZU2ToO7GmGR9uw&format=json'
	else:
		url = 'http://realtime.mbta.com/developer/api/v2/' + query + '?api_key=wX9NwuHnZU2ToO7GmGR9uw&format=json&' + params
	r = requests.get(url)
	return r.json()

def get_routes(mode_name):
	response = get_data("routes", params = None)
	bus_routes = []
	for route_type in response["mode"]:
		if route_type["mode_name"] ==  mode_name:
			bus_routes = route_type["route"]
			break
	return bus_routes

## write a method to store each routes schedule for that day in database
## also make sure that method skip, hidden routes

def get_schedule(route):
	params = 'route='+route
	response = get_data("schedulebyroute",params)
	return response

def prediction(stop_id):
	params = 'stop=' + stop_id
	response = get_data("predictionsbystop",params)
	return response

def store_trip():
	routes = get_routes("Bus")
	file = open('json_file', 'w')
	bus_trips = []
	for route in routes:
		if 'hidden' not in route.keys():
			schedule = get_schedule(route["route_id"])
			for direction in schedule["direction"]:
				#print direction["trip"]
				bus_trips.append(direction["trip"])
	print bus_trips
	file.write(str(bus_trips))
	file.close

store_trip()    