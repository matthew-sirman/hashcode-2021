from Solution import Solution


class Metric:
    def __init__(self, sol: Solution) -> None:
        # Solution has list of intersection schedules
        # Schedule is list of pairs of name, time
        self.sol = sol
        self.data = sol.data

    def calculate(self) -> int:
        return self.simulate()

    def simulate(self):
        # Map of current streets to cars waiting at them
        intersection_cars = dict()
        # Map of streets to cars and positions along (empty initially)
        street_cars = dict()

        for s in self.data.streets:
            street_cars[s] = []
            intersection_cars[s] = []

        for c in self.data.cars:
            k = c.path.pop(0)
            intersection_cars[k].append(c)

        score = 0

        for step in range(self.data.D):
            # Update the light at each intersection
            print("SCHEDULES")
            for i in range(self.data.I):
                light = self.sol.schedule[i].find_street(step)
                print(light.name)
                if light is not None:
                    waiting_cars = intersection_cars[light]
                    if len(waiting_cars) > 0:
                        # This pops from the dictionary as well - the list is a ref
                        car = waiting_cars.pop(0)
                        # Move the car onto the next street on its path
                        street_cars[car.path[0]].append((car, 0))

            # Look at each street
            for s in street_cars:
                for i, (c, t) in enumerate(street_cars[s]):
                    # Move the car along the street
                    street_cars[s][i] = (c, t+1)
                    if t + 1 == s.L:
                        new_s = c.path.pop(0)
                        # Reached the end
                        if len(c.path) == 0:
                            score += self.data.F + self.data.D - step - 1
                        else:
                            intersection_cars[new_s].append(c)

                        # Mark for removal from this street
                        street_cars[s][i] = None

                street_cars[s] = list(filter(lambda x: x is not None, street_cars[s]))

        return score
