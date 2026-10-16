from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .forms import CourseForm
from .models import Course
User = get_user_model()
class CourseModelTests(TestCase):
    """Tests for the course database model """
    def text_course_is_saved_with_correct_details(self):
        #Arrange : prepare the course data 
        course = Course.objects.create(
            title="Django  Development",
            description="Django development description "            
        )
        
        #act: retrive the saved course
        saved_course = Course.objects.get(pk=course.pk)
        
        #Assert : Verify its stored details 
        self.assertEqual(saved_course.title,"Django  Development")
        self.assertEqual(saved_course.description,"Django development description ")
        self.assertEqual(str(saved_course),"Django  Development")


class CourseViewTests(TestCase):
    """Tests for course list and details page"""
    def setUp(self):
        self.course = Course.objects.create(
            title="python programming",
            description = "Learn python programming",
        )
    
    def text_course_list_returns_success(self):
        response = self.client.get(reverse("course_list"))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"python programming")
    
    def test_course_detail_displays_selected_course(self):
        url = reverse("course_detail",args=[self.course.pk])
        
        response =self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"python programming")
        self.assertContains(response,"Learn python programming")

class CourseFormTests(TestCase):
    """ Tests for valid and invalid course form data"""
    def test_valid_course_form(self):
        form_data = {
            "title":"Web Development",
            "description ":"Learn Web Development"
            
        }
        form = CourseForm(data = form_data)
        self.assertTrue(form.is_valid)
    def test_course_form_rejects_missing_title(self):
        form_data={
            "title":"",
            "description":"learn lksjdfjldf klsd " 
        }
        form = CourseForm(data = form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("title",form.errors)