#!/usr/bin/env python3
"""Dijkstra's algorithm usage"""


from pythonds3.graphs import Graph
import toml


def read_toml(filename: str) -> Graph:
    """Read TOML config file"""
    n, g =  dict(), Graph()
    myRoute = toml.load(filename)
    for i in myRoute['routers']: n[i['address']] = i['name']
    for i in myRoute['routers']:
        for j in i['neighbors']: g.add_edge(i['name'], n[j['address']], j['cost'])
    return g

def find_path(g: Graph, start: str) -> None:
    """Use Dijkstra's algorithm to find the shortest path from *start* to other vertices"""
    print(g.dijkstra(g.get_vertex(start)))


def main():
    graph = read_toml("data/exercises/dijkstra/network.toml")
    find_path(graph, 'v')


if __name__ == "__main__":
    main()
