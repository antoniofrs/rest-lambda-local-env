
import json
from rest.model.route import HttpMethod, Route

route_list=[]

def add_route(route, root_path):
    path = root_path + route["path"]
    for http_method in HttpMethod:
        method_str = http_method.value
        if method_str in route:
            route_list.append(Route(http_method, path, route[method_str]))
    if "route" in route:
        add_route(route["route"],path)
        

def find_function(input_method: str, input_path: str) -> str:
    for route in route_list:
        if route.http_method == input_method and route.path == input_path:
            return route.function
    return "Funzione non trovata"


def init_config():
    with open("config.json", 'r') as file:
            config = json.load(file)
            add_route(config["route"], "")
    return config["port"]