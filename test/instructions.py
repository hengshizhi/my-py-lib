from lib import instructions

tc = instructions.call(lambda x,b,c:(x+1,b,c),{'x','b','c'})
ti = instructions.instructions({'x':114514})
ti.add('plus',tc)
print('返回值:',ti.run_instructions('plus',{'b':'lovekeqing'}))