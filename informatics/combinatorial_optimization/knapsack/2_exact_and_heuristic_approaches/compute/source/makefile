CC = g++

knapsack : ../knapsack.cpp build fptas greedy_heuristic dynamic_programming branch_and_bound brute_force read_problem knap_mock
	$(CC) -Wall -Wextra -pedantic ../knapsack.cpp -fsanitize=address -g -o build/knapsack

fptas : fptas.cpp build
	$(CC) -Wall -Wextra -pedantic fptas.cpp -fsanitize=address -g -o build/fptas

greedy_heuristic : greedy_heuristic.cpp build
	$(CC) -Wall -pedantic -Wextra -Werror greedy_heuristic.cpp -o build/greedy_heuristic

dynamic_programming : dynamic_programming.cpp build
	$(CC) -Wall -Wextra -Werror dynamic_programming.cpp -o build/dynamic_programming

branch_and_bound : branch_and_bound.cpp build
	$(CC) -Wall -Wextra -pedantic branch_and_bound.cpp -fsanitize=address -g -o build/branch_and_bound

brute_force : brute_force.cpp build
	$(CC) -Wall -Wextra -pedantic brute_force.cpp -g -o build/brute_force

read_problem : read_problem.cpp build
	$(CC) -Wall -Wextra -Werror read_problem.cpp -o build/read_problem

knap_mock : knap_mock.cpp build
	$(CC) knap_mock.cpp -o build/knap_mock

clean:
	rm build/*
