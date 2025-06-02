class Graph:
    def __init__(self, edges):
        self.edges = edges


routes = {
    "Mumbai": ["Pune", "Delhi", "Goa", "Chennai"],
    "Pune": ["Mumbai", "Nashik", "Aurangabad"],
    "Delhi": ["Mumbai", "Agra", "Jaipur"],
    "Goa": ["Mumbai", "Mangalore", "Kochi"],
    "Chennai": ["Mumbai", "Bangalore", "Hyderabad"],
    "Nashik": ["Pune", "Aurangabad"],
    "Aurangabad": ["Pune", "Nashik", "Hyderabad"],
    "Agra": ["Delhi", "Jaipur"],
    "Jaipur": ["Delhi", "Agra"],
    "Mangalore": ["Goa", "Bangalore"],
    "Kochi": ["Goa", "Bangalore"],
    "Bangalore": ["Chennai", "Mangalore", "Kochi"],
    "Hyderabad": ["Chennai", "Aurangabad"],
}

graph = Graph(routes)
