from unittest import TestCase
import password


class TestPasswordGenerator(TestCase):
    def test_passwordGenerator_length(self):
        pass1 = password.passwordGenerator(3)
        self.assertEqual(3, len(pass1))

    def test_passwordGenerator_notSame(self):
        pass1 = password.passwordGenerator(3)
        pass2 = password.passwordGenerator(3)
        self.assertNotEqual(pass1, pass2)
