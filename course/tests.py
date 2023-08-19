from rest_framework import status
from rest_framework.test import APITestCase


class CourseTestCase(APITestCase):

    def setUp(self) -> None:
        pass

    def test_subscription_check(self):
        response = self.client.post('/course/', {"title": "test", "price": 50})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response2 = self.client.get('/course/')
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        response3 = self.client.post('/user/create/', {"email": "test@test.com", "is_active": "true", "password": 123})
        self.assertEqual(response3.status_code, status.HTTP_201_CREATED)
        response4 = self.client.post('/subscription/create/', {"status": "true", "user": 1, "course": 1})
        self.assertEqual(response4.json(),
                         {"id": 1, "status": True, "user": 1, "course": 1})
