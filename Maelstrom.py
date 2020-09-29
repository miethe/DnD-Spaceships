import random
from Ship import ship
from math import floor
from Roll_Table import RollTable

class MaelstromQuadrant:

    possible_encounters = ['Debris Cloud', 'Increasing Need', 'Smooth Sailing', 'Escape Capsule']
    encounter_weights = [1, 1, 1, 1]
    weighted_encounter_table = None

    sector = 0
    quadrant = ''
    full_coordinates = ''

    def __init__(self, sector, quadrant = ''):
        self.sector = sector
        self.quadrant = quadrant
        self.setCoordinates(quadrant, sector)

    def setCoordinates(self, quadrant, sector = ''):
        if not sector:
            sector = self.sector
        self.full_coordinates = quadrant+sector

    def getCoordinates(self):
        return self.full_coordinates

    def getQuadrant(self):
        return self.quadrant

    def getSector(self):
        return self.sector

    def __calculateMontressorPerceptionCheck(self, current_quadrant, current_sector):
        BASE_CHECK = 10
        QUADRANT_MOD = 2
        SECTOR_MOD = 2

        perception_check = (BASE_CHECK + (QUADRANT_MOD ** self.__getQuadrantDistance(current_quadrant)) + \
            (SECTOR_MOD ** self.__getSectorDistance(current_sector)))

        return int(perception_check)

    def __getQuadrantDistance(self, current_quadrant):
        return abs(ord(current_quadrant.upper()) - ord(self.quadrant))

    def __getSectorDistance(self, current_sector):
        return abs(int(current_sector) - int(self.sector))

    def getMontressorPerceptionCheck(self, current_quadrant, current_sector):
        return self.__calculateMontressorPerceptionCheck(current_quadrant, current_sector)

    def getEncounter(self, useWeights = False):
        if useWeights:
            return self.weighted_encounter_table.get_item()
        else:
            return random.choice(self.possible_encounters)

    def getEncounters(self):
        return self.possible_encounters

    def setEncounters(self, encounters, weights = []):
        self.possible_encounters.append(encounters)
        if not weights:
            for _ in range(len(encounters)):
                weights.append(1)

        #self.weighted_encounter_table = RollTable(self.possible_encounters, weights)

class MaelstromQuadrantA(MaelstromQuadrant):

    def __init__(self, sector):
        MaelstromQuadrant.__init__(self, sector, 'A')

        encounters = ['Gravitite Bulettes', 'Dispel Magic Wave']
        self.setEncounters(encounters)

class MaelstromQuadrantB(MaelstromQuadrant):

    def __init__(self, sector):
        MaelstromQuadrant.__init__(self, sector, 'B')

        encounters = ['Gravitite Bulettes', 'Strong Current', 'Wave of Despair', 'Dispel Magic Wave', 'Roperoid', 'Refuge']
        if sector == '2':
            encounters.append('Watcher of the Storm')

        self.setEncounters(encounters)

class MaelstromQuadrantC(MaelstromQuadrant):

    def __init__(self, sector):
        MaelstromQuadrant.__init__(self, sector, 'C')

        encounters = ['Strong Current', 'Wave of Despair', 'Psychic Storm', 'Dispel Magic Wave', 'Roperoid', 'Refuge']
        self.setEncounters(encounters)

class MaelstromQuadrantD(MaelstromQuadrant):

    def __init__(self, sector):
        MaelstromQuadrant.__init__(self, sector, 'D')

        encounters = ['Strong Current', 'Wave of Despair', 'Psychic Storm', 'Meet Your Echo']
        self.setEncounters(encounters)

class Maelstrom:

    quadrant_defaults = ['A', 'B', 'C', 'D']
    montressor_start_quadrant_default = quadrant_defaults[-2:]
    sector_defaults = ['1', '2', '3', '4', '5', '6', '7', '8']

    quadrant = ''
    sector = 0
    montressor = None
    player_ship = None

    def __init__(self, quadrant = None, sector = None):
        if quadrant and quadrant in self.quadrant_defaults:
            self.quadrant = quadrant
        else:
            self.quadrant = random.choice(self.quadrant_defaults)
        if sector and str(sector) in self.sector_defaults:
            self.sector = str(sector)
        else:
            self.sector = str(random.choice(self.sector_defaults))

        montressor_location = self.getLocationInMaelstrom(random.choice(self.montressor_start_quadrant_default), \
            str(random.choice(self.sector_defaults)))
        self.initMontressor(montressor_location)

        player_location = self.getLocationInMaelstrom(quadrant, sector)
        self.initPlayerShip(player_location)

    # Takes in quadrant and sector and returns a MaelstromQuadrant object
    def getLocationInMaelstrom(self, quadrant, sector) -> MaelstromQuadrant:
        ship_location = None

        if quadrant == 'A':
            ship_location = MaelstromQuadrantA(sector)
        elif quadrant == 'B':
            ship_location = MaelstromQuadrantB(sector)
        elif quadrant == 'C':
            ship_location = MaelstromQuadrantC(sector)
        elif quadrant == 'D':
            ship_location = MaelstromQuadrantD(sector)

        return ship_location

    def getMontressorCoordinates(self):
        return self.montressor.getShipCoordinates()

    def initMontressor(self, montressor_location):
        self.montressor = ship('Montressor', montressor_location)

    def getPlayerCoordinates(self):
        return self.player_ship.getShipCoordinates()

    def initPlayerShip(self, player_location):
        self.player_ship = ship('Player', player_location)

    def movePlayerShip(self, quadrant, sector):
        newLocation = self.getLocationInMaelstrom(quadrant, sector)
        self.player_ship.setNewMaelstromLocation(newLocation)
        return('Ship moved to: ' + str(self.getPlayerCoordinates()))

    def getMontressorPerceptionCheck(self):
        return self.montressor.getMontressorPerceptionCheck(self.player_ship.getShipQuadrant(), self.player_ship.getShipSector())