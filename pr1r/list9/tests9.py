from list9 import Rectangle, Polynomial, Urn
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.factor = 5
        self.rect1 = Rectangle(width=2, height=3)
        self.rect2 = Rectangle(width=3, height=2)
        self.rect3 = Rectangle(width=1, height=2)
        self.square = Rectangle(width=3, height=3)

    def test_area(self):
        self.assertEqual(self.rect1.area(), 6)
        self.assertEqual(self.rect2.area(), 6)
        self.assertEqual(self.rect3.area(), 2)
        self.assertEqual(self.square.area(), 9)

    def test_perim(self):
        self.assertEqual(self.rect1.perimeter(), 10)
        self.assertEqual(self.rect2.perimeter(), 10)
        self.assertEqual(self.rect3.perimeter(), 6)
        self.assertEqual(self.square.perimeter(), 12)

    def test_scale(self):
        self.assertEqual(self.rect1.scale(5), Rectangle(width=10, height=15))
        self.assertEqual(self.rect2.scale(self.factor), Rectangle(width=15, height=10))
        self.assertEqual(self.rect3.scale(self.factor), Rectangle(width=5, height=10))
        self.assertEqual(self.square.scale(self.factor), Rectangle(width=15, height=15))


class TestPolynomial(unittest.TestCase):
 
    def setUp(self):
        self.p1 = Polynomial([1, 1, 1])   # 1 + x + x^2
        self.p2 = Polynomial([0, 0, 1])   # x^2
        self.p3 = Polynomial([1, 2, 3])   # 1 + 2x + 3x^2
        self.p4 = Polynomial([0, 1])      # x
        self.p5 = Polynomial([0, 1, 0])   # x
        self.zero = Polynomial([0])
 
    def test_deg_basic(self):
        self.assertEqual(self.p1.deg(), 2)
        self.assertEqual(self.p4.deg(), 1)
        self.assertEqual(self.p5.deg(), 1)
 
    def test_deg_after_subtraction(self):
        result = (Polynomial([1, 1, 1]) - Polynomial([0, 0, 1])).deg()
        self.assertEqual(result, 1)
 
    def test_str(self):
        self.assertEqual(str(Polynomial([0])), "0")
        self.assertEqual(str(self.p1), "1 + 1x + 1x^2")
        self.assertEqual(str(self.p3), "1 + 2x + 3x^2")
        self.assertEqual(str(self.p5), "1x")
 
    def test_neg(self):
        neg = -self.p3
        self.assertEqual(neg, Polynomial([-1, -2, -3]))
 
    def test_add(self):
        result = self.p1 + self.p2
        self.assertEqual(result, Polynomial([1, 1, 2]))
 
    def test_add_different_lengths(self):
        result = self.p4 + self.p3   # x + (1+2x+3x^2) = 1+3x+3x^2
        self.assertEqual(result, Polynomial([1, 3, 3]))
 
    def test_sub(self):
        result = self.p1 - self.p2   # 1+x+x^2 - x^2 = 1+x
        self.assertEqual(result, Polynomial([1, 1]))
 
    def test_sub_self(self):
        result = self.p1 - self.p1
        self.assertEqual(result, Polynomial([0]))
 
    def test_mul(self):
        # (1+x) * (1+x) = 1+2x+x^2
        p = Polynomial([1, 1])
        self.assertEqual(p * p, Polynomial([1, 2, 1]))
 
    def test_mul_by_zero(self):
        self.assertEqual(self.p3 * self.zero, Polynomial([0]))
 
    def test_eq_true(self):
        self.assertEqual(Polynomial([1, 2]), Polynomial([1, 2]))
        self.assertNotEqual(self.p1, self.p2)
        self.assertEqual(Polynomial([1, 2, 0]), Polynomial([1, 2]))

    def test_call_zero(self):
        self.assertEqual(self.p3(0), 1)
        # 1 + 2 + 3 = 6
        self.assertEqual(self.p3(1), 6)
        # x^2 at x=3 → 9
        self.assertEqual(self.p2(3), 9)


class TestUrn(unittest.TestCase):
 
    def test_empty_init(self):
        u = Urn()
        self.assertEqual(u.total(), 0)
 
    def test_count(self):
        u = Urn({"red": 3, "blue": 2})
        self.assertEqual(u.count("red"), 3)
        self.assertEqual(u.count("blue"), 2)
 
    def test_add_new_color(self):
        u = Urn()
        u.add("green", 5)
        self.assertEqual(u.count("green"), 5)
 
    def test_add_existing_color(self):
        u = Urn({"red": 3})
        u.add("red", 2)
        self.assertEqual(u.count("red"), 5)
        u.add("blue")
        self.assertEqual(u.count("blue"), 1)
        self.assertEqual(u.count("green"), 0)
 
    def test_total_empty(self):
        self.assertEqual(Urn().total(), 0)
 
    def test_total(self):
        u = Urn({"red": 3, "blue": 2, "green": 5})
        self.assertEqual(u.total(), 10)
 
    def test_probability_empty(self):
        u = Urn()
        self.assertEqual(u.probability("red"), 0)
 
    def test_probability(self):
        u = Urn({"red": 3, "blue": 1})
        self.assertAlmostEqual(u.probability("red"), 0.75)
        self.assertAlmostEqual(u.probability("blue"), 0.25)
 
    def test_probability_same_color(self):
        u = Urn({"red": 4})
        self.assertAlmostEqual(u.probability("red"), 1.0)
 
    def test_str_nonempty(self):
        u = Urn({"blue": 2, "red": 3})
        s = "Urn(Counter({'red': 3, 'blue': 2}))"
        self.assertEqual(str(u), s)

if __name__ == "__main__":
    unittest.main()
