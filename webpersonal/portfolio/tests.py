from django.test import TestCase
import os
from .models import Project
from unittest.mock import MagicMock # Para simular un objeto sin tener que crearlo
from django.core.files import File

# Create your tests here.
class TestProject(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            title='Test Project',
            description='Test Description',
            image= 'projects/test-image.jpg',
            link='https://example.com'
            )
    def test_creation(self):
        self.assertEqual(Project.objects.count(), 1)
        self.assertEqual(self.project.title, 'Test Project')
        self.assertEqual(self.project.description, 'Test Description')
        self.assertEqual(self.project.link, 'https://example.com')
        self.assertTrue(os.path.basename(self.project.image.path), 'test-image.jpg')

    def test_str(self):
        self.assertEqual(str(self.project), 'Test Project')

    def test_ordering(self):
        project2 = Project.objects.create(
            title='Test Project 2',
            description='Test Description 2',
            image='projects/test-image.jpg',
            link='https://example2.com'
        )
        projects = list(Project.objects.all())
        self.assertEqual(projects[1], project2)
        self.assertEqual(projects[0], self.project)

    
    def test_delete(self):
        self.project.delete()
        self.assertEqual(Project.objects.count(), 0)
