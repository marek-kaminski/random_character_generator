import sys
from unittest import TestCase

#example "hello word" test #

class Evaluate(TestCase):
    def test_hello_world(self):
        import exercise  # Imports and runs student's solution
        output = sys.stdout.getvalue()  # Returns output since this function started
        self.assertEqual("Hello World\n", output, "You must print Hello World")

