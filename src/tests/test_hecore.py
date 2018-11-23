import mock
import unittest
import shutil, tempfile

from hecore.hecore import HecoreBackend

class FileExistsTest(unittest.TestCase):
    '''Verifica la funcionalidad de hecore'''

    def setUp(self):
        self.hb = HecoreBackend()
        self.spath = '/tmp/testfile.txt'


    @mock.patch('hecore.hecore.os.path.isfile')
    def test_file_exists_should_succeed(self, mock_isfile):
        mock_isfile.return_value = True
        self.assertTrue(self.hb.check_file_exists(self.spath))

    @mock.patch('hecore.hecore.os.path.isfile')
    def test_file_exists_should_fail(self, mock_isfile):
        mock_isfile.return_value = False
        spath = '/tmp/testfile.txt'
        self.assertFalse(self.hb.check_file_exists(self.spath))



    # TODO: Crear test para launch de server.


    if __name__ == '__main__':
        unittest.main()
