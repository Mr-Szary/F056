CXX = g++
CXXFLAGS = $(shell root-config --cflags) -I$(PYTHIA8_ROOT)/include -O2
LDFLAGS = $(shell root-config --libs) -L$(PYTHIA8_ROOT)/lib -lpythia8 -ldl

main_higgs: main_higgs.cc
	$(CXX) $@.cc -o $@ $(CXXFLAGS) $(LDFLAGS)

clean:
	rm -f main_higgs higgs_mass.root
