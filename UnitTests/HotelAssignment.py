import pytest
from HotelManagement import HotelManagement
from States import States
class TestHotelAssignment:
    @pytest.fixture
    def hotel(self):
        # Floor
        floor = 4
        # rooms
        rooms = ['A', 'B', 'C', 'D', 'E']
        return HotelManagement(floor, rooms)

    def test_1(self, hotel):
        # First Checkin
        hotel.requestRoomAssignment()
        assert hotel.getRoom('1A').state == States.OCCUPIED
        assert hotel.getRoom('1B').state == States.AVAILABLE

        # Second Checkin
        hotel.requestRoomAssignment()
        assert hotel.getRoom('1B').state == States.OCCUPIED

        # Checkout
        hotel.checkoutRoom('1B')
        assert hotel.getRoom('1B').state == States.VACANT

        # Check in 5 times
        hotel.requestRoomAssignment()
        hotel.requestRoomAssignment()
        hotel.requestRoomAssignment()
        hotel.requestRoomAssignment()
        hotel.requestRoomAssignment()
        assert hotel.firstAvailableKey == "2C"

        # Clean Room
        hotel.markRoomClean('1B')
        assert hotel.firstAvailableKey == "1B"

        # Another Check in
        hotel.requestRoomAssignment()
        assert hotel.firstAvailableKey == "2C"

        # Clean the Occupied room
        assert hotel.getRoom('1A').state == States.OCCUPIED
        hotel.markRoomClean('1A')
        assert hotel.getRoom('1A').state == States.OCCUPIED

        # Checkout and Mark Out of service
        hotel.checkoutRoom('1A')
        hotel.markRoomOOS('1A')
        assert hotel.getRoom('1A').state == States.REPAIR

        # Clean the out of service room
        hotel.markRoomClean('1A')
        assert hotel.getRoom('1A').state == States.REPAIR

        # Repair the room
        hotel.markRoomRepaired('1A')
        assert hotel.getRoom('1A').state == States.VACANT

        # Clean the vacant room
        hotel.markRoomClean('1A')
        assert hotel.getRoom('1A').state == States.AVAILABLE

        # Check first available room
        assert hotel.firstAvailableKey == "1A"
        assert hotel.getRoom('1A').state == States.AVAILABLE

        # Check all vacant room
        assert hotel.checkAllAvailableRooms() == ['1A', '2C', '2B', '2A', '3A', '3B', '3C', '3D', '3E', '4E', '4D', '4C', '4B', '4A']
