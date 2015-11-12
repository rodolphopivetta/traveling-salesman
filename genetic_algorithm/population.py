from tour import Tour


class Population:
    _tours = []

    def __init__(self, population_size, initialise, cities=None):
        self._tours = [None] * population_size
        if initialise:
            for i in xrange(population_size):
                new_tour = Tour()
                new_tour.generate(cities)
                self.save_tour(i, new_tour)


    def save_tour(self, index, tour):
        self._tours[index] = tour


    def get_tour(self, index):
        return self._tours[index]


    def get_fittest(self):
        fittest = self._tours[0]
        for i in xrange(self.population_size()):
            if fittest.get_fitness() <= self.get_tour(i).get_fitness():
                fittest = self.get_tour(i)

        return fittest


    def population_size(self):
        return len(self._tours)
