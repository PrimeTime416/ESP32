print('**** Imported: BitWisePlay.py')


def bitwise_and_bytes(x, y=b'\x01', byteX=1, inden='little'):
    andX = int.from_bytes(x, inden) & int.from_bytes(y, inden)
    return int(andX).to_bytes(byteX,inden)

def invertBytes(x, byteX=1, inden='little'):
  x = int(~x).to_bytes(byteX,inden)
  return x 


  # ******************************* PLAY ******************************

  

inden='little'
x = invertBytes(0)

#print()
# print('{}:  {}: {}'.format(bin(int.from_bytes(x, inden)), x, int.from_bytes(x, inden)))
# print('{}'.format(bitwise_and_bytes(x, b'\x03')))

class Person:
  x = 5

p1 = Person()
# print(Person)
# print(p1.x)

print(type(Person))
print(type(p1))