# Traveling Salesman solved by Simulated Annealing and Genetic Algorithm

This repository contains a implementation of two algorithms to solve the Traveling Salesman problem:

* Simulated Annealing
* Genetic Algorithm

This work compares the implementations, so the ```tsp.py``` file executes the random generation of cities and uses this collection to send to the algorithms.

## Dependencies

To run this code, you need to install the matplotlib and argparse.

```
sudo apt-get install python-matplotlib
sudo pip install argparse
```

## Execution

To execute, call

``` python tsp.py ```

This will show three graphs, first with the initial and final tours to Simulated Annealing and the second for Genetic Algoritm. The third graph shows the comparision of the executions.

To set the number of cities, use ```--numcities``` param. By default, this will execute [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] cities.

To run to test comparision, use ```--numtests``` param.

-------

This repository have too a report (in Brazilian Portuguese) of this implementations and the results of observations.
