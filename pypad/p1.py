x:int = 90

def test():
  x = 10
  def test2():
      nonlocal x
      x = 5
      print(x)
  test2() 
  print(x)

    

test()
print(x)
x = 'rahul'
print(x)
