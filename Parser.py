class Intersection:
    def __init__(self, id, streets_in, streets_out):
        self.id = id
        self.streets_in = streets_in
        self.streets_out = streets_out
    
    def add_in(self, street):
        if not street in self.streets_in:
            self.streets_in.append(street)
    def add_out(self, street):
        if not street in self.streets_out:
            self.streets_out.append(street)

    def __eq__(self, other):
        if isinstance(other, Intersection):
            return self.id == other.id
        return False

class Car:
    def __init__(self, path):
        self.path = path

    def __str__(self):
        return ' '.join(str(street) for street in self.path)

class Street:
    def __init__(self, B, E, L, name):
        self.B = B
        self.E = E
        self.L = L
        self.name = name

    def __eq__(self, other):
        if isinstance(other, Street):
            return self.name == other.name
        return False

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return self.name
        #return f'(B = {self.B}, E = {self.E}, L = {self.L}, {self.name})'

class DataInput:
    def __init__(self, D, I, F, streets, cars) -> None:
        self.D = D
        self.I = I
        self.F = F
        self.streets = streets
        self.cars = cars

        intersection_lookup = {}
        for street in streets:
            for id in (street.B, street.E):
                if not id in intersection_lookup:
                    intersection = Intersection(id, [], [])
                    intersection_lookup[id] = intersection
                intersection = intersection_lookup[id]
                if id == street.B:
                    intersection.add_in(street)
                else:
                    intersection.add_out(street)
        self.intersections = intersection_lookup.values()

    
    def __str__(self):
        return f'D = {self.D} I = {self.I} F = {self.F}\n\n' + 'Streets:\n' + '\n'.join(str(street) for street in self.streets) + '\n\nCars:\n' + '\n'.join(str(car) for car in self.cars)


class Parser:
    def __init__(self, input_file: str) -> None:
        self.__in_file = input_file
        lines = []
        with open(input_file, "r") as in_file:
            for line in in_file:
                if line != '':
                    lines.append(line)
        self.lines = [line.strip() for line in lines]

    def create_input(self) -> DataInput:
        count = 0
        D,I,S,V,F = tuple(map(lambda x: int(x), self.lines[count].split(' ')))
        count += 1
        streets = []
        street_lookup = dict()
        for i in range(S):
            B,E,name,L = tuple(self.lines[count].split(' '))
            B = int(B)
            E = int(E)
            L = int(L)
            new_s = Street(B, E, L, name)
            streets.append(new_s)
            street_lookup[name] = new_s
            count += 1
        cars = []
        for i in range(V):
            data = self.lines[count].split(' ')
            P = int(data[0])
            street_names = data[1:]
            path = []
            for street_name in street_names:
                path.append(street_lookup[street_name])
                # for street in streets:
                #     if street.name == street_name:
                #         path.append(street)
                #         break
            cars.append(Car(path))
            count += 1
        return DataInput(D, I, F, streets, cars)

