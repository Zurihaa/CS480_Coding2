import sys
import csv

class CSP:
    def __init__(self, initial, no_of_park):
        self.initial = initial
        self.no_of_park = no_of_park
        self.load_data()

    def load_data(self):
        driving = {}
        with open("driving2.csv") as file:
            csvreader = csv.reader(file)
            states = next(csvreader)[1:]
            for row in csvreader:
                state = row[0]
                driving[state] = {}
                for i, distance in enumerate(row[1:]):
                    driving[state][states[i]] = int(distance)

        with open("parks.csv") as file:
            csvreader = csv.reader(file)
            states = next(csvreader)[1:]
            no_parks = next(csvreader)[1:]
            parks = {states[i]: int(no_parks[i]) for i in range(len(states))}

        state_in_zones = {}

        with open("zones.csv") as file:
            csvreader = csv.reader(file)
            states = next(csvreader)[1:]
            zone_num = next(csvreader)[1:]
            zones = {states[i]: int(zone_num[i]) for i in range(len(states))}

            for state, zone in zones.items():
                if zone not in state_in_zones:
                    state_in_zones[zone] = []
                state_in_zones[zone].append(state)

            zone_state = {i: sorted(j) for i, j in sorted(state_in_zones.items())}
        
        mapping = sorted(state_in_zones.items())
        
        self.driving, self.parks, self.zones, self.zone_map = driving, parks, zone_state, mapping

    def is_complete(self, assignment, park_visited):
        last_state = list(assignment.keys())[-1]
        return park_visited >= self.no_of_park and last_state in self.zones[12]

    def select_unassigned_variable(self, assignment):
        assigned_zones = [self.zone_map[state] for state in assignment if state in self.zone_map]
        unassigned_zones = [zone for zone in self.zones if zone not in assigned_zones]
        return unassigned_zones[0] if unassigned_zones else None

    def order_domain_values(self, var, assignment):
        prev_state = list(assignment.keys())[-1]
        possible_move = [(state, driving) for state, driving in self.driving[prev_state].items() if state not in assignment]
        return possible_move

    def is_consistent(self, value, assignment):
        _, distance = value        
        return  distance != -1

    def inference(self, var, assignment):
        prev_zone = var
        if prev_zone in self.zones:
              for state in self.zones[prev_zone]:
                    if state not in assignment:
                          return []
        return None

def backtracking_search(csp):
    initial_park = csp.parks[csp.initial]
    solution = backtracking(csp, {csp.initial: initial_park}, initial_park)
    return solution

def backtracking(csp, assignment, park_visited):
    if csp.is_complete(assignment, park_visited):
        return assignment
    
    var = csp.select_unassigned_variable(assignment)

    for value in csp.order_domain_values(var, assignment):
        if csp.is_consistent(value, assignment):
            state, distance = value
            assignment[state] = distance
            park_visited += csp.parks[state]
            travel_distance = 0
            travel_distance += distance
            inference = csp.inference(var, assignment)
            if inference is not None:
                solution = backtracking(csp, assignment, park_visited)
                if solution is not None:
                    return solution
            del assignment[state]
    return None	
	
def argument_check(args):
	if len(args) != 3:
		print("ERROR: Not enough or too many input arguments.")
		sys.exit(1)

	initial = args[1]
	if initial == " " or not isinstance(initial, str):
		print("ERROR: Not enough or too many input arguments.")
		sys.exit(1)
		
	no_of_parks = int(args[2])
	if no_of_parks < 2:
		print("ERROR: Not enough or too many input arguments.")
		sys.exit(1)

	return initial, no_of_parks

def main():
	# initial, no_of_park = argument_check(sys.argv)

	initial = "OH"
	no_of_park = 17

	csp = CSP(initial, no_of_park)
	assignment = backtracking_search(csp)
	print(assignment)
    
	print("Thien Le A20484898 Solution:")
	print("Initial state: ", initial)
	print("Minimum number of parks: ", no_of_park)
	
	if assignment:
		print("Solution Path:" )
		print("Solution Path:" )
		print("Solution Path:" )

main()