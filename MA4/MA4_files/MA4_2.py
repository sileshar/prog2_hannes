#!/usr/bin/env python3

from integer import Integer
import matplotlib.pyplot as plt
from time import perf_counter
#from numba import njit

def main():
	#time_numba = []
	time_python = []
	time_cpp = []
	for n in range(30, 46):
		#start_numba = perf_counter()
		#fib_numba_py(n)
		#end_numba = perf_counter()
		#time_numba.append(end_numba - start_numba)

		start_python = perf_counter()
		fib_pure_py(n)
		end_python = perf_counter()
		time_python.append(end_python - start_python)

		start_cpp = perf_counter()
		f = Integer(n)
		f.fib()
		end_cpp = perf_counter()
		time_cpp.append(end_cpp - start_cpp)


	n = [x for x in range(30, 45)]
	plt.figure()
	#plt.plot(n, time_numba)
	plt.plot(n, time_python, "r")
	plt.plot(n, time_cpp, "b")
	plt.title("comparison between c++ and python")
	plt.xlabel("n")
	plt.ylabel("seconds")
	plt.savefig("time_graph_all.png")


	#time_numba = []
	#time_python = []
	#for n in range(1, 31):
		#start_numba = perf_counter()
		#fib_numba_py(n)
		#end_numba = perf_counter()
		#time_numba.append(end_numba - start_numba)

		#start_python = perf_counter()
		#fib_pure_py(n)
		#end_python = perf_counter()
		#time_python.append(end_python - start_python)


	#n = [x for x in range(1, 30)]
	#plt.figure()
	#plt.plot(n, time_numba)
	#plt.plot(n, time_python)
	#plt.savefig("time_graph_python_numba.png")


	f = Integer(47)
	print(f.fib())
	#print(f.fib(), fib_numba_py(47))


#@njit
#def fib_numba_py(n):
	#if n <= 1:
		#return n
	#else:
		#return (fib_numba_py(n - 1) + fib_numba_py(n - 2))



def fib_pure_py(n):
	if n <= 1:
		return n
	else:
		return (fib_pure_py(n - 1) + fib_pure_py(n - 2))


if __name__ == '__main__':
	main()
