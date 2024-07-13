import unittest

from requests_api.restfull_booker_api import RestfullBookerApi

class NegativeTests(unittest.TestCase):

    accessToken = ''

    def setUp(self):
        self.api = RestfullBookerApi()
        if self.accessToken == '':
            self.accessToken = self.api.generate_access_token()

    def test_01_post_createAuth_badCredentials(self):
        response = self.api.post_api_authorization_negative_badCredentials()
        self.assertEqual(response.status_code, 200, 'The response status code is not the same')

        try:
            self.assertTrue(isinstance(response.json()['token'], str), 'Response token is not a string')
        except:
            print('The test is negative')

        for key in response.json():
            self.assertTrue(isinstance(response.json()['reason'], str), 'Response token is not a string')
            self.assertEqual(response.json()[key], 'Bad credentials', 'The message is different')

    def test_02_post_createAuth_notFound(self):
        response = self.api.post_api_authorization_negative_notFound()

        try:
            self.assertEqual(response.status_code, 200, 'The response status code is not the same')
            self.assertTrue(isinstance(response.json()['token'], str), 'Response token is not a string')
        except:
            print('The test is negative')

        self.assertEqual(response.status_code, 404, 'The response status code is not the same')
        self.assertEqual(response.text, 'Not Found', 'The message is different')

    def test_03_get_booking_by_id_notFound(self):
        response = self.api.get_api_all_bookings_ids()

        response = self.api.get_api_booking_by_id(-1)
        try:
            self.assertEqual(response.status_code, 200, 'The status code is not the same')
        except:
            print('The test is negative')

        self.assertEqual(response.status_code, 404, 'The status code is not the same')
        self.assertEqual(response.text, 'Not Found', "Response text is not the same")

    def test_04_post_create_booking_forbidden(self): # The booking is created instead of being forbidden
        first_name = 'Mihai'
        last_name = 'Daneasa'
        total_price = 150
        deposit_paid = True
        checkin_date = '2024-06-17'
        checkout_date = '2024-06-24'
        additional_needs = 'Breakfast'

        response = self.api.post_api_create_booking_negative(
            first_name,
            last_name,
            total_price,
            deposit_paid,
            checkin_date,
            checkout_date,
            additional_needs
        )

        try:
            self.assertEqual(response.status_code, 200, 'The response status code is not the same')
            self.assertEqual(len(response.json()), 2, 'Length of response is not the same')
        except:
            print('The test is negative')

        self.assertEqual(response.status_code, 403, 'The response status code is not the same')
        self.assertEqual(response.text, 'Forbidden', 'The message is different')

    def test_05_post_create_booking_notFound(self):
        first_name = 'Mihai'
        last_name = 'Daneasa'
        total_price = 150
        deposit_paid = True
        checkin_date = '2024-06-17'
        checkout_date = '2024-06-24'
        additional_needs = 'Breakfast'

        response = self.api.post_api_create_booking_negative_notFound(
            first_name,
            last_name,
            total_price,
            deposit_paid,
            checkin_date,
            checkout_date,
            additional_needs
        )

        try:
            self.assertEqual(response.status_code, 200, 'The response status code is not the same')
            self.assertEqual(len(response.json()), 2, 'Length of response is not the same')
        except:
            print('The test is negative')

        self.assertEqual(response.status_code, 404, 'The status code is not the same')
        self.assertEqual(response.text, 'Not Found', "Response text is not the same")

    def test_06_put_a_booking_forbidden(self):
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

        response = self.api.put_api_booking_negative(
            booking_id,
            new_first_name,
            new_last_name,
            new_total_price,
            new_deposit_paid,
            new_checkin_date,
            new_checkout_date,
            new_additional_needs
        )

        try:
            self.assertEqual(response.status_code, 200, 'The response status code is not the same')
            self.assertEqual(len(response.json()), 6, 'Length of response is not the same')
        except:
            print('The test is negative')

        self.assertEqual(response.status_code, 403, 'The response status code is not the same')
        self.assertEqual(response.text, 'Forbidden', 'The message is different')

    def test_07_patch_a_booking_forbidden(self):
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

        response = self.api.patch_api_booking_negative(
            booking_id,
            new_firstname,
            new_lastname,
            new_deposipaid
        )

        try:
            self.assertEqual(response.status_code, 200, 'The response status code is not the same')
            self.assertEqual(len(response.json()), 6, 'Length of response is not the same')
        except:
            print('The test is negative')

        self.assertEqual(response.status_code, 403, 'The response status code is not the same')
        self.assertEqual(response.text, 'Forbidden', 'The message is different')

    def test_08_delete_a_booking_forbidden(self):
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

        # Delete the booking
        response = self.api.delete_api_booking_negative(booking_id)

        try:
            self.assertEqual(response.status_code, 201, 'The response status code is not the same')
            self.assertEqual(response.text, 'Created', "Response text is not the same")
        except:
            print('The test is negative')

        self.assertEqual(response.status_code, 403, 'The response status code is not the same')
        self.assertEqual(response.text, 'Forbidden', 'The message is different')

        # Verify if the booking was not deleted
        response = self.api.get_api_booking_by_id(booking_id)
        self.assertEqual(response.status_code, 200, 'The response status code is not the same')
        self.assertEqual(len(response.json()), 6, 'Length of response is not the same')