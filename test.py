import unittest
from index_coordinates import cartesian_plane

class index_coordinates_test(unittest.TestCase):

	def test_closest_origin(self):
		origin = (1,2)
		closest_point = (20,16)
		index_distances = cartesian_plane(origin)
		self.assertEqual(sorted(index_distances, key=lambda k: k['distance'])[0]['value'], '20,16')

	def test_farthest_origin(self):
		origin = (2,1000)
		closest_point = (84,100)
		index_distances = cartesian_plane(origin)
		self.assertEqual(sorted(index_distances, key=lambda k: k['distance'])[-1]['value'], '84,100')

	def test_hello(self):
		str1 = "a"
		str2 = "aaaa"
		self.assertEqual(str1,str2)
		

if __name__ == '__main__':
    unittest.main()
