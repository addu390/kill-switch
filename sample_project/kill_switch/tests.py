from django.test import TestCase


class SampleTest(TestCase):

    def test_ls(self):
        result = "ACTIVE"
        self.assertEqual("ACTIVE", result)
