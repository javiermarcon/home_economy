import unittest
import shutil, tempfile
from os import path

from hecore.hecore import HecoreBackend

class FileExistsTest(unittest.TestCase):
    '''Verifica la funcionalidad de hecore'''

    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Remove the directory after the test
        shutil.rmtree(self.test_dir)

    def test_file_exists(self):
        spath = path.join(self.test_dir, 'test.txt')
        hb = HecoreBackend()
        # Check that file exists
        self.assertFalse(hb.check_file_exists(spath))
        # Create the file in the temporary directory
        f = open(spath, 'w')
        f.write('The owls are not what they seem')
        f.flush()
        f.close()
        # Check that file does not exist
        self.assertTrue(hb.check_file_exists(spath))

    # TODO: Crear test para launch de server.


    if __name__ == '__main__':
        unittest.main()
