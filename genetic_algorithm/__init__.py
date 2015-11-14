import random

from population import Population
from tour import Tour

import matplotlib.pyplot as plt

class GeneticAlgorithm:
    _mutation_rate = 0.015
    _tournament_size = 5
    _cities_list = []
    _elitism = True
    x_graph = []
    y_graph = []
    ini = None
    end = None
    best_distance = 0


    def __init__(self, window, cities_list):
        self.ini = window.figure.add_subplot(211)
        self.end = window.figure.add_subplot(212)

        self._cities_list = cities_list
        random.seed()

        pop = Population(1000, True, self._cities_list)
        self.plt_reload(211, self._cities_list, 'Starting')
        print 'Initial distance: %.4f' % (pop.get_fittest().get_distance())
        self.x_graph.append(0)
        self.y_graph.append(pop.get_fittest().get_distance())

        for j in xrange(100):
            new_population = Population(pop.population_size(), False)

            elitism_offset = 0
            if self._elitism:
                new_population.save_tour(0, pop.get_fittest())
                elitism_offset = 1

            for i in xrange(elitism_offset, new_population.population_size()):
                parent1 = self.tournament_selection(pop)
                parent2 = self.tournament_selection(pop)

                # Crossover parents
                child = self.crossover(parent1, parent2)

                new_population.save_tour(i, child)

            # mutate
            for i in xrange(elitism_offset, new_population.population_size()):
                self.mutate(new_population.get_tour(i))
            pop = new_population
            self.plt_reload(212, pop.get_fittest().get_tour(), 'Iteration: ' + str(j + 1))
            self.x_graph.append(self.x_graph[-1] + 1)
            self.y_graph.append(pop.get_fittest().get_distance())

        self.plt_reload(212, pop.get_fittest().get_tour(), 'Iteration: ' + str(j + 1))
        self.x_graph.append(self.x_graph[-1] + 1)
        self.y_graph.append(pop.get_fittest().get_distance())

        print 'Final distance: %.4f' % (pop.get_fittest().get_distance())
        print 'Solution:'
        print pop.get_fittest()
        self.best_distance = pop.get_fittest().get_distance()


    def crossover(self, parent1, parent2):
        child = Tour(len(self._cities_list))

        start_pos = int(random.random() * parent1.tour_size())
        end_pos = int(random.random() * parent1.tour_size())

        for i in xrange(child.tour_size()):
            if start_pos < end_pos and i > start_pos and i < end_pos:
                child.set_city(i, parent1.get_city(i))
            elif start_pos > end_pos:
                if not (i < start_pos and i > end_pos):
                    child.set_city(i, parent1.get_city(i))

        for i in xrange(parent2.tour_size()):
            if not child.contains_city(parent2.get_city(i)):
                for j in xrange(child.tour_size()):
                    if not child.get_city(j):
                        child.set_city(j, parent2.get_city(i))
                        break

        return child


    def mutate(self, tour):
        for tour_pos1 in xrange(tour.tour_size()):
            if random.random() < self._mutation_rate:
                tour_pos2 = int(random.random() * tour.tour_size())

                city1 = tour.get_city(tour_pos1)
                city2 = tour.get_city(tour_pos2)

                tour.set_city(tour_pos2, city1)
                tour.set_city(tour_pos1, city2)


    def tournament_selection(self, pop):
        tournament = Population(self._tournament_size, False)

        for i in xrange(self._tournament_size):
            random_id = int(random.random() * pop.population_size())
            tournament.save_tour(i, pop.get_tour(random_id))

        return tournament.get_fittest()

    def plt_reload(self, f, cities, msg):
        x_list = []
        y_list = []
        for c in cities:
            x_list.append(c.getX())
            y_list.append(c.getY())

        plt.subplot(f)
        plt.cla()
        self.ini.set_title(msg)
        plt.fill(x_list, y_list, edgecolor='b', fill=False)
        plt.plot(x_list, y_list, 'bo')
        plt.grid(True)
        plt.pause(0.001)
