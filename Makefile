
CXX = g++

CXXFLAGS = -Wall -Wextra -O2

SOURCES = src/program.cpp

EXECUTABLE = program

all: $(EXECUTABLE)

$(EXECUTABLE): $(SOURCES)
	$(CXX) $(CXXFLAGS) $(SOURCES) -o $(EXECUTABLE)

clean:
	rm -f $(EXECUTABLE)
