import wikipediaapi
from pyvis.network import Network
import networkx as nx
import argparse

parser = argparse.ArgumentParser(description='Generate a network of wikipedia pages')
parser.add_argument('--lang', '-l', default='en', help='language code')
parser.add_argument('source', help='start page')
parser.add_argument('target', help='end page')
parser.add_argument('--depth', '-d', default=1000, type=int, help='depth of the graph')
parser.add_argument('--output', '-o', default='wikimap.html', help='output file')
args = parser.parse_args()

wiki = wikipediaapi.Wikipedia(args.lang)

source = args.source
if not wiki.page(source).exists():
    print("Source page does not exist")
    exit()
target = args.target
if not wiki.page(target).exists():
    print("Target page does not exist")
    exit()
depth = 1000

map = Network(height='95vh', width='95vw')
graph = nx.Graph()

queue = [source]
while target not in graph and graph.number_of_nodes() < depth:
    article = queue.pop(0) 
    if article not in graph:
        graph.add_node(article)
    links = wiki.page(article).links
    for title in sorted(links.keys()):
        if title not in graph:
            queue.append(title)
            graph.add_node(title)
            graph.add_edge(article, title)

if target in graph:
    print(nx.algorithms.shortest_paths.generic.shortest_path(graph, source, target))
else:
    print("Target not found! Consider increasing the depth!")
    
map.from_nx(graph)
print("generated map")
map.options = {
  "physics": {
    "barnesHut": {
      "gravitationalConstant": -30000,
      "centralGravity": 0,
      "springConstant": 0.025
    },
    "minVelocity": 0.75
  }
}
map.show(args.output)
try:
    wiki.__del__()
except TypeError:
    pass