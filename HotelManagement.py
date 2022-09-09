from Room import Room

class HotelManagement:

    def __init__(self, floor, rooms):
        self.floor = floor
        self.rooms = rooms
        self.hotelLayout = self.arrangeRooms()
        self.roomNameList = list(self.hotelLayout.keys())
        self.firstAvailableKey = self.roomNameList[0]

    def arrangeRooms(self):
        hotelLayout= {}
        for i in range(1,self.floor+1):
            # Even
            if i % 2 == 0:
                hotelLayout.update({str(i) + n: Room(str(i) + n) for n in self.rooms[::-1]})
            # Odd
            else:
                hotelLayout.update({str(i) + n: Room(str(i) + n) for n in self.rooms})

        RoomNameList = list(hotelLayout.keys())
        for i in range(len(RoomNameList)):

            if i>0:
                hotelLayout[RoomNameList[i]].insertPrevRoom(hotelLayout[RoomNameList[i-1]])
            if i<(len(RoomNameList)-1):
                hotelLayout[RoomNameList[i]].insertNextRoom(hotelLayout[RoomNameList[i + 1]])

        return hotelLayout

    def requestRoomAssignment(self):
        if not self.firstAvailableKey:
            print("All the rooms are checked-in.")
            return False
        room = self.hotelLayout[self.firstAvailableKey]
        if room.checkin():
            print("Hotel Room "+room.name+" is assigned and checked in. ")
            print("Hotel Room " + room.name + " is "+ room.state +" now.")

        self.firstAvailableKey = room.nextRoom.checkAvailability()

    def checkoutRoom(self, roomName):
        if roomName not in self.roomNameList:
            print("Room Name is not valid.")
            return
        room = self.hotelLayout[roomName]
        if room.checkout():
            print("Hotel Room " + room.name + " is checked out.")
            print("Hotel Room " + room.name + " is " + room.state + " now.")
        else:
            print("Hotel Room " + room.name + " is " + room.state + " now. You can't check out.")

    def markRoomClean(self, roomName):
        if roomName not in self.roomNameList:
            print("Room Name is not valid.")
            return
        room = self.hotelLayout[roomName]
        if room.clean():
            print("Hotel Room " + room.name + " is clean.")
            print("Hotel Room " + room.name + " is " + room.state + " now.")
        else:
            print("Hotel Room " + room.name + " is " + room.state + " now. You can't clean the room.")
        self.firstAvailableKey = self.hotelLayout[self.roomNameList[0]].checkAvailability()

    def markRoomOOS(self, roomName):
        if roomName not in self.roomNameList:
            print("Room Name is not valid.")
            return
        room = self.hotelLayout[roomName]
        if room.outofservice():
            print("Hotel Room " + room.name + " is out of service for repair.")
            print("Hotel Room " + room.name + " is " + room.state + " now.")
        else:
            print("Hotel Room " + room.name + " is " + room.state + " now. You can't mark for out of service.")

    def markRoomRepaired(self, roomName):
        if roomName not in self.roomNameList:
            print("Room Name is not valid.")
            return
        room = self.hotelLayout[roomName]
        if room.repair():
            print("Hotel Room " + room.name + " is repaired.")
            print("Hotel Room " + room.name + " is " + room.state + " now.")
        else:
            print("Hotel Room " + room.name + " is " + room.state + " now. You can't repair the room.")
        self.firstAvailableKey = self.hotelLayout[self.roomNameList[0]].checkAvailability()

    def checkAllAvailableRooms(self):
        availableRooms =  ([key for key in self.roomNameList if self.hotelLayout[key].checkCurrentAvaility()])
        print(availableRooms)
        return availableRooms

    def getRoom(self, roomName):
        if roomName not in self.roomNameList:
            return None
        return self.hotelLayout[roomName]




