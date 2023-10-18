from glsl_interpreter.la import Vec2
from unittest import TestCase, main


class Vec2Test(TestCase):
    def test_init(self):
        a = Vec2(69)
        b = Vec2(x=69)
        c = Vec2(42, 69)
        d = Vec2(x=42, y=69)

        self.assertEqual(a.x, 69)
        self.assertEqual(a.y, 69)

        self.assertEqual(b.x, 69)
        self.assertEqual(b.y, 69)

        self.assertEqual(c.x, 42)
        self.assertEqual(d.y, 69)

        self.assertEqual(c.x, 42)
        self.assertEqual(d.y, 69)


if __name__ == "__main__":
    main()
