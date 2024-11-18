from django.test import TestCase
from .models import Experience
import os
# Create your tests here.
class TestProject(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title='Test Experience',
            description='Test Description',
            image='experiences/test-image.jpg',
            date_started='2020-01-01',
            date_ended='2020-01-02'
            )
    def test_creation(self):
        self.assertEqual(Experience.objects.count(), 1)
        self.assertEqual(self.experience.title, 'Test Experience')
        self.assertEqual(self.experience.description, 'Test Description')
        self.assertTrue(os.path.basename(self.experience.image.path), 'test-image.jpg')
        self.assertEqual(self.experience.date_started, '2020-01-01')
        self.assertEqual(self.experience.date_ended, '2020-01-02')

    def test_str(self):
        self.assertEqual(str(self.experience), 'Test Experience')

    def test_ordering(self):
        experience2 = Experience.objects.create(
            title='Test Experience 2',
            description='Test Description 2',
            image='experiences/test-image-2.jpg',
            date_started='2020-03-01',
            date_ended='2020-04-02'
        )
        projects = list(Experience.objects.all())
        self.assertEqual(projects[0], experience2)
        self.assertEqual(projects[1], self.experience)

    
    def test_delete(self):
        self.experience.delete()
        self.assertEqual(Experience.objects.count(), 0)
