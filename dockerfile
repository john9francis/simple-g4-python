FROM ubuntu:20.04

# We will start by installing spack using curl,
# Then downloading geant4 with spack.

# Update the package list and install required dependencies
RUN apt-get update && apt-get install -y \
    git \
    python3 \
    tar \
    curl

ENTRYPOINT [ "/bin/bash" ]

# link to download geant4 zip:
#https://gitlab.cern.ch/geant4/geant4/-/archive/v11.1.2/geant4-v11.1.2.zip
#https://gitlab.cern.ch/geant4/geant4/-/archive/v11.1.2/geant4-v11.1.2.tar.gz