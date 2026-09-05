#ifndef SIMTRACK_H
#define SIMTRACK_H
#include "Track.h"

class SimTrack : public Track {
private:
    int pdgId_;
    int parentPdgId_;
public:
    SimTrack(double e, double px, double py, double pz, int pdg, int parent);
    int ParticleId() const;
    int ParentId() const;
};
#endif
