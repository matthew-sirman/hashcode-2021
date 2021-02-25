from Parser import DataInput
from Parser import Intersection, Car, Street

class IntersectionSchedule:
    def __init__(self, timings):
        # List containing (street, time) pairs
        self.timings = timings
        self.total_schedule_time = sum(map(lambda x: x[1], timings))

    def find_street(self, time) -> str:
        time %= self.total_schedule_time
        total = 0
        for (s, t) in self.timings:
            if total <= time < total + t:
                return s
            total += t

        return None

    def __str__(self):
        return '[' + ', '.join(f'({str(street)}, {timing})' for street,timing in self.timings) + ']'

class Schedule(dict):
    def __init__(self, schedules = {}):
        self.__dict__ = schedules
    
    def __getitem__(self, key):
        return self.__dict__.get(key, IntersectionSchedule([]))

    def __setitem__(self, key, value):
        if isinstance(key, Intersection):
            self.__dict__[key.id] = value
        else:
            self.__dict__[key] = value

    def __repr__(self):
        return repr(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __delitem__(self, key):
        del self.__dict__[key]

    def clear(self):
        return self.__dict__.clear()

    def copy(self):
        return self.__dict__.copy()

    def has_key(self, k):
        return k in self.__dict__

    def update(self, *args, **kwargs):
        return self.__dict__.update(*args, **kwargs)

    def keys(self):
        return self.__dict__.keys()

    def values(self):
        return self.__dict__.values()

    def items(self):
        return self.__dict__.items()

    def pop(self, *args):
        return self.__dict__.pop(*args)

    def __cmp__(self, dict_):
        return self.__cmp__(self.__dict__, dict_)

    def __contains__(self, item):
        return item in self.__dict__

    def __iter__(self):
        return iter(self.__dict__)

    def __unicode__(self):
        return unicode(repr(self.__dict__))


class Solution:
    def __init__(self, data: DataInput) -> None:
        self.data = data
        # Index corresponds to the intersection
        self.schedule = self.solve()
    
    #def car_journey_time(self):
    #    for _car in self.data.cars:
    #        time = 0
    #        for _str in _car.path:
    #            time = time + _str.L
    #        if time > self.D * 0.95:
    #           _car = None

    def solve(self) -> Schedule:
        return self.solve_round_robin()

    def weighted_solve(self):
      # look at adjacent graph nodes
      schedule = Schedule()
      for _intersec in self.data.intersections:
            schedule_list = []
            total_in = 0
            for street in _intersec.streets_in:
                # find the adjacent interesection
                _id = street.B
                intersections = [adj_intersec for adj_intersect]
                int_schedule = (street, 1)
                schedule_list.append(int_schedule)
            int_schedule_obj = IntersectionSchedule(schedule_list)
            schedule[_intersec] = int_schedule_obj
      return schedule

    def solve_round_robin(self):
        # if the intersection only has one incoming, set it always to be greeen.
        schedule = Schedule()
        for _intersec in self.data.intersections:
            schedule_list = []
            
            for street in _intersec.streets_in:
                int_schedule = (street, 1)
                schedule_list.append(int_schedule)
            int_schedule_obj = IntersectionSchedule(schedule_list)
            schedule[_intersec] = int_schedule_obj
        return schedule
            

    def __str__(self):
        if not isinstance(self.schedule, Schedule):
            return ''
        result = ''
        ints = self.schedule.keys()
        count = len(ints)
        result += f'{count}\n'
        for id in ints:
            result += f'{id}\n'
            intschedule = self.schedule[id]
            timings = intschedule.timings
            result += f'{len(timings)}\n'
            for i in range(len(timings)):
                street,timing = timings[i]
                result += f'{street.name} {timing}' + '\n'
        return result.strip()
            
