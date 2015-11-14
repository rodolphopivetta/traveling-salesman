import matplotlib.pyplot as plt

from simulated_annealing import SimulatedAnnealing
from genetic_algorithm import GeneticAlgorithm

from city import City


class ManageGraph:
    figure = None

    def __init__(self):
        self.figure = plt.figure()


if __name__ == "__main__":
    cities_list = []

    for i in xrange(10):
        city = City()
        cities_list.append(city)

    simulated_window = ManageGraph()
    simulated_annealing = SimulatedAnnealing(simulated_window, cities_list)

    genetic_window = ManageGraph()
    genetic_algorithm = GeneticAlgorithm(genetic_window, cities_list)

    compare_window = ManageGraph()
    plt.plot(simulated_annealing.x_graph, simulated_annealing.y_graph)
    plt.plot(genetic_algorithm.x_graph, genetic_algorithm.y_graph)
    plt.legend(['Simulated Annealing', 'Genetic Algorhtm'], loc='upper right')
    plt.text(simulated_annealing.x_graph[-1], simulated_annealing.y_graph[-1] + 5,
        "%.4f" % simulated_annealing.best_distance)
    plt.text(genetic_algorithm.x_graph[-1], genetic_algorithm.y_graph[-1] + 5,
        "%.4f" % genetic_algorithm.best_distance)
    plt.xlabel('Iteration')
    plt.ylabel('Distance')
    plt.grid(True)
    plt.show()
