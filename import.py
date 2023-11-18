import json 
import xml.etree.ElementTree as ET

#Handles the distance and time calculations for the ending JSON file
from distance import distance
from timeElasped import time

#Define 'Way' object
class Way:
    def __init__(self, way_id, nodes):
        self.way_id = way_id
        self.nodes = nodes

#Define 'Node' object
class Node:
    def __init__(self, node_id, lat, lon):
        self.node_id = node_id
        self.lat = lat
        self.lon = lon

#Define 'Bot' object
class Bot:
    def __init__(self, location, capacity):
        self.location = location
        self.capacity = capacity

#Define 'Package' object
class Package:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

#Specify file path
file_path = 'test_data/TA1.json'

#Open the file in read mode
with open(file_path, 'r') as file:
    #Load JSON file
    data = json.load(file)

#Access the 'bots' list
bots_list = data['bots']

#Access the 'packages' list
packages_list = data['packages']

#Create instances of 'Bot' and 'Package' classes
bots = [Bot(bot['location'], bot['capacity']) for bot in bots_list]
packages = [Package(package['source'], package['destination']) for package in packages_list]

# Specify the path to XML file
xml_file_path = 'test_data/TA1.xml'

# Parse the XML file
tree = ET.parse(xml_file_path)
root = tree.getroot()

# Create lists to store Node and Way objects
nodes = []
ways = []

# Iterate over elements in the XML tree
for element in root:
    if element.tag == 'node':
        # Extract node attributes
        node_id = int(element.attrib['id'])
        lat = float(element.find('lat').text)
        lon = float(element.find('lon').text)

        # Create Node object and add to the list
        nodes.append(Node(node_id, lat, lon))

    elif element.tag == 'way':
        # Extract way attributes
        way_id = int(element.attrib['id'])
        
        # Extract node references within the way
        node_references = [int(node.text) for node in element.findall('node')]

        # Create Way object and add to the list
        ways.append(Way(way_id, node_references))

#rahat
sources ={}

destination = {}

for package in packages:
    destination[package.destination]=package
    sources[package.source]=package

graph ={}

for way in ways:
    if (graph.get(way.nodes[0])):
        graph[way.nodes[0]].append(way.nodes[1])
    else:
        graph[way.nodes[0]]=[way.nodes[1]]
    if (graph.get(way.nodes[1])):
        graph[way.nodes[1]].append(way.nodes[0])
    else:
        graph[way.nodes[1]]=[way.nodes[0]]
nodeMap ={}

for node in nodes:
    nodeMap[node.node_id]= node


superBot = bots[0]



superBot.capacity = len(packages)

print(superBot.location)

visited = set()
path =[]

def dfs(graph, start):
    visited.add(start)
    path.append(start)
    print(path)
    for next_node in graph.get(start, []):
        if next_node not in visited:
            dfs(graph, next_node)


# Initialize time variable
time = len(destination)*2

# Call DFS function
dfs(graph, superBot.location)

# Calculate time taken to traverse each node
for i in range(len(path) - 1):
    node1 = nodeMap[path[i]]
    node2 = nodeMap[path[i + 1]]
    dist = distance(node1.lat, node1.lon, node2.lat, node2.lon)
    time += dist / 40

print(f"Path: {path}")
print(f"Time: {time*2}")