import utils_test

# Define input channels
pv = op("position_vals")
sv = op("speedvals")
v_s = op("noisespeed").chans()
h = op("highs").chans()

# Define indices and clips
clip_index = range(2, 4, 5)
extra_clips = [2, 3, 4, 5, 6]

# Define dictionaries for effects and parameters
extra_effects = {
    "kaleidofx": {"shiftx": v_s[0], "shifty": v_s[1]},
    "kaleidofx2": {"shiftx": v_s[0], "shifty": v_s[1]},
    "kaleidofx3": {"shiftx": v_s[0], "shifty": v_s[1]},
    "droste": {"offset": pv[4]},
    "mosaic": {"posx": pv[3], "posy": pv[2]},
    "fractaldisplace": {"rotation": v_s[2]},
    "shine": {"intensity": h[0]},
}

clip_dict = {
    "edge": {"basealpha": h[0]},
    "warpspeed": {"rotate": v_s[2]},
    "mosaic": {"posx": pv[3], "posy": pv[2]},
    "fractaldisplace": {'rotate': pv[-3]},
    "fractaldisplace2": {'rotate': pv[-1]},
    "fractaldisplace3": {'rotate': pv[-2]},
}

source_dict = {
    "sinewave": {"modulatorspeed": sv[1], "mainspeed": sv[2]},
}

# Generate addresses using dictionaries
source_fx = utils_test.address_generator(source_dict, clip_index=[5, 6], layer_index=[1, 5])
xtra = utils_test.clip_fx(extra_effects, extra_clips, layer_index=[1, 5])
osc_clip = utils_test.clip_fx(clip_dict, clip_index, layer_index=[2, 3, 4, 5, 6])

# Combine dictionaries
osc_list = utils_test.dict_combine(osc_clip, xtra, source_fx)


def onPulse(par):
    op("scriptOp").clear()
    return


def cook(scriptOp):
    scriptOp.clear()
    [scriptOp.appendRow(name) for name in osc_list]
    scriptOp.appendCol()
    for name, value in osc_list.items():
        scriptOp[name, 1] = value

    return
