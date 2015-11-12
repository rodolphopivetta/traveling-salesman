import math
from random import random, randint
import matplotlib.pyplot as plt

from tour import Tour


class SimulatedAnnealing:
    _temp = 1000
    _cooling_rate = 0.0003
    x_graph = []
    y_graph = []
    ini = None
    end = None

    def __init__(self, window, cities_list):
        self.ini = window.figure.add_subplot(211)
        self.end = window.figure.add_subplot(212)

        self._cities_list = cities_list

        current_solution = Tour()
        current_solution.generate(self._cities_list)
        self.plt_reload(211, current_solution.get_tour(), self._temp)

        print 'Initial distance: ', current_solution.get_distance()
        self.x_graph.append(0)
        self.y_graph.append(current_solution.get_distance())

        best = Tour(current_solution)

        while self._temp > 1:
            new_solution = Tour(current_solution)

            # swap cities
            self.swap_solution(new_solution)

            # reverse slide of list
            self.reverse_solution(new_solution)

            # translate slice of list
            self.translate_solution(new_solution)

            current_energy = current_solution.get_distance()
            neighbour_energy = new_solution.get_distance()

            if self.acceptance_probability(current_energy, neighbour_energy, self._temp) > random():
                current_solution = new_solution

            if current_solution.get_distance() < best.get_distance():
                best = current_solution
                self.plt_reload(212, new_solution.get_tour(), self._temp)
                self.x_graph.append(self.x_graph[-1] + 1)
                self.y_graph.append(new_solution.get_distance())

            self._temp *= (1 - self._cooling_rate)

        print 'Final distance: ', best.get_distance()
        print 'Tour: ', best
        self.plt_reload(212, best.get_tour(), self._temp)
        self.x_graph.append(self.x_graph[-1] + 1)
        self.y_graph.append(best.get_distance())


    def swap_solution(self, new_solution):
        tour_pos1 = int(new_solution.tour_size() * random())
        tour_pos2 = int(new_solution.tour_size() * random())

        city_swap1 = new_solution.get_city(tour_pos1)
        city_swap2 = new_solution.get_city(tour_pos2)

        new_solution.set_city(tour_pos1, city_swap2)
        new_solution.set_city(tour_pos2, city_swap1)


    def reverse_solution(self, new_solution):
        tour_pos1 = 0
        tour_pos2 = 0
        while tour_pos1 >= tour_pos2:
            tour_pos1 = int(new_solution.tour_size() * random())
            tour_pos2 = int(new_solution.tour_size() * random())

        aux_list = new_solution.get_tour()
        aux_list[tour_pos1:tour_pos2] = list(reversed(aux_list[tour_pos1:tour_pos2]))
        new_solution.set_tour(aux_list)


    def translate_solution(self, new_solution):
        start = 0
        end = 0
        while start > end:
            start = int(new_solution.tour_size() * random())
            end = int(new_solution.tour_size() * random())
        size = start
        while size >= start and size <= end:
            size = randint(0, new_solution.tour_size())

        aux_list = new_solution.get_tour()
        for i in xrange(size):
            for j in xrange(start, end + 1):
                aux_list[j + 1], aux_list[j] = aux_list[j], aux_list[j + 1]
        new_solution.set_tour(aux_list)


    def acceptance_probability(self, energy, new_energy, temperature):
        if new_energy < energy:
            return 1.0
        return math.exp((energy - new_energy) / temperature)


    def plt_reload(self, f, cities, temp=''):
        x_list = []
        y_list = []
        for c in cities:
            x_list.append(c.getX())
            y_list.append(c.getY())

        plt.subplot(f)
        plt.cla()
        self.ini.set_title('Temperature: ' + str(temp))
        plt.fill(x_list, y_list, edgecolor='b', fill=False)
        plt.plot(x_list, y_list, 'bo')
        plt.grid(True)
        plt.pause(0.001)
