from django.test import SimpleTestCase


class HomePageViewTestCase1(SimpleTestCase):

    def test_request_home_page1(self):
        response = self.client.get('/')
        self.assertContains(response, 'Hello, world!', status_code=200)

