import unittest
import coords_rectangle
class Test(unittest.TestCase):
    #def test_myfirsttest1(self):
     #   self.assertEqual(2+3, 5)      #метод который который проевряет что два объекат равны
    def test_within_x_true(self):   
        co1 = coords_rectangle.Coords(x1=7, y1=1, x2=9, y2=3)
        co2 = coords_rectangle.Coords(x1=4, y1=4, x2=10, y2=6)
        self.assertTrue(coords_rectangle.within_x(co1, co2))

    def test_within_x_false(self):
        co1 = coords_rectangle.Coords(x1=13, y1=2, x2=15, y2=5)
        co2 = coords_rectangle.Coords(x1=4, y1=4, x2=10, y2=6)
        self.assertFalse(coords_rectangle.within_x(co1, co2))  

    def test_within_y_true(self):   
        co1 = coords_rectangle.Coords(x1=13, y1=2, x2=15, y2=5)
        co2 = coords_rectangle.Coords(x1=4, y1=4, x2=10, y2=6)
        self.assertTrue(coords_rectangle.within_y(co1, co2))

    def test_within_y_false(self):   
        co1 = coords_rectangle.Coords(x1=7, y1=1, x2=9, y2=3)
        co2 = coords_rectangle.Coords(x1=4, y1=4, x2=10, y2=6)
        self.assertFalse(coords_rectangle.within_y(co1, co2))

    def test_collided_left_true(self):
        co1 = coords_rectangle.Coords(x1=10, y1=2, x2=12, y2=5)
        co2 = coords_rectangle.Coords(x1=4, y1=4, x2=10, y2=6)
        self.assertTrue(coords_rectangle.collided_left(co1, co2))

    def test_collided_right_true(self):
        co1 = coords_rectangle.Coords(x1=2, y1=2, x2=4, y2=5)
        co2 = coords_rectangle.Coords(x1=4, y1=4, x2=10, y2=6)
        self.assertTrue(coords_rectangle.collided_right(co1, co2))

    def test_collided_left_false_side(self):
        co1 = coords_rectangle.Coords(x1 = 13, y1 = 2, x2 = 15, y2 = 5)
        co2 = coords_rectangle.Coords(x1 = 4, y1 = 4, x2 = 10, y2 = 6)
        self.assertFalse(coords_rectangle.collided_left(co1, co2))

    def test_collided_left_false_up(self):
        co1 = coords_rectangle.Coords(x1 = 7, y1 = 1, x2 = 9, y2 = 3)
        co2 = coords_rectangle.Coords(x1 = 4, y1 = 4, x2 = 10, y2 = 6)
        self.assertFalse(coords_rectangle.collided_left(co1, co2))

    def test_collided_right_false_up(self):
        co1 = coords_rectangle.Coords(x1 = 7, y1 = 1, x2 = 9, y2 = 3)
        co2 = coords_rectangle.Coords(x1 = 4, y1 = 4, x2 = 10, y2 = 6)
        self.assertFalse(coords_rectangle.collided_right(co1, co2))

    def test_collided_right_false_side(self):
        co1 = coords_rectangle.Coords(x1 = 1, y1 = 2, x2 = 3, y2 = 5)
        co2 = coords_rectangle.Coords(x1 = 4, y1 = 4, x2 = 10, y2 = 6)
        self.assertFalse(coords_rectangle.collided_right(co1, co2))

    def test_collided_right_false_inleftside(self):
        co1 = coords_rectangle.Coords(x1=10, y1=2, x2=12, y2=5)
        co2 = coords_rectangle.Coords(x1=4, y1=4, x2=10, y2=6)
        self.assertFalse(coords_rectangle.collided_right(co1, co2))
    
    def test_collided_top_true(self):
        co1 = coords_rectangle.Coords(x1 = 6, y1 = 5, x2 = 8, y2 = 7)
        co2 = coords_rectangle.Coords(x1 = 4, y1 = 4, x2 = 10, y2 = 6)
        self.assertTrue(coords_rectangle.collided_top(co1, co2))
    
    def test_collided_top_false_side(self):
        co1 = coords_rectangle.Coords(x1 = 12, y1 = 5, x2 = 14, y2 = 7)
        co2 = coords_rectangle.Coords(x1 = 4, y1 = 4, x2 = 10, y2 = 6)
        self.assertFalse(coords_rectangle.collided_top(co1, co2))

    

unittest.main()




 
