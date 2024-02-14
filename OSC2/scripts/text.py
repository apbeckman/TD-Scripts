import random
import string

# me - this DAT
# scriptOp - the OP which is cooking
#
# press 'Setup Parameters' in the OP to call this function to re-create the parameters.
def onSetupParameters(scriptOp):
	page = scriptOp.appendCustomPage('Custom')
	p = page.appendFloat('Valuea', label='Value A')
	p = page.appendFloat('Valueb', label='Value B')
	return
address = '/composition/layers/5/clips/12/video/source/textgenerator/text/params/lines'



# called whenever custom pulse parameter is pushed
def onPulse(par):
	return

def onCook(scriptOp):
	scriptOp.clear()

	nums = [(int(x)) for x in op('nums').chans()]
	n = [str(x) for x in nums]
	matrix = ''.join(n)
	# letters = [chr(x) for x in nums
	# [letters.append(str(chr(int(x/2)+1))) for x in nums]

	# letters = [(str(chr(x)) for x in n)]
	#letters = [''.join(x) for x in n]

	scriptOp.appendCol()
	scriptOp.appendCol()
	scriptOp.appendRow()
	scriptOp[0, 0] = address

	scriptOp[0, 1] = matrix
	#scriptOp.copy(scriptOp.inputs[0])	# no need to call .clear() above when copying
	#scriptOp.insertRow(['color', 'size', 'shape'], 0)
	#scriptOp.appendRow(['red', '3', 'square'])
	#scriptOp[1,0] += '**'

	return
