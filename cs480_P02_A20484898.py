import sys

def argument_check(args):
	if len(args) != 4:
		print("ERROR: Not enough/too many/illegal input arguments. ")
		sys.exit(1)

	algo = args[1]
	if algo not in ['1', '2']:
		print("ERROR: Not enough/too many/illegal input arguments. ")
		sys.exit(1)
		
	first = args[2]
	if first not in ['x', 'o']:
		print("ERROR: Not enough/too many/illegal input arguments. ")
		sys.exit(1)

	mode = args[3]
	if mode not in ['1', '2']:
		print("ERROR: Not enough/too many/illegal input arguments. ")
		sys.exit(1)

	return algo, first, mode
