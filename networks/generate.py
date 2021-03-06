#!/usr/bin/env python3

# Description:  Create random simple graphs of a given dimension
# Author:       Eric Leung
# Date:         2016 Jun 22nd
# Python:       3.5.1

import numpy as np  # 1.11.0


def simple(size, weight=1):
    """
    Generate a simple graph, specifically an undirected network, with neither
    self-edges nor multiedges

    Arguments:
    size:       number of nodes in the graph
    weight:     indicate weighted simple network (default = 1)
    """
    graph = np.random.randint(weight+1, size=(size, size))
    return(np.tril(graph) + np.tril(graph, -1).T - np.diag(graph.diagonal()))

def digraph(size, weight=1):
    """
    Generate a directed simple graph

    Arguments:
    size:       number of nodes in the graph
    weight:     indicate weights of network (default = 1)
    """
    graph = np.random.randint(weight+1, size=(size, size))
    return(graph - np.diag(graph.diagonal()))
