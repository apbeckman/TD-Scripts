import utils_test

m = op("Multiply")
pv = op("position_vals")
sv = op("speedvals")
v_s = op("noisespeed")
h = op("highs")
presence = op("presence")[-1]
clip_index = range(2, 4, 5)
extra_clips = [2, 3, 4, 5, 6]

extra_effects = {
    "kaleidofx": {"shiftx": pv[-1], "shifty": v_s[1]},
    "kaleidofx2": {"shiftx": v_s[0], "shifty": v_s[1]},
    "kaleidofx3": {"shiftx": v_s[0], "shifty": v_s[1]},
    "droste": {"offset": pv[1]},
    "mosaic": {"posx": pv[-1], "posy": pv[-2]},
    "fractaldisplace": {"rotation": pv[-5]},
    "fractaldisplace2": {"rotation": pv[-1]},
    "fractaldisplace3": {"rotation": pv[-2]},
    "fractaldisplace4": {"rotation": pv[-4]},
    "fractaldisplace5": {"rotation": pv[-3]},
    "shine": {"intensity": h[0]},
}

clip_dict = {
    "edge": {"basealpha": h[0]},
    "warpspeed": {"rotate": v_s[2]},
    "mosaic": {"posx": pv[3], "posy": pv[2]},
}

source_dict = {
    "sinewave": {"modulator": pv[-1], "modulationdepth": m[0]},
}

def cook(scriptOp):
    scriptOp.clear()

    source_fx = utils_test.address_generator(
        source_dict, clip_index=[2, 5, 6], layer_index=[1, 5]
    )

    xtra = utils_test.clip_fx(extra_effects, extra_clips, layer_index=[1, 5])

    osc_clip = utils_test.clip_fx(clip_dict, clip_index, layer_index=[1, 2, 3, 4, 5, 6])

    osc_list = utils_test.dict_combine(osc_clip, xtra, source_fx)

    for name in osc_list:
        scriptOp.appendRow(name)

    scriptOp.appendCol()

    for name in osc_list:
        scriptOp[name, 1] = osc_list.get(name)

    return
