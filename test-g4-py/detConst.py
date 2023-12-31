from Geant4 import G4VUserDetectorConstruction

from Geant4 import G4Box
from Geant4 import G4LogicalVolume
from Geant4 import G4PVPlacement
from Geant4 import G4ThreeVector
from Geant4 import G4RotationMatrix
from Geant4 import G4Transform3D

from Geant4 import gNistManager

class DetectorConstruction(G4VUserDetectorConstruction):
  def __init__(self):
    super(DetectorConstruction, self).__init__()



  def Construct(self):

    # Define materials
    nist_manager = gNistManager.Instance()
    air = nist_manager.FindOrBuildMaterial("G4_AIR")
    gold = nist_manager.FindOrBuildMaterial("G4_Au")

    # Define world
    solidWorld = G4Box("solidWorld", 10, 10, 10)
    logicWorld = G4LogicalVolume(solidWorld, air, "logicWorld")

    # Define a detector
    solidDet = G4Box("solidDet", 1, 1, 1)
    logicDet = G4LogicalVolume(solidDet, gold, "logicDet")

    # place things in the world:
    physWorld = G4PVPlacement(None, G4ThreeVector(), logicWorld, "physWorld", None, False, 0)

    return logicWorld
    