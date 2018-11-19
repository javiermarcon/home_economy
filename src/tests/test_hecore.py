import mock
import unittest
import shutil, tempfile

from hecore.hecore import HecoreBackend

class FileExistsTest(unittest.TestCase):
    '''Verifica la funcionalidad de hecore'''

    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Remove the directory after the test
        shutil.rmtree(self.test_dir)

    @mock.patch('hecore.hecore.os.path.isfile')
    def test_file_exists_should_succeed(self, mock_isfile):
        mock_isfile.return_value = True
        spath = '/tmp/testfile.txt'
        hb = HecoreBackend()
        self.assertTrue(hb.check_file_exists(spath))

    @mock.patch('hecore.hecore.os.path.isfile')
    def test_file_exists_should_succeed(self, mock_isfile):
        mock_isfile.return_value = False
        spath = '/tmp/testfile.txt'
        hb = HecoreBackend()
        self.assertFalse(hb.check_file_exists(spath))

    # TODO: Crear test para launch de server.


    if __name__ == '__main__':
        unittest.main()
