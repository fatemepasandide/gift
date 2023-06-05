from rest_framework.test import APITestCase
from rest_framework import status


class TestProfileView(APITestCase):
    def setUp(self) -> None:
        self.url = "http://127.0.0.1:8000/user/"

    def test_view_200_status(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
