#include "Track.h"
#include <cmath>

double Track::Pt() const {
    return std::sqrt(px_ * px_ + py_ * py_);
}

double Track::Eta() const {
    double pt = Pt();
    if (pt == 0.0) 
        return (pz_ >= 0) ? 1e9 : -1e9; 
    }
    double p = std::sqrt(pt * pt + pz_ * pz_);
    double theta = std::acos(pz_ / p);
    return -std::log(std::tan(theta / 2.0));
}
