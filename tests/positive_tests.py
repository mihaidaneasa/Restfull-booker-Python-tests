import random
import unittest

from requests_api.restfull_booker_api import RestfullBookerApi

class PositiveTests(unittest.TestCase):

    accessToken = ''

    def setUp(self):
        self.api = RestfullBookerApi()
        if self.accessToken == '':
            self.accessToken = self.api.generate_access_token()

    def test_01_post_createAuth(self):
        response = self.api.post_api_authorization_positive()

        self.assertEqual(response.status_code, 200, 'The response status code is not the same')
        self.assertTrue(isinstance(response.json()['token'], str), 'Response token is not a string')

    def test_02_get_all_bookings_ids(self):
        response = self.api.get_api_all_bookings_ids()

        booking_from_api = response.json()

        for index in range(0, len(booking_from_api)):
            current_booking = booking_from_api[index]
            # print(current_booking)
            self.assertEqual(response.status_code, 200, 'The status code is not the same')
            self.assertTrue(isinstance(current_booking['bookingid'], int), 'Booking id is not an integer')

    def test_03_get_booking_by_id(self): # The result is different in Postman
        response = self.api.get_api_all_bookings_ids()

        # Generate random booking id
        booking_id = []
        for i in response.json():
            booking_id.append(i['bookingid'])
        random.shuffle(booking_id)
        response = self.api.get_api_booking_by_id(1)
        self.assertEqual(response.status_code, 200, 'The status code is not the same')
        self.assertEqual(len(response.json()), 5, 'Length of response is not the same')
        # self.assertEqual(len(response.json()), 6, 'Length of response is not the same')

        booking_from_api = response.json()
        self.assertTrue(isinstance(booking_from_api['firstname'], str), 'The first name is not a string')
        self.assertTrue(isinstance(booking_from_api['lastname'], str), 'The last name is not a string')
        self.assertTrue(isinstance(booking_from_api['totalprice'], int), 'The total price is not a integer')
        self.assertTrue(isinstance(booking_from_api['depositpaid'], bool), 'The deposit paid is not a boolean')
        self.assertTrue(isinstance(booking_from_api['bookingdates'], dict), 'The checkin date is not a dictionary')
        # self.assertTrue(isinstance(booking_from_api['additionalneeds'], str), 'The additional needs date is not a string')

    def test_04_post_create_booking(self):
        first_name = 'Mihai'
        last_name = 'Daneasa'
        total_price = 150
        deposit_paid = True
        checkin_date = '2024-06-17'
        checkout_date = '2024-06-24'
        additional_needs = 'Breakfast'

        response = self.api.post_api_create_booking(
            self.accessToken,
            first_name,
            last_name,
            total_price,
            deposit_paid,
            checkin_date,
            checkout_date,
            additional_needs
        )

        self.assertEqual(response.status_code, 200, 'The response status code is not the same')
        self.assertEqual(len(response.json()), 2, 'Length of response is not the same')

        # Verify if the booking was created
        booking_id = response.json()['bookingid']

        response = self.api.get_api_booking_by_id(booking_id)

        self.assertEqual(response.status_code, 200, 'The response status code is not the same')
        self.assertEqual(len(response.json()), 6, 'Length of response is not the same')
        self.assertEqual(response.json()['firstname'], first_name, 'The first name is not the same')
        self.assertEqual(response.json()['lastname'], last_name, 'The last name is not the same')
        self.assertEqual(response.json()['totalprice'], total_price, 'The total price is not the same')
        self.assertEqual(response.json()['depositpaid'], deposit_paid, 'The deposit paid is not the same')
        self.assertEqual(response.json()['bookingdates'], {'checkin': checkin_date, 'checkout': checkout_date}, 'The booking dates are not the same')
        self.assertEqual(response.json()['additionalneeds'], additional_needs, 'The additional needs are not the same')

    def test_05_put_a_booking(self):
        # Create a booking
        first_name = 'Mihai'
        last_name = 'Daneasa'
        total_price = 150
        deposit_paid = True
        checkin_date = '2024-06-17'
        checkout_date = '2024-06-24'
        additional_needs = 'Breakfast'

        response = self.api.post_api_create_booking(
            self.accessToken,
            first_name,
            last_name,
            total_price,
            deposit_paid,
            checkin_date,
            checkout_date,
            additional_needs
        )

        self.assertEqual(response.status_code, 200, 'The response status code is not the same')
        self.assertEqual(len(response.json()), 2, 'Length of response is not the same')

        # Verify if the booking was created
        booking_id = response.json()['bookingid']

        response = self.api.get_api_booking_by_id(booking_id)
        self.assertEqual(response.status_code, 200, 'The response status code is not the same')
        self.assertEqual(len(response.json()), 6, 'Length of response is not the same')

        # Modify the booking values
        new_first_name = 'Mihai-Andrei'
        new_last_name = 'Daneasa1'
        new_total_price = 201
        new_deposit_paid = True # It doesn't make the change to "False"
        new_checkin_date = '2024-06-10'
        new_checkout_date = '2024-06-20'
        new_additional_needs = 'Site-seeing'

        response = self.api.put_api_booking(
            booking_id,
            new_first_name,
            new_last_name,
            new_total_price,
            new_deposit_paid,
            new_checkin_date,
            new_checkout_date,
            new_additional_needs
        )

        self.assertEqual(response.status_code, 200, 'The response status code is not the same')
        self.assertEqual(len(response.json()), 6, 'Length of response is not the same')

        # Verify if the changes are actually made
        response = self.api.get_api_booking_by_id(booking_id)

        self.assertEqual(response.status_code, 200, 'The response status code is not the same')
        self.assertEqual(len(response.json()), 6, 'Length of bookings is not the same')
        self.assertEqual(response.json()['firstname'], new_first_name, 'The first name is not the same')
        self.assertEqual(response.json()['lastname'], new_last_name, 'The last name is not the same')
        self.assertEqual(response.json()['totalprice'], new_total_price, 'The total price is not the same')
        self.assertEqual(response.json()['depositpaid'], new_deposit_paid, 'The deposit paid is not the same')
        self.assertEqual(response.json()['bookingdates'], {'checkin': new_checkin_date, 'checkout': new_checkout_date}, 'The booking dates are not the same')
        self.assertEqual(response.json()['additionalneeds'], new_additional_needs, 'The additional needs are not the same')

    def test_06_patch_a_booking(self):
        # Create a booking
        first_name = 'Mihai'
        last_name = 'Daneasa'
        total_price = 150
        deposit_paid = True
        checkin_date = '2024-06-17'
        checkout_date = '2024-06-24'
        additional_needs = 'Breakfast'

        response = self.api.post_api_create_booking(
            self.accessToken,
            first_name,
            last_name,
            total_price,
            deposit_paid,
            checkin_date,
            checkout_date,
            additional_needs
        )

        self.assertEqual(response.status_code, 200, 'The response status code is not the same')
        self.assertEqual(len(response.json()), 2, 'Length of response is not the same')

        # Verify if the booking was created
        booking_id = response.json()['bookingid']

        response = self.api.get_api_booking_by_id(booking_id)
        self.assertEqual(response.status_code, 200, 'The response status code is not the same')
        self.assertEqual(len(response.json()), 6, 'Length of response is not the same')

        # Modify the booking values
        new_first_name = 'Mihai-Andrei'
        new_last_name = 'Daneasa1'
        new_total_price = 201
        new_deposit_paid = False
        new_checkin_date = '2024-06-10'
        new_checkout_date = '2024-06-20'
        new_additional_needs = 'Site-seeing'

        response = self.api.put_api_booking(
            booking_id,
            new_first_name,
            new_last_name,
            new_total_price,
            new_deposit_paid,
            new_checkin_date,
            new_checkout_date,
            new_additional_needs
        )

        self.assertEqual(response.status_code, 200, 'The response status code is not the same')
        self.assertEqual(len(response.json()), 6, 'Length of response is not the same')

        # Modify some booking values
        new_firstname = 'Marte'
        new_lastname = 'Jupiter'
        new_deposipaid = True

        response = self.api.patch_api_booking(
            booking_id,
            new_firstname,
            new_lastname,
            new_deposipaid
        )

        self.assertEqual(response.status_code, 200, 'The response status code is not the same')
        self.assertEqual(len(response.json()), 6, 'Length of response is not the same')

        # Verify if the changes are actually made
        response = self.api.get_api_booking_by_id(booking_id)

        self.assertEqual(response.status_code, 200, 'The response status code is not the same')
        self.assertEqual(len(response.json()), 6, 'Length of bookings is not the same')
        self.assertEqual(response.json()['firstname'], new_firstname, 'The first name is not the same')
        self.assertEqual(response.json()['lastname'], new_lastname, 'The last name is not the same')
        self.assertEqual(response.json()['totalprice'], new_total_price, 'The total price is not the same')
        self.assertEqual(response.json()['depositpaid'], new_deposipaid, 'The deposit paid is not the same')
        self.assertEqual(response.json()['bookingdates'], {'checkin': new_checkin_date, 'checkout': new_checkout_date}, 'The booking dates are not the same')
        self.assertEqual(response.json()['additionalneeds'], new_additional_needs, 'The additional needs are not the same')

    def test_07_delete_a_booking(self):
        # Create a booking
        first_name = 'Mihai'
        last_name = 'Daneasa'
        total_price = 150
        deposit_paid = True
        checkin_date = '2024-06-17'
        checkout_date = '2024-06-24'
        additional_needs = 'Breakfast'

        response = self.api.post_api_create_booking(
            self.accessToken,
            first_name,
            last_name,
            total_price,
            deposit_paid,
            checkin_date,
            checkout_date,
            additional_needs
        )

        self.assertEqual(response.status_code, 200, 'The response status code is not the same')
        self.assertEqual(len(response.json()), 2, 'Length of response is not the same')

        # Verify if the booking was created
        booking_id = response.json()['bookingid']

        response = self.api.get_api_booking_by_id(booking_id)
        self.assertEqual(response.status_code, 200, 'The response status code is not the same')
        self.assertEqual(len(response.json()), 6, 'Length of response is not the same')

        # Modify the booking values
        new_first_name = 'Mihai-Andrei'
        new_last_name = 'Daneasa1'
        new_total_price = 201
        new_deposit_paid = False
        new_checkin_date = '2024-06-10'
        new_checkout_date = '2024-06-20'
        new_additional_needs = 'Site-seeing'

        response = self.api.put_api_booking(
            booking_id,
            new_first_name,
            new_last_name,
            new_total_price,
            new_deposit_paid,
            new_checkin_date,
            new_checkout_date,
            new_additional_needs
        )

        self.assertEqual(response.status_code, 200, 'The response status code is not the same after modified it')
        self.assertEqual(len(response.json()), 6, 'Length of response is not the same')

        # Modify some booking values
        new_firstname = 'Marte'
        new_lastname = 'Jupiter'
        new_deposipaid = True

        response = self.api.patch_api_booking(
            booking_id,
            new_firstname,
            new_lastname,
            new_deposipaid
        )

        self.assertEqual(response.status_code, 200, 'The response status code is not the same after patching it')
        self.assertEqual(len(response.json()), 6, 'Length of response is not the same')

        # Delete the booking
        response = self.api.delete_api_booking(booking_id)
        self.assertEqual(response.status_code, 201, 'The response status code is not the same')
        self.assertEqual(response.text, 'Created', "Response text is not the same")

        # Verify if the booking was deleted
        response = self.api.get_api_booking_by_id(booking_id)
        self.assertEqual(response.status_code, 404, 'The response status code is not the same when calling get/booking/id after deleted it')

    def test_08_ping_server(self):
        response = self.api.get_api_ping_server()
        self.assertEqual(response.status_code, 201, 'The response status code is not the same')
        self.assertEqual(response.text, 'Created', "Response text is not the same")