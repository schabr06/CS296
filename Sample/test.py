import disassembler
def f(x,y):
  def g(x,y):
    if x < 1:
      return y
    else:
      return f(y-1,x)
  return g(x,y)
def main():
  print(f(5,12)) 
#main()
disassembler.disassemble(f)
disassembler.disassemble(main)