import unittest
import time
from backend import app, db


header = {"Authorization": 'eyJ1c2VyX2lkIjoxLCJ1b2Z0X2VtYWlsIjoiZ3VpdGFyLmhlcm9AbWFpbC51dG9yb250by5jYSJ9.ZVEhJw.L8uu9748wABRiu7cpVo4U45Uzyg'}


class TestEnrollmentCartResponseTime(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_enrollment_cart_time(self):
        start_time = time.time()
        res = self.app.get('/enroll/', headers=header)
        end_time = time.time()

        duration = end_time - start_time
        print(f"Enrollment cart runtime: {duration} seconds")
        with self.assertRaises(ValueError):
            if duration < 0.3:
                raise ValueError("response time is " + str(duration) + " should be smaller that 0.3s (300 ms)")

