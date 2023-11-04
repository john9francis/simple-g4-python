# start from the spack image, so spack is installed
FROM spack/ubuntu-bionic:v0.20.3

# install required dependencies
RUN apt-get update && apt-get install -y \
    git \
    python3

ENV PATH=/opt/spack/bin:$PATH

RUN spack install geant4

WORKDIR /opt

ENTRYPOINT [ "/bin/bash" ]

# link to download geant4 zip:
#https://gitlab.cern.ch/geant4/geant4/-/archive/v11.1.2/geant4-v11.1.2.zip
#https://gitlab.cern.ch/geant4/geant4/-/archive/v11.1.2/geant4-v11.1.2.tar.gz