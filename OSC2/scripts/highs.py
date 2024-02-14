# me is this DAT.
# 
# scriptOp is the OP which is cooking.
import utils

val_list = op('highs').chans()

layer_index = range(1, 7, 1)
clip_index = list(range(2, 3, 1))

comp_dict = {
        'bloom': ['amount'],
        'edge': ['basealpha'],
        'edge2': ['basealpha'],
        'shine': ['distance', 'intensity']
        }
layer_dict = {
        'edge': ['basealpha', 'exposure']
        }
clip_dict = {
        'bloom': ['amount'],
        'bloom2': ['amount'],
        'edge': ['basealpha'],
        'edge': ['basealpha'],
        'shine': ['intensity', 'falloff'],
        'shine2': ['intensity', 'falloff']	    	
    }
#adding multiple instances of edge effect


[clip_dict.update({'edge{}'.format(str(x)): ['basealpha']}) for x in [1, 2, 3, 4]]

osc_clip = utils.clip_fx(
    clip_dict,
    clip_index,
    layer_index = [2, 3, 4, 5]
    )

osc_layer = utils.layer_fx(
    layer_dict, layer_index
)

osc_comp = utils.comp_fx(
        comp_dict
)
osc_list = utils.dict_combine(osc_clip, osc_layer, osc_comp)

# get input value


def setupParameters(scriptOp):
	#scriptOp.appendParFloat('ValueA', page='Custom')
	#scriptOp.appendParFloat('ValueB', page='Custom')
	#scriptOp.appendParFloat('ValueC', page='Custom')
	scriptOp.clear()
	
	return

# called whenever custom pulse parameter is pushed
def onPulse(par):

	return

def cook(scriptOp):
    scriptOp.clear()
    [scriptOp.appendRow(name) for name in osc_list]
    scriptOp.appendCol()
	


	#names[0][0] = val_list[0]
	#names[1][0] = val_list[1]
	#names[2][0] = val_list[0]* 0.5 + val_list[1] * 0.5
	#names[3][0] = val_list[1] * 0.5 + val_list[2] * 0.5
	#names[4][0] = val_list[2]
    for name in osc_list:
        if 'basealpha' in name:
            scriptOp[name, 1] = val_list[0]
        elif 'bloom' in name:
            scriptOp[name, 1] = val_list[1]
        elif 'edge2' in name:
            scriptOp[name, 1] = val_list[2]*0.6 + val_list[1]*0.4
        elif 'edge3' in name:
            scriptOp[name, 1] = val_list[1]*0.6 + val_list[2]*0.4
        elif 'intensity' in name:
            scriptOp[name, 1] = val_list[3]
        elif 'falloff' in name:
            scriptOp[name, 1] = val_list[3]*0.7 + val_list[2]*0.3
        elif 'exposure' in name:
            scriptOp[name, 1] = val_list[3]*0.4 + val_list[2]*0.6		
        elif 'distance' in name:
            scriptOp[name, 1] = 1.0-val_list[2]		
        

		
		
		#else:
			#name[0] = val_list[1]

    return