class encap:
  _a=10
  c=12
  def encapfunction(self):
    _b=30
    print("encap function accessing protected")
    print(self._a+10)
obj=encap()
print(obj._a)
obj.encapfunction()
print(obj.c)
