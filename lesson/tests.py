from rest_framework import status
from rest_framework.test import APITestCase

from lesson.models import Lesson


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        pass

    def test_lesson_create(self):
        """Тест создания урока"""
        response = self.client.post('/lesson/create/', {"title": "test"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response2 = self.client.post('/lesson/create/', {"title": "test", "url_video": "google.com"})
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_lesson(self):
        """Тест деталей модели Lesson"""
        self.test_lesson_create()
        response = self.client.get('/lesson/list/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(),
                         {"id": 1, "title": "test", "description": None, "image": None, "url_video": None,
                          "owner": None})

    def test_update_lesson(self):
        """Тест обновления Lesson"""
        self.test_lesson_create()
        response = self.client.patch(f'/lesson/list/update/4/', {"title": "test2"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(),
                         {"id": 4, "title": "test2", "description": None, "image": None, "url_video": None,
                          "owner": None})

    def test_lesson_delete(self):
        """Тест удаления урока"""
        self.test_lesson_create()
        response = self.client.delete('/lesson/list/delete/3/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
