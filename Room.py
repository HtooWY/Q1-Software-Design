from States import States


class Room:
    states = ['Available', 'Occupied', 'Vacant', 'Repair']

    def __init__(self, name, prevRoom, nextRoom, state):
        self.name = name
        self.prevRoom = prevRoom
        self.nextRoom = nextRoom
        self.state = state

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
