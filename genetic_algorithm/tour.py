import random


class Tour:
    _tour = []
    _fitness = 0
    _distance = 0

    def __init__(self, num_cities=0, tour=None):
        if num_cities:
            self._tour = [None] * num_cities
        if tour:
            self._tour = list(tour._tour)
            self._fitness = tour._fitness
            self._distance = tour._distance


    def __str__(self):
        gene_string = ''
        for i in xrange(len(self._tour)):
            gene_string += str(self.get_city(i))
            if i < len(self._tour) - 1:
                gene_string += ' -> '
        return gene_string


    def get_tour(self):
        return self._tour


    def set_tour(self, new_list):
        self._tour = new_list


    def generate(self, cities_list):
        self._tour = cities_list
        random.shuffle(self._tour)


    def get_city(self, index):
        return self._tour[index]


    def set_city(self, index, city):
        self._tour[index] = city
        self._fitness = 0
        self._distance = 0


    def tour_size(self):
        return len(self._tour)


    def get_distance(self):
        if self._distance == 0:
            tour_distance = 0
            for i in xrange(len(self._tour)):
                from_city = self.get_city(i)
                destination_city = None
                if i + 1 < self.tour_size():
                    destination_city = self.get_city(i + 1)
                else:
                    destination_city = self.get_city(0)
                tour_distance += from_city.distance_to(destination_city)
            self._distance = tour_distance
        return self._distance


    def get_fitness(self):
        if self._fitness == 0:
            fitness = 1 / float(self.get_distance())
        return fitness


    def contains_city(self, city):
        return True if city in self._tour else False
