
class ship:

    name = "Unknown"
    maelstrom_location_data = None
    quadrant = ''
    sector = ''

    def __init__(self, name = "Unknown", maelstrom_location_data = None):
        self.name = name
        self.maelstrom_location_data = maelstrom_location_data

    def getMaelstromLocationData(self):
        return self.maelstrom_location_data

    def setMaelstromCoordinates(self, quadrant, sector):
        self.quadrant = quadrant
        self.sector = sector

    def setNewMaelstromLocation(self, maelstrom_location_data):
        self.maelstrom_location_data = maelstrom_location_data

    def getShipCoordinates(self):
        return self.maelstrom_location_data.getCoordinates()

    def getShipQuadrant(self):
        return self.maelstrom_location_data.getQuadrant()

    def getShipSector(self):
        return self.maelstrom_location_data.getSector()

    def getMontressorPerceptionCheck(self, quadrant, sector):
        return self.maelstrom_location_data.getMontressorPerceptionCheck(quadrant, sector)
