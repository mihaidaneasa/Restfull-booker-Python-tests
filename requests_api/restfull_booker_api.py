import requests

class RestfullBookerApi:

    __BASE_URL = 'https://restful-booker.herokuapp.com'

    __AUTH_ENDPOINT = '/auth'
    __AUTH_NEGATIVE_ENDPOINT = '/authorization'
    __BOOKING_ENDPOINT = '/booking'
    __BOOKING_NEGATIVE_ENDPOINT = '/book'
    __PING_ENDPOINT = '/ping'

    def __get_auth_route(self):
        return self.__BASE_URL + self.__AUTH_ENDPOINT

    def __get_auth_route_negative(self):
        return self.__BASE_URL + self.__AUTH_NEGATIVE_ENDPOINT

    def __get_booking_route(self):
        return self.__BASE_URL + self.__BOOKING_ENDPOINT

    def __get_booking_route_notFound(self):
        return self.__BASE_URL + self.__BOOKING_NEGATIVE_ENDPOINT

    def __get_ping_route(self):
        return self.__BASE_URL + self.__PING_ENDPOINT


    def __get_booking_by_id(self, id):
        return self.__get_booking_route() + f'/{id}'

    def post_api_authorization_positive(self):
        URL = self.__get_auth_route()

        body = {
            'username': 'admin',
            'password': 'password123'
        }

        return requests.post(URL, json=body)

    def post_api_authorization_negative_badCredentials(self):
        URL = self.__get_auth_route()

        body = {
            'username': 'Mihai',
            'password': 'password123'
        }

        return requests.post(URL, json=body)

    def post_api_authorization_negative_notFound(self):
        URL = self.__get_auth_route_negative()

        body = {
            'username': 'admin',
            'password': 'password123'
        }

        return requests.post(URL, json=body)

    def generate_access_token(self):
        response = self.post_api_authorization_positive()

        if response.status_code == 201:
            return response.json()['accessToken']

        return ''

    def __generate_authorization_token(self, access_token):
        return {
            'Authorization': f'Bearer {access_token}'
        }

    def __body_json(self, first_name, last_name, total_price, deposit_paid, checkin_date, checkout_date, additional_needs):
        return {
            'firstname': f'{first_name}',
            'lastname': f'{last_name}',
            'totalprice': f'{total_price}',
            'depositpaid': f'{deposit_paid}',
            'bookingdates': {
                'checkin': f'{checkin_date}',
                'checkout': f'{checkout_date}'
            },
            'additionalneeds': f'{additional_needs}'
        }

    def get_api_all_bookings_ids(self):
        URL = self.__get_booking_route()
        return requests.get(URL)

    def get_api_booking_by_id(self, id):
        URL = self.__get_booking_by_id(id)
        return requests.get(URL)

    def post_api_create_booking(self, access_token, first_name, last_name, total_price, deposit_paid, checkin_date, checkout_date, additional_needs):
        URL = self.__get_booking_route()

        return requests.post(URL, json=self.__body_json(first_name, last_name, total_price, deposit_paid, checkin_date, checkout_date, additional_needs), headers=self.__generate_authorization_token(access_token))

    def post_api_create_booking_negative(self, first_name, last_name, total_price, deposit_paid, checkin_date, checkout_date, additional_needs):
        URL = self.__get_booking_route()

        headers = {
            'Authorization': 'I do not have a token'
        }

        return requests.post(URL, json=self.__body_json(first_name, last_name, total_price, deposit_paid, checkin_date, checkout_date, additional_needs), headers=headers)

    def post_api_create_booking_negative_notFound(self, first_name, last_name, total_price, deposit_paid, checkin_date, checkout_date, additional_needs):
        URL = self.__get_booking_route_notFound()

        return requests.post(URL, json=self.__body_json(first_name, last_name, total_price, deposit_paid, checkin_date, checkout_date, additional_needs))

    def put_api_booking(self, booking_id, new_first_name, new_last_name, new_total_price, new_deposit_paid, new_checkin_date, new_checkout_date, new_additional_needs):
        URL = self.__get_booking_by_id(booking_id)

        headers = {
            'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='
        }

        # body = {
        #     'firstname': new_first_name,
        #     'lastname': new_last_name,
        #     'totalprice': new_total_price,
        #     'depositpaid': new_deposit_paid,
        #     'bookingdates': {
        #         'checkin': new_checkin_date,
        #         'checkout': new_checkout_date
        #     },
        #     'additionalneeds': new_additional_needs
        # }

        return requests.put(URL, json=self.__body_json(new_first_name, new_last_name, new_total_price, new_deposit_paid, new_checkin_date, new_checkout_date, new_additional_needs), headers=headers)

    def put_api_booking_negative(self, booking_id, new_first_name, new_last_name, new_total_price, new_deposit_paid, new_checkin_date, new_checkout_date, new_additional_needs):
        URL = self.__get_booking_by_id(booking_id)

        headers = {
            'Authorization': ''
        }

        return requests.put(URL, json=self.__body_json(new_first_name, new_last_name, new_total_price, new_deposit_paid, new_checkin_date, new_checkout_date, new_additional_needs), headers=headers)

    def patch_api_booking(self, booking_id, new_firstname, new_lastname, new_depositpaid):
        URL = self.__get_booking_by_id(booking_id)

        headers = {
            'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='
        }

        body = {
            'firstname': new_firstname,
            'lastname': new_lastname,
            'depositpaid': new_depositpaid,
        }

        return requests.patch(URL, json=body, headers=headers)

    def patch_api_booking_negative(self, booking_id, new_firstname, new_lastname, new_depositpaid):
        URL = self.__get_booking_by_id(booking_id)

        headers = {
            'Authorization': 'I don not have a token'
        }

        body = {
            'firstname': new_firstname,
            'lastname': new_lastname,
            'depositpaid': new_depositpaid,
        }

        return requests.patch(URL, json=body, headers=headers)

    def delete_api_booking(self, booking_id):
        URL = self.__get_booking_by_id(booking_id)

        # cookie = {
        #     'Cookie': f'token={access_token}'
        # }

        headers = {
            'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='
        }

        return requests.delete(URL, headers=headers)

    def delete_api_booking_negative(self, booking_id):
        URL = self.__get_booking_by_id(booking_id)

        headers = {
            'Authorization': 'I do not have a token'
        }

        return requests.delete(URL, headers=headers)

    def get_api_ping_server(self):
        URL = self.__get_ping_route()

        return requests.get(URL)