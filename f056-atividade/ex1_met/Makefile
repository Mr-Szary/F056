all: testMET

libSimpleMET.so: SimpleMET.cpp SimpleMET.h
	g++ -fPIC -c SimpleMET.cpp -o SimpleMET.o
	g++ -shared -o libSimpleMET.so SimpleMET.o

testMET: testMET.cpp libSimpleMET.so
	g++ testMET.cpp -L. -lSimpleMET -Wl,-rpath,. -o testMET

clean:
	rm -f *.o *.so testMET
