# me is this DAT.
#
# scriptOp is the OP which is cooking.

import addresses
osc_list = addresses.hca()
#val_list = xyn + sv
xyn = op('noisespeed').chans()
m=op('Multiply').chans()
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
    [scriptOp.appendRow(name) for name in osc_list]
    scriptOp.appendCol()
    target = scriptOp
    # print(val_list)
    for name in osc_list:
        if "interval" in name:
            scriptOp[name, 1] =0.6-m[0]
        elif "lines/r" in name:
            scriptOp[name, 1] = xyn[2]
    return
