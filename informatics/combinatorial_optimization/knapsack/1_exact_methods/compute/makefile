knapsack.so : knapsack.o
	g++ -shared -Wl,-soname,build/knapsack.so -o build/knapsack.so build/knapsack.o

knapsack.o : knapsack.cpp build
	g++ -c -fPIC knapsack.cpp -o build/knapsack.o
