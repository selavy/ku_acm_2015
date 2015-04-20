CC=g++
CFLAGS=-g -std=c++11

EXE=leaded_cribs

all: $(EXE)
	./$(EXE) < input.in > output.out
	diff output.out output.solution

$(EXE): main.cpp
	$(CC) -o $(EXE) $(CFLAGS) main.cpp
.PHONY: clean
clean:
	rm -rf $(EXE) output.out
