import multiprocessing

def test_func(param):
	print('this. is number {}'.format(param * param))
	return param * param

pool = multiprocessing.Pool(processes=4)
list = [x for x in range(1001)]

result = pool.map(test_func, list)

print('result list')
print(result)


