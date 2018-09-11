# Logic behind meeting scheduler. Takes input in the form of a list of list of tuples, each set of tuples representing one user's unabailable times
# Example included


def schedule(available_times):
	time_table = [[[] for x in range(0,24)] for y in available_times] # Populate schedule table with empty values
	for x,y in zip(available_times, time_table):
		numbers=[]
		for z in x:
			numbers += range(z[0], z[1])
		numbers = list(set(numbers)) # Populate list of busy time
		for time in numbers:
			y[time] = 'x' # Fill schedule table with busy spots
	av = []
	for x in range(0, 24): # Iterates through all given schedules and registers all available meeting hours
		opn = True
		for y in range(0, len(time_table)):
			if time_table[y][x] != 'x':
				if (y == len(time_table)-1) and (opn == True):
					av.append(x)
			else:
				opn = False
	sch = create_schedule([], av) # Recursively iterate through available meetings hours and create tuples of open meeting times in format [start, end]
	print sch

def create_schedule(sch, av_times ):
	if len(av_times)<1:
		return sch
	x = y = [av_times.pop(0)]
	while (av_times[0] == y[0]+1):
		y=[av_times.pop(0)]
		if len(av_times)<1:
			break
	sch.append([x[0],y[0]s+1])
	return create_schedule(sch, av_times)

