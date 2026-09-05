all: testTrack

libTrack.so: Track.cpp Track.h
	g++ -fPIC -c Track.cpp -o Track.o
	g++ -shared -o libTrack.so Track.o

libSimTrack.so: SimTrack.cpp SimTrack.h libTrack.so
	g++ -fPIC -c SimTrack.cpp -o SimTrack.o
	g++ -shared -o libSimTrack.so SimTrack.o -L. -lTrack -Wl,-rpath,.

testTrack: testTrack.cpp libTrack.so libSimTrack.so
	g++ testTrack.cpp -L. -lTrack -lSimTrack -Wl,-rpath,. -o testTrack

clean:
	rm -f *.o *.so testTrack
