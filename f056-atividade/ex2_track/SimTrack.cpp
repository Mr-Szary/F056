#include "SimTrack.h"

SimTrack::SimTrack(double e, double px, double py, double pz, int pdg, int parent)
    : Track(e, px, py, pz), pdgId_(pdg), parentPdgId_(parent) {}

int SimTrack::ParticleId() const { return pdgId_; }
int SimTrack::ParentId() const { return parentPdgId_; }
