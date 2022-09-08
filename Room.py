from States import States


class Room:

    def __init__(self, name):
        self.name = name
        self.prevRoom = None
        self.nextRoom = None
        self.state = States.AVAILABLE

    def insertPrevRoom(self, prevRoom):
        self.prevRoom = prevRoom

    def insertNextRoom(self, nextRoom):
        self.nextRoom = nextRoom

    def checkin(self):
        if self.state == States.AVAILABLE:
            self.state = States.OCCUPIED
            return True
        return False

    def checkout(self):
        if self.state == States.OCCUPIED:
            self.state = States.VACANT
            return True
        return False

    def clean(self):
        if self.state == States.VACANT:
            self.state = States.AVAILABLE
            return True
        return False

    def outofservice(self):
        if self.state == States.VACANT:
            self.state = States.REPAIR
            return True
        return False

    def repair(self):
        if self.state == States.REPAIR:
            self.state = States.VACANT
            return True
        return False

    def checkAvailability(self):
        if self.state == States.AVAILABLE:
            return self.name
        else:
            if self.nextRoom:
                return self.nextRoom.checkAvailability()
            return None

    def checkCurrentAvaility(self):
        return self.state == States.AVAILABLE
