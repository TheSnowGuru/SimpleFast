import unittest
from src.main import compile_sfast_file

class TestSimpleFast(unittest.TestCase):
    def test_hello_world(self):
        # Compile the hello_world.sfast file
        compile_sfast_file('examples/hello_world.sfast')
        
        # If the compilation was successful, an executable named hello_world (or hello_world.exe on Windows) should exist.
        # We check for the existence of this file as a simple test.
        # This is a very basic test. In a real test suite, we would want to check the correctness of the compiled program,
        # not just whether it was compiled successfully.
        
        self.assertTrue(os.path.exists('examples/hello_world'))

if __name__ == '__main__':
    unittest.main()
