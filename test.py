# Script for automatic testing of hello.py
import subprocess

def test():
  proc = subprocess.Popen(['python3', 'hello.py',  ''], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  res = proc.communicate()[0].decode("utf-8").strip()
  print("Result:", res)
  if res != "Hello, world.":
    print("Test Fail!")
    assert False
  else:
    print("Test Pass!")  

if __name__ == '__main__':
    test()
