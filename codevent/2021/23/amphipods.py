class Amphipod():
    def __init__(self, type):
        self.type = type

class Room():
    def __init__(self, location, amphipod):
        self.location = location
        self.amphipod = Amphipod(amphipod)
        self.exits =
