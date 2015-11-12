import math
from random import random, randint
from population import Population
from tour import Tour


class GA:
    _mutation_rate = 0.015
    _tournament_size = 5
    _elitism = True

    def envolve_population(self, pop, num_cities):
        new_population = Population(pop.population_size(), False)

        elitism_offset = 0
        if self._elitism:
            new_population.save_tour(0, pop.get_fittest())
            elitism_offset = 1

        for i in xrange(elitism_offset, new_population.population_size()):
            parent1 = self.tournament_selection(pop)
            parent2 = self.tournament_selection(pop)

            # Crossover parents
            child = self.crossover(parent1, parent2, num_cities)

            new_population.save_tour(i, child)

        # mutate
        for i in xrange(elitism_offset, new_population.population_size()):
            self.mutate(new_population.get_tour(i))

        return new_population


    def crossover(self, parent1, parent2, num_cities):
        child = Tour(num_cities)

        start_pos = int(random() * parent1.tour_size())
        end_pos = int(random() * parent1.tour_size())

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
            if random() < self._mutation_rate:
                tour_pos2 = randint(0, tour.tour_size() - 1)  # int(random() * tour.tour_size())

                city1 = tour.get_city(tour_pos1)
                city2 = tour.get_city(tour_pos2)

                tour.set_city(tour_pos2, city1)
                tour.set_city(tour_pos1, city2)


    def tournament_selection(self, pop):
        tournament = Population(self._tournament_size, False)

        for i in xrange(self._tournament_size):
            random_id = randint(0, pop.population_size() - 1)  # int(random() * pop.population_size())
            tournament.save_tour(i, pop.get_tour(random_id))

        return tournament.get_fittest()
