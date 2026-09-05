#ifndef TRACK_H
#define TRACK_H

class Track {
private:
    double e_;
    double px_;
    double py_;
    double pz_;

public:
    Track(double e, double px, double py, double pz);

    double E() const;
    double Px() const;
    double Py() const;
    double Pz() const;

    double Pt() const;
    double Eta() const;
};

#endif
