import utils_test

# Define input channels
val_list = op('highs').chans()

# Define indices and clips
layer_index = range(1, 7, 1)
clip_index = list(range(2, 3, 1))

# Define dictionaries for effects and parameters
comp_dict = {
    'bloom': {'amount': val_list[0]},
    'edge': {'basealpha': val_list[-1], 'exposure': val_list[2]},
    'shine': {'distance': 1.0 - val_list[2], 'intensity': val_list[3], 'falloff': val_list[3]*0.7 + val_list[2]*0.3}
}

layer_dict = {
    'edge': {'basealpha': val_list[0], 'exposure': val_list[3]}
}

clip_dict = {
    'bloom': {'amount': val_list[1]},
    'edge': {'basealpha': val_list[0]*0.6 + val_list[1]*0.4, 'exposure': val_list[3]*0.4 + val_list[2]*0.6},
    'shine': {'intensity': val_list[3], 'falloff': val_list[3]*0.7 + val_list[2]*0.3}
}

# Adding multiple instances of edge effect
[clip_dict.update({'edge{}'.format(str(x)): {'basealpha': val_list[0]}}) for x in ['', 1, 2, 3, 4]]



# Combine dictionaries


def setupParameters(scriptOp):
    scriptOp.clear()
    return


def onPulse(par):
    return


def cook(scriptOp):
    scriptOp.clear()
    # Generate addresses using dictionaries
    osc_clip = utils_test.clip_fx(clip_dict, clip_index, layer_index=[2, 3, 4, 5])
    osc_layer = utils_test.layer_fx(layer_dict, layer_index)
    osc_comp = utils_test.comp_fx(comp_dict) 
    osc_list = utils_test.dict_combine(osc_clip, osc_layer, osc_comp)
    [scriptOp.appendRow(name) for name in osc_list]
    scriptOp.appendCol()


    for name in osc_list:
        scriptOp[name, 1] = osc_list.get(name)

    return
