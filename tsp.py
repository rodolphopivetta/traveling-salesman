import matplotlib.pyplot as plt

from simulated_annealing import SimulatedAnnealing
from genetic_algorithm import GeneticAlgorithm

from city import City

import argparse


class ManageGraph:
    figure = None

    def __init__(self):
        self.figure = plt.figure()


if __name__ == "__main__":
    cities_list = []
    qnt_to_test = 1
    min_simulated = []
    simulated_avg = []
    max_simulated = []
    min_genetic = []
    genetic_avg = []
    max_genetic = []
    show_window = False
    num_cities = range(10, 81, 10)

    parser = argparse.ArgumentParser(description='Traveling Salesman by Simulated Annealing and Genetic Algorithm')
    parser.add_argument('--numcities', type=int, default=0, help='Total number of cities')
    parser.add_argument('--numtests', type=int, default=1, help='Number of tests')
    args, unknown = parser.parse_known_args()

    if args.numcities:
        num_cities = [args.numcities]
    else:
        if args.numtests > 1:
            num_cities = range(10, 101, 10)
        else:
            num_cities = [10]

    for q_cities in num_cities:
        for i in xrange(q_cities):
            city = City()
            cities_list.append(city)

        if args.numtests == 1:
            show_window = True
        print '----------- SIMULATED ANNEALING WITH %d CITIES -----------' % q_cities
        simulated_annealing_s = []
        for i in xrange(args.numtests):
            print 'Test ', i + 1
            if show_window:
                simulated_window = ManageGraph()
            else:
                simulated_window = None
            simulated_annealing_s.append(SimulatedAnnealing(simulated_window, cities_list, show_window=show_window))

        min_simulated.append(min(i.get_best_distance() for i in simulated_annealing_s))
        simulated_avg.append(sum(sa_best.get_best_distance() for sa_best in simulated_annealing_s) / float(len(simulated_annealing_s)))
        max_simulated.append(max(i.get_best_distance() for i in simulated_annealing_s))

        print '----------- GENETIC ALGORITHM WITH %d CITIES -----------' % q_cities
        genetic_algorithm_s = []
        for i in xrange(args.numtests):
            print 'Test ', i + 1
            if show_window:
                genetic_window = ManageGraph()
            else:
                genetic_window = None
            genetic_algorithm_s.append(GeneticAlgorithm(genetic_window, cities_list, show_window=show_window))

        min_genetic.append(min(i.get_best_distance() for i in genetic_algorithm_s))
        genetic_avg.append(sum(ag_best.get_best_distance() for ag_best in genetic_algorithm_s) / float(len(genetic_algorithm_s)))
        max_genetic.append(max(i.get_best_distance() for i in genetic_algorithm_s))

    if args.numtests == 1:
        compare_window = ManageGraph()
        plt.plot(simulated_annealing_s[0].x_graph, simulated_annealing_s[0].y_graph)
        plt.plot(genetic_algorithm_s[0].x_graph, genetic_algorithm_s[0].y_graph)
        plt.legend(['Simulated Annealing', 'Genetic Algorhtm'], loc='upper right')
        plt.text(simulated_annealing_s[0].x_graph[-1], simulated_annealing_s[0].y_graph[-1] + 5,
            "%.4f" % simulated_annealing_s[0].best_distance)
        plt.text(genetic_algorithm_s[0].x_graph[-1], genetic_algorithm_s[0].y_graph[-1] + 5,
            "%.4f" % genetic_algorithm_s[0].best_distance)
        plt.xlabel('Iteration')
        plt.ylabel('Distance')
        plt.grid(True)
        plt.show()
    else:
        print 'Min Simulated Annealing', min_simulated
        print 'Simulated Annealing', simulated_avg
        print 'Max Simulated Annealing', max_simulated

        print 'Min Genetic Algorithm', min_genetic
        print 'Genetic Algorithm', genetic_avg
        print 'Max Genetic Algorithm', max_genetic

        compare_distances = ManageGraph()
        plt.axis([0, max(num_cities) + 10, 0, max(max(simulated_avg), max(genetic_avg)) + 1000])

        l1 = plt.plot([0] + num_cities, [0] + min_simulated, '--o')
        plt.setp(l1, color='#FA8072', linewidth=2.0)

        plt.plot([0] + num_cities, [0] + simulated_avg, '-or')

        l2 = plt.plot([0] + num_cities, [0] + max_simulated, '--o')
        plt.setp(l2, color='#B22222', linewidth=2.0)

        l3 = plt.plot([0] + num_cities, [0] + min_genetic, '--o')
        plt.setp(l3, color='#4169E1', linewidth=2.0)

        plt.plot([0] + num_cities, [0] + genetic_avg, '-ob')

        l4 = plt.plot([0] + num_cities, [0] + max_genetic, '--ok')
        plt.setp(l4, color='#191970', linewidth=2.0)

        plt.legend([
            'Min Simulated Annealing',
            'Simulated Annealing',
            'Max Simulated Annealing',
            'Min Genetic Algorithm',
            'Genetic Algorhtm',
            'Max Genetic Algorithm'], loc='upper left')
        plt.xlabel('Number of Cities')
        plt.ylabel('Distance')
        plt.grid(True)
        plt.show()
