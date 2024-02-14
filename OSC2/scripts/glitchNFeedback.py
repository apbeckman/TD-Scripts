# me is this DAT.
#
# scriptOp is the OP which is cooking.
import utils
xyn = op('noisespeed').chans()
sv = op('Multiply').chans()
h = op('Average').chans()
f_n = op('fastnoise1').chans()
#val_list = xyn + sv
osc_clip = utils.clip_fx(
    {
        "shiftglitch": ["frequency", "size"],
        #'aceflow': 'speed',
        "distortion": ["distort", "radius"],
        #"stingysphere": ["extrusion", "noiseamount"],
        "jabdisplacementfeedback(7.18.0+)": [
            "fbscalex",
            "fbscaley",
            "fbdisplacementintensity",
        ],
    },
    clip_index=[2],
    layer_index = [2, 3, 4]
)

osc_layer = utils.layer_fx(
    {"isf-feedback-fugfeedbackgl": ["minvalue", "zoom"], "infinitezoom": ["zoom"]},
    layer_index = [1, 2, 3, 4, 6]
)

osc_comp = utils.comp_fx(
    {
        "isf-tile-softflip": ['angle'],
        "isf-tile-softflip2": ['angle'],
        "shiftglitch": ["frequency", "size", 'vertical', 'horizontal'],
        "stingysphere": ["extrusion", "noiseamount", "rotatex", "rotatey"],
        "infinitezoom": ["zoom"],
        "isf-feedback-fugfeedbackgl": ["minvalue", "zoom"],
        "distortion": ["distort", "radius"],
        "isf-distortion-shake": ["magnitude", "intensity"],
        "jabdisplacementfeedback(7.18.0+)": [
            "fbscalex",
            "fbscaley",
            "fbdisplacementintensity",
            'fbrotate',
        ],
        'repeater': ['xoff', 'yoff'],
        'blow':['x', 'y'],
    }
)
osc_list = utils.dict_combine(osc_clip, osc_layer, osc_comp)



def setupParameters(scriptOp):
    # scriptOp.appendParFloat('ValueA', page='Custom')
    # scriptOp.appendParFloat('ValueB', page='Custom')
    # scriptOp.appendParFloat('ValueC', page='Custom')
    return


# called whenever custom pulse parameter is pushed
def onPulse(par):
    return


def cook(scriptOp):
    scriptOp.clear()
    # get input value
  
    [scriptOp.appendRow(name) for name in osc_list.keys()]
    scriptOp.appendCol()
    target = scriptOp
    # assign values to effects
    for name in osc_list:
        if "frequency" in name:
            target[name, 1] = h[0]
        elif "size" in name:
            target[name, 1] = h[1]
        elif "vertical" in name:
            target[name, 1] = xyn[0]
        elif "horizontal" in name:
            target[name, 1] = xyn[1]
        elif "fbdisplacement" in name:
            target[name, 1] = h[0]
        elif "extrusion" in name:
            target[name, 1] = sv[0]
        elif "noise" in name:
            target[name, 1] = sv[1]
        elif "l/effect/zoom" in name:
            target[name, 1] = sv[0]
        elif "infinitezoom" in name:
            target[name, 1] = sv[0] 
        elif "minvalue" in name:
            target[name, 1] = sv[0]
        elif "rotatex" in name:
            target[name, 1] = xyn[2]
        elif "rotatey" in name:
            target[name, 1] = f_n[3]
        elif "xoff" in name:
            target[name, 1] = f_n[3]
        elif "yoff" in name:
            target[name, 1] = 1.0-f_n[0]
        elif "minvalue" in name:
            target[name, 1] = val_list[3]
        elif "magnitude" in name:
            target[name, 1] = h[1]
        elif "video/effects/isf" in name:
            target[name, 1] = h[0]
        elif "effect/radius" in name:
            target[name, 1] = sv[0]
        elif "effect/distort" in name:
            target[name, 1] = h[0]
        elif "fbrotate" in name:
            target[name, 1] = xyn[0]
        # elif 'layer' not in name:
        # target[name, 1] = 0.5+val_list[1] * 0.5
        elif "fbscale" in name:
            target[name, 1] = sv[1]
        elif name[-1] == 'x':
            target[name, 1] = f_n[3]
        elif name[-1] == 'y':
            target[name, 1] = f_n[0]

        # else:
        # name[0] = val_list[1]

    return
