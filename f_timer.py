import time

def time_funcs(functions, generatorFunc, generatorInput, iterations):
	return get_func_time_and_res(functions, generatorFunc, generatorInput, iterations)[0]


def get_func_time_and_res(functions, generatorFunc, generatorInput, iterations):

	times = [[] for _ in functions]
	results = [[] for _ in functions]
	for i in range(iterations):
		funcInput = generatorFunc(*generatorInput)
		for j,func in enumerate(functions):
			run_time, res = time_func(func, funcInput)
			times[j].append(run_time)
			results[j].append(res)

		for j in range(len(functions)-1):
			if results[j][i] != results[j+1][i]:
				print(results[j][i],results[j+1][i],'results differ')
				return funcInput

	return ([sum(func_times) for func_times in times], results[0])





def time_func(function, input):
	start = time.time()
	output = function(*input)
	end = time.time()
	return (end - start, output)

