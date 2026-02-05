from django.test import TestCase
from django.urls import reverse


class TimeViewTests(TestCase):
    def test_time_page_loads(self):
        response = self.client.get(reverse('mytime:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Current time in Malaysia')
