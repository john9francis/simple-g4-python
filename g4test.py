import Geant4 as g4

from phList import PhysicsList
from detConst import DetectorConstruction

def main():
  run_manager = g4.gRunManager
  run_manager.SetUserInitialization(PhysicsList())
  run_manager.SetUserInitialization(DetectorConstruction())
  #run_manager.Initialize()


  print("Hello G4Py world!")


if __name__ == "__main__":
  main()