from unittest import TestCase

from triangle_containment import calculate_equation, crosses_origin,contains_origin

point_1 = (-1, 3)
point_2 = (3, 11)

triangle = [(-340,495),(-153,-910),(835,-947)]
triangle_2 = [(-175,41),(-421,-714),(574,-645)]


class Test(TestCase):
    def test_calculate_equation(self):
        self.assertEqual(calculate_equation(point_1, point_2), (2, 5))

    def test_crosses_origin(self):
        self.assertEqual(crosses_origin(*calculate_equation(point_1, point_2)), (-2.5, 5))

    def test_contains_origin(self):
        self.assertTrue(contains_origin(triangle))
        self.assertFalse(contains_origin(triangle_2))
