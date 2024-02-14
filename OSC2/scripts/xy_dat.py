# me is this DAT.
#
# scriptOp is the OP which is cooking.
import utils
xyn = op('xy_noise').chans()
sv = op('bass_mids_mixed').chans()
h = op('hits_mixed').chans()
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
    layer_index = [2, 3, 5]
)

osc_layer = utils.layer_fx(
    {"isf-feedback-fugfeedbackgl": ["minvalue", "zoom"], "infinitezoom": "zoom"},
    layer_index = [1, 2, 3, 5, 6]
)

osc_comp = utils.comp_fx(
    {
        "shiftglitch": ["frequency", "size"],
        "stingysphere": ["extrusion", "noiseamount"],
        "infinitezoom": "zoom",
        "isf-feedback-fugfeedbackgl": ["minvalue", "zoom"],
        "distortion": ["distort", "radius"],
        "isf-distortion-shake": ["magnitude", "intensity"],
        "jabdisplacementfeedback(7.18.0+)": [
            "fbscalex",
            "fbscaley",
            "fbdisplacementintensity",
        ],
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
    # print(val_list)
    for name in osc_list:
        if "frequency" in name:
            target[name, 1] = xyn[0]
        elif "size" in name:
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

        elif "minvalue" in name:
            target[name, 1] = val_list[3]
        elif "magnitude" in name:
            target[name, 1] = h[1]
        elif "video/effects/i" in name:
            target[name, 1] = h[0]
        elif "effect/radius" in name:
            target[name, 1] = sv[0]
        elif "effect/distort" in name:
            target[name, 1] = h[0]
        # elif 'layer' not in name:
        # target[name, 1] = 0.5+val_list[1] * 0.5
        elif "fbscale" in name:
            target[name, 1] = sv[1]

        # else:
        # name[0] = val_list[1]

    return
