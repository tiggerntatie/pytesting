# Script for automatic testing of hello.py
import subprocess

def test():
  proc = subprocess.Popen(['python', 'hello.py',  ''], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  res = proc.communicate()[0]
  if res != "Hello, world.":
    assert False
