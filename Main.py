from HotelManagement import HotelManagement

if __name__ == '__main__':
    # Floor
    floor = 4
    # rooms
    rooms = ['A', 'B', 'C', 'D', 'E']
    newHotel = HotelManagement(floor, rooms)
    print("Welcome to boutique Hotel.")
    while True:
        print("\nChoose these options: \n 1. Request Room Assignment \n 2. Check out Room \n 3. Mark a room clean \n 4. Mark a room for repair\n 5. List all the available room.")
        option = input("Enter Option: ")
        # Request Room Assignment
        if option =="1":
            newHotel.requestRoomAssignment()
        # Check out Room
        elif option=="2":
            roomName = input("Enter Room Name: ")
            newHotel.checkoutRoom(roomName)
        # Mark a room clean
        elif option == "3":
            roomName = input("Enter Room Name: ")
            newHotel.markRoomClean(roomName)
        # Mark a room for OOS
        elif option == "4":
            roomName = input("Enter Room Name: ")
            newHotel.markRoomOOS(roomName)
        # List all the available room.
        elif option == "5":
            newHotel.checkAllAvailableRooms()

