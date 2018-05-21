import base64, re
from Crypto.Cipher import AES
from Crypto import Random
import os
import random
import string

# para hash de autenticacion de usuarios
from passlib.context import CryptContext

PWD_CONTEXT = CryptContext(
        # Replace this list with the hash(es) you wish to support.
        # this example sets pbkdf2_sha256 as the default,
        # with additional support for reading legacy des_crypt hashes.
        schemes=["pbkdf2_sha256"],  # "des_crypt"],
        # Automatically mark all but first hasher in list as deprecated.
        # (this will be the default in Passlib 2.0)
        deprecated="auto",
        # Optionally, set the number of rounds that should be used.
        # Appropriate values may vary for different schemes,
        # and the amount of time you wish it to take.
        # Leaving this alone is usually safe, and will use passlib's defaults.
        ## pbkdf2_sha256__rounds = 29000,
    )

class AESCipher:
    """
      Usage:
      aes = AESCipher( settings.SECRET_KEY[:16], 32)
      encryp_msg = aes.encrypt( 'ppppppppppppppppppppppppppppppppppppppppppppppppppppppp' )
      msg = aes.decrypt( encryp_msg )
      print("'{}'".format(msg))
    """
    def __init__(self, key, blk_sz):
        self.key = key
        self.blk_sz = blk_sz

    def encrypt( self, raw ):
        if raw is None or len(raw) == 0:
            raise NameError("No value given to encrypt")
        raw = raw + '\0' * (self.blk_sz - len(raw) % self.blk_sz)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw ) ).decode('utf-8')

    def decrypt( self, enc ):
        if enc is None or len(enc) == 0:
            raise NameError("No value given to decrypt")
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return re.sub(b'\x00*$', b'', cipher.decrypt( enc[16:])).decode('utf-8')


class password_file:
    pwd_text = ""

    def get(self, filename):
        if self.pwd_text:
            return self.pwd_text
        if os.path.isfile(filename):
            with open(filename, "r") as f:
                self.pwd_text = "".join(f.readlines())
                return self.pwd_text
        else:
            self.pwd_text = self.get_random_chars(16)
            with open(filename, "w") as f:
                f.write(self.pwd_text)
                return self.pwd_text

    def get_random_chars(self, lenght):
        return ''.join(random.choice(string.ascii_letters) for x in range(lenght))