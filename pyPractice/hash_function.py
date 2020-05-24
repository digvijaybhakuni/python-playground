# Hash function

import hashlib

def sha1(input):
  pass

def pbkdf2_password():
  dk = hashlib.pbkdf2_hmac('sha256', b'digvijay', b'thetestSalt', 10000) 
  hash_str = dk.hex()
  print(hash_str)


def main():
  pbkdf2_password()



if __name__ == '__main__':
  main()
