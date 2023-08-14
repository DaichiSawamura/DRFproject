from rest_framework import status
from rest_framework.test import APITestCase


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        pass

    def test_lesson_create(self):
        """Тест создания урока"""
        response = self.client.post('/lesson/create/', {"title": "test"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
