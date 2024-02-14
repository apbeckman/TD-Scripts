# me is this DAT.
# 
# scriptOp is the OP which is cooking.

# import utils
import addresses

val_list = op('mask_vals').chans()

#hardcoding addresses for speed params, fuck formatting these lol 
osc_list = addresses.speeds()


def setupParameters(scriptOp):

	return

# called whenever custom pulse parameter is pushed
def onPulse(par):
	return

def cook(scriptOp):
	scriptOp.clear()

	 
	[scriptOp.appendRow(name) for name in osc_list.keys()]
	scriptOp.appendCol()


	# assign out channels
	scriptOp[0, 1] = (val_list[1])
	scriptOp[1, 1] = val_list[0]
	scriptOp[2, 1] = val_list[1] * 0.1
	scriptOp[3, 1] = val_list[1] * 0.5
	scriptOp[4, 1] = val_list[1] * 0.5
	scriptOp[5, 1] = val_list[1] * 0.5
	scriptOp[6, 1] = val_list[0] * 0.5
	scriptOp[7, 1] = val_list[1]
	scriptOp[8, 1] = val_list[0]
	scriptOp[9, 1] = val_list[1]
	return
