# me is this DAT.
# 
# scriptOp is the OP which is cooking.

import utils

def setupParameters(scriptOp):
	#scriptOp.appendParFloat('ValueA', page='Custom')
	#scriptOp.appendParFloat('ValueB', page='Custom')
	#scriptOp.appendParFloat('ValueC', page='Custom')
	return
val_list = op('Multiply').chans()
osc_comp = []
osc_layer = []
osc_clip = []	



osc_layer = utils.layer_fx(
	{
		'keystonemask': ['opacity']
	},
	[1, 2, 3, 4, 6]
)


osc_list = osc_layer 

	

# called whenever custom pulse parameter is pushed
def onPulse(par):
	scriptOp.clear()
	return

def cook(scriptOp):
	scriptOp.clear()
	# get input value
	[scriptOp.appendRow(name) for name in osc_list]
	scriptOp.appendCol()
	#print(osc_list)
	target = scriptOp

	
	target[0, 1] = val_list[0]
	target[1, 1] = val_list[1]
	target[2, 1] = val_list[0]
	target[3, 1] = val_list[1]
	target[4, 1] = val_list[3]
	#names[5][0] = val_list[1]
	return