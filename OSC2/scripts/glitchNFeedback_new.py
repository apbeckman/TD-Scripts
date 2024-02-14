import utils_test

xyn = op('noisespeed').chans()
sv = op('Multiply').chans()
h = op('Average').chans()
f_n = op('fastnoise').chans()

# Define the dictionaries for address generators
clip_fx = {
    "effect_dict": {
        "shiftglitch": {"frequency": h[0], "size": h[1]},
        "distortion": {"distort": sv[0], "radius": sv[0]},
        "jabdisplacementfeedback(7.18.0+)": {"fbscalex": sv[1], "fbscaley": sv[1], "fbdisplacementintensity": h[0]},
    },
    "clip_index": [2],
    "layer_index": [2, 3, 4]
}

layer_fx = {
    "effect_dict": {
        "isf-feedback-fugfeedbackgl": {"minvalue": sv[0], "zoom": sv[0]},
        "infinitezoom": {"zoom": sv[0]},
    },
    "layer_index": [1, 2, 3, 4, 6]
}

comp_fx = {
    "effect_dict": {
        "isf-tile-softflip": {'angle': xyn[0]},
        "isf-tile-softflip2": {'angle': xyn[1]},

        "shiftglitch": {"frequency": h[0], "size": h[1], 'vertical': xyn[0], 'horizontal': xyn[1]},
        "stingysphere": {"extrusion": sv[0], "noiseamount": sv[1], "rotatex": xyn[2], "rotatey": f_n[3]},
        "infinitezoom": {"zoom": sv[0]},
        "isf-feedback-fugfeedbackgl": {"minvalue": sv[0], "zoom": sv[0]},
        "distortion": {"distort": sv[0], "radius": sv[0]},
        "isf-distortion-shake": {"magnitude": h[1], "intensity": h[0]},
        "jabdisplacementfeedback(7.18.0+)": {"fbscalex": sv[1], "fbscaley": sv[1], "fbdisplacementintensity": h[0], 'fbrotate': xyn[0]},
        'repeater': {'xoff': f_n[3], 'yoff': 1.0 - f_n[0]},
        'blow': {'x': f_n[3], 'y': f_n[0]},
    }
}

def setupParameters(scriptOp):
    return

def onPulse(par):
    return

def cook(scriptOp):
    scriptOp.clear()

    # Call the address generator methods
    osc_clip = utils_test.clip_fx(**clip_fx)
    osc_layer = utils_test.layer_fx(**layer_fx)
    osc_comp = utils_test.comp_fx(**comp_fx)

    # Combine the results
    osc_list = utils_test.dict_combine(osc_clip, osc_layer, osc_comp)

    [scriptOp.appendRow(name) for name in osc_list.keys()]
    scriptOp.appendCol()
    target = scriptOp

    for name in osc_list.items():
        scriptOp.appendRow(name)
    
    scriptOp.appendCol()

    for name, value in osc_list.items():
        scriptOp[name, 1] = value


    return
