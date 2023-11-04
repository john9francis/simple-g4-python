from Geant4 import G4VModularPhysicsList

class PhysicsList(G4VModularPhysicsList):
  def __init__(self):
    super(G4VModularPhysicsList, self).__init__()


  def ConstructParticle(self):
    pass

  def ConstructProcess(self):
    pass