import math
import svgcuts
import unittest

class LineTests(unittest.TestCase) :
	def test_linelen(self) :
		p1 = svgcuts.Point(0,0)
		p2 = svgcuts.Point(2,3)
		l = svgcuts.Line(p1, p2)
		self.assertAlmostEqual(l.length, 3.60555127546398929312)

	"""
	looks like: x
	"""
	def test_crosses1(self) :
		p1 = svgcuts.Point(0,0)
		p2 = svgcuts.Point(1,1)
		p3 = svgcuts.Point(0,1)
		p4 = svgcuts.Point(1,0)
		l1 = svgcuts.Line(p1,p2)
		l2 = svgcuts.Line(p3,p4)
		self.assertTrue(l1.intersects(l2))
		self.assertTrue(l2.intersects(l1))

	"""
	looks like:
	|
	|
	"""
	def test_aligned_vert_nonintersect(self) :
		p1 = svgcuts.Point(0,0)
		p2 = svgcuts.Point(0,1)
		p3 = svgcuts.Point(0,2)
		p4 = svgcuts.Point(0,3)
		l1 = svgcuts.Line(p1,p2)
		l2 = svgcuts.Line(p3,p4)
		self.assertFalse(l1.intersects(l2))
		self.assertFalse(l2.intersects(l1))

	"""
	looks like: --
	"""
	def test_aligned_hor_nonintersect(self) :
		p1 = svgcuts.Point(0,0)
		p2 = svgcuts.Point(1,0)
		p3 = svgcuts.Point(2,0)
		p4 = svgcuts.Point(3,0)
		l1 = svgcuts.Line(p1,p2)
		l2 = svgcuts.Line(p3,p4)
		self.assertFalse(l1.intersects(l2))
		self.assertFalse(l2.intersects(l1))

	"""
	looks like: +
	"""
	def test_crosses2(self) :
		p1 = svgcuts.Point(1,0)
		p2 = svgcuts.Point(1,2)
		p3 = svgcuts.Point(0,1)
		p4 = svgcuts.Point(2,1)
		l1 = svgcuts.Line(p1,p2)
		l2 = svgcuts.Line(p3,p4)
		self.assertTrue(l1.intersects(l2))
		self.assertTrue(l2.intersects(l1))

	"""
	looks like: |
		   __
	"""
	def test_crosses2a(self) :
		p1 = svgcuts.Point(0,0)
		p2 = svgcuts.Point(2,0)
		p3 = svgcuts.Point(1,1)
		p4 = svgcuts.Point(1,2)
		l1 = svgcuts.Line(p1,p2)
		l2 = svgcuts.Line(p3,p4)
		self.assertFalse(l1.intersects(l2))
		self.assertFalse(l2.intersects(l1))

	"""
	looks like: //
	"""
	def test_crosses3(self) :
		p1 = svgcuts.Point(0,0)
		p2 = svgcuts.Point(2,3)
		p3 = svgcuts.Point(1,1)
		p4 = svgcuts.Point(3,4)
		l1 = svgcuts.Line(p1,p2)
		l2 = svgcuts.Line(p3,p4)
		self.assertFalse(l1.intersects(l2))
		self.assertFalse(l2.intersects(l1))


	"""
	looks like: / (2 on top of each other)
	"""
	def test_crosses3a(self) :
		p1 = svgcuts.Point(0,0)
		p2 = svgcuts.Point(2,3)
		p3 = svgcuts.Point(0,0)
		p4 = svgcuts.Point(2,3)
		l1 = svgcuts.Line(p1,p2)
		l2 = svgcuts.Line(p3,p4)
		self.assertTrue(l1.intersects(l2))
		self.assertTrue(l2.intersects(l1))

	"""
	looks like: ||
	"""
	def test_crosses4(self) :
		p1 = svgcuts.Point(0,0)
		p2 = svgcuts.Point(0,3)
		p3 = svgcuts.Point(1,0)
		p4 = svgcuts.Point(1,3)
		l1 = svgcuts.Line(p1,p2)
		l2 = svgcuts.Line(p3,p4)
		self.assertFalse(l1.intersects(l2))
		self.assertFalse(l2.intersects(l1))

	"""
	looks like: | (two of them on top of each other)
	"""
	def test_crosses5(self) :
		p1 = svgcuts.Point(0,0)
		p2 = svgcuts.Point(0,3)
		p3 = svgcuts.Point(0,0)
		p4 = svgcuts.Point(0,3)
		l1 = svgcuts.Line(p1,p2)
		l2 = svgcuts.Line(p3,p4)
		self.assertTrue(l1.intersects(l2))
		self.assertTrue(l2.intersects(l1))

	def test_slope_offset(self) :
		s,i = svgcuts.Line(svgcuts.Point(1,1), svgcuts.Point(2,3)).slope_offset
		self.assertAlmostEqual(s, 2.0)
		self.assertAlmostEqual(i, -1.0)
		s,i = svgcuts.Line(svgcuts.Point(1,1), svgcuts.Point(3,4)).slope_offset
		self.assertAlmostEqual(s, 1.5)
		self.assertAlmostEqual(i, -0.5)

	def test_angle(self) :
		self.assertAlmostEqual(svgcuts.Line(svgcuts.Point(0,0), svgcuts.Point(1,1)).angle, math.pi / 4.0)
		self.assertAlmostEqual(svgcuts.Line(svgcuts.Point(0,0), svgcuts.Point(0,1)).angle, math.pi / 2.0)
		self.assertAlmostEqual(svgcuts.Line(svgcuts.Point(0,0), svgcuts.Point(0,-1)).angle, math.pi / -2.0)
		self.assertAlmostEqual(svgcuts.Line(svgcuts.Point(0,0.5), svgcuts.Point(1,1)).angle, 0.46364760900080609)
		self.assertAlmostEqual(svgcuts.Line(svgcuts.Point(0,0), svgcuts.Point(-1,1)).angle, math.pi * 3.0 / 4.0)
		self.assertAlmostEqual(svgcuts.Line(svgcuts.Point(0,0), svgcuts.Point(-1,-1)).angle, math.pi * -3.0 / 4.0)
		self.assertAlmostEqual(svgcuts.Line(svgcuts.Point(0,0), svgcuts.Point(1, 0)).angle, 0.0)
		self.assertAlmostEqual(svgcuts.Line(svgcuts.Point(0,0), svgcuts.Point(1, -1)).angle, math.pi * -1.0 / 4.0)

	def test_incidental_angle_with_common_points(self) :
		l1 = svgcuts.Line(svgcuts.Point(1,1), svgcuts.Point(2, 2))
		l2 = svgcuts.Line(svgcuts.Point(1,1), svgcuts.Point(0, 2))
		self.assertAlmostEqual(l1.incident_angle(l2), math.pi / 2.0)

		l1 = svgcuts.Line(svgcuts.Point(1,1), svgcuts.Point(2, 2))
		self.assertAlmostEqual(l1.incident_angle(l1), 0.0)

		l1 = svgcuts.Line(svgcuts.Point(2,2), svgcuts.Point(1,1))
		l2 = svgcuts.Line(svgcuts.Point(2,2), svgcuts.Point(3, 2))
		self.assertAlmostEqual(l1.incident_angle(l2), math.pi * 3.0 / 4.0) 
		l1 = svgcuts.Line(svgcuts.Point(1,1), svgcuts.Point(2,2))
		self.assertAlmostEqual(l1.incident_angle(l2), math.pi * 3.0 / 4.0)

	"""
	   _
	  _
	/ _
	"""
	def test_incidental_angle_without_common_points(self) :
		l1 = svgcuts.Line(svgcuts.Point(0,2), svgcuts.Point(2,4))
		l2 = svgcuts.Line(svgcuts.Point(4,5), svgcuts.Point(5,5))
		l3a = svgcuts.Line(svgcuts.Point(3,3.999), svgcuts.Point(4,3.999))
		l3b = svgcuts.Line(svgcuts.Point(3,4), svgcuts.Point(4,4))
		l3c = svgcuts.Line(svgcuts.Point(3,4.001), svgcuts.Point(4,4.001))
		l4 = svgcuts.Line(svgcuts.Point(3,3), svgcuts.Point(4,3))
		l5 = svgcuts.Line(svgcuts.Point(1,2), svgcuts.Point(3,4))
		self.assertAlmostEqual(l1.incident_angle(l2), math.pi * 3.0 / 4.0)
		# TODO add ones for l3*
		self.assertAlmostEqual(l1.incident_angle(l4), math.pi * 1.0 / 4.0)
		# incident angle should be pi, even if they never touch..?
		self.assertAlmostEqual(l1.incident_angle(l5), math.pi)

	def test_closest_distance_1(self) :
		l1 = svgcuts.Line(svgcuts.Point(0,2), svgcuts.Point(2,4))
		l2 = svgcuts.Line(svgcuts.Point(4,5), svgcuts.Point(5,5))
		self.assertAlmostEqual(l1.closest_distance(l2), math.sqrt(5))
		self.assertAlmostEqual(l2.closest_distance(l1), math.sqrt(5))

	def test_closest_distance_2(self) :
		l1 = svgcuts.Line(svgcuts.Point(1,2), svgcuts.Point(1,3))
		l2 = svgcuts.Line(svgcuts.Point(3,3.5), svgcuts.Point(5,1.5))
		self.assertAlmostEqual(l1.closest_distance(l2), math.sqrt(4 + math.pow(0.5, 2)))
		self.assertAlmostEqual(l2.closest_distance(l1), math.sqrt(4 + math.pow(0.5, 2)))

	def test_closest_distance_3(self) :
		l1 = svgcuts.Line(svgcuts.Point(1,1), svgcuts.Point(1,3))
		l2 = svgcuts.Line(svgcuts.Point(4,3), svgcuts.Point(2,1.5))
		self.assertAlmostEqual(l1.closest_distance(l2), 1.0)
		self.assertAlmostEqual(l2.closest_distance(l1), 1.0)

	def test_closest_distance_4(self) :
		l1 = svgcuts.Line(svgcuts.Point(0,1), svgcuts.Point(1,2))
		l2 = svgcuts.Line(svgcuts.Point(1,4), svgcuts.Point(3,2))
		self.assertAlmostEqual(l2.closest_distance(l1), math.sqrt(2))
