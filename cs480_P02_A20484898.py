import sys
import csv

def load_data():

	driving = {}
	with open("driving2.csv") as file:
		csvreader = csv.reader(file)
		states = next(csvreader)[1:]
		for row in csvreader:
			state = row[0]
			driving[state] = {}
			for i, distance in enumerate(row[1:]):
				driving[state][states[i]] = int(distance)

	parks = {}
	with open("parks.csv") as file:
		csvreader = csv.reader(file)
		states = next(csvreader)[1:]
		no_parks = next(csvreader)[1:]
		parks = {states[i]: int(no_parks[i]) for i in range(len(states))}

	zones = {}
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

		Z_number = {i: sorted(j) for i, j in sorted(state_in_zones.items())}

	return driving, parks, zones, Z_number

def backtracking_search(csp):
	return backtracking(csp, {})

def backtracking(csp, assignment):
	if assignment.is_complete():
		return assignment
	
	var = select_unassigned_variable(csp, assignment)

	for value in csp.order_domain_values(var, assignment):
		if csp.is_consistent(var, assignment):
			assignment[var] = value
			interference = csp.interference(var, assignment)
			if interference is not None:
				csp += interference
				result = backtracking(csp, assignment)
				if result != None:
					return result
				csp -= interference
			assignment[var] = 0
		return None	

def select_unassigned_variable(csp, assignment):
	for var in sorted(csp['variable']):
		if var not in assignment:
			return var
	return None

def is_complete(csp, assignment):
	return 0

def argument_check(args):
	if len(args) != 3:
		print("ERROR: Not enough or too many input arguments.")
		sys.exit(1)

	initial = args[1]
	if initial != " " or type(initial) != str:
		print("ERROR: Not enough or too many input arguments.")
		sys.exit(1)
		
	no_of_parks = args[2]
	if no_of_parks < 2:
		print("ERROR: Not enough or too many input arguments.")
		sys.exit(1)

	return initial, no_of_parks

def main():
	#initial, no_of_park = argument_check(sys.argv)

	#print("Thien Le A20484898 Solution:")
	#print("Initial state: ", initial)
	#print("Minimum number of parks: ", no_of_park)
	return 0


print(load_data())