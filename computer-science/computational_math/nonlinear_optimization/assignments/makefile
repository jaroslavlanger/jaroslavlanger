CC=g++
CFLAGS =-pedantic \
				-Wall \
				-Wextra \
				-fsanitize=address \
				-g

all: solver_1 solver_2 solver_3

solver_1: solver_1.cpp build
	$(CC) $(CFLAGS) solver_1.cpp -o build/solver_1

solver_2: solver_2.cpp build
	$(CC) $(CFLAGS) solver_2.cpp -o build/solver_2

solver_3: solver_3.cpp build
	$(CC) $(CFLAGS) solver_3.cpp -o build/solver_3

# %.o:: %.cpp build
# 	$(CC) $(CFLAGS) -o build/$@ $^

clean:
	rm build/*

