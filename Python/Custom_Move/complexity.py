list = [0,1,2,3,4,5,6,7,8,9]
def _format():
	
	top = "{0:<4} {1:10} {2:>}".format("num:","nsquare","squaren")
	_under(top)
def _under(top):
	print(top)
	for items in top:
		print('_',end='')
	print('\n')
	_calculate()
	
def _calculate():
	for index, items in enumerate(list):
		nsquare = index**2
		squaren = 2**index
		
		out = "{0:<2} :  {1:6}|{2:>10}".format(index,nsquare,squaren)
		print(out)
		
_format()


##
