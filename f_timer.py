import time
import copy
import signal

def time_funcs(functions, generatorFunc, generatorInput, iterations, batch = False):
	return get_func_time_and_res(functions, generatorFunc, generatorInput, iterations, batch)[0]


def get_func_time_and_res(functions, generatorFunc, generatorInput, iterations, batch = False):
	if not batch:
		print('Initializing...')
	times = [[] for _ in functions]
	results = [[] for _ in functions]
	start = time.time()
	last = start
	for i in range(iterations):
		if(time.time() - last > 6 and not batch):
			print([sum(t) for t in times],'On iteration starting',i,'of',iterations)
			last = time.time()
		funcInput = generatorFunc(*generatorInput)
		for j,func in enumerate(functions):
			run_time, res = time_func(func, copy.deepcopy(funcInput))
			if(run_time > 6 and not batch):
				print('function ', func, ' took ', run_time, 'on problem ', i)
				# print(funcInput)
				print('------')
			times[j].append(run_time)
			results[j].append(res)

		for j in range(len(functions)-1):
			if results[j][i] != results[j+1][i]:
				outputs = ""
				for res in results:
					outputs += str(res[i]) + " "
				print(funcInput, outputs, 'results differ')
				return [""]
				# return funcInput
	finish = time.time()
	if(finish - start > 3 and not batch):
		print(finish - start - sum([sum(func_times) for func_times in times]), ' is non-func processing time out of total ', finish - start)
	return ([sum(func_times) for func_times in times], results[0])





def time_func(function, input):
	start = time.time()
	output = function(*input)
	end = time.time()
	return (end - start, output)


