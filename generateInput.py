import numpy as np
import uproot
import os

os.system('mkdir -vp input')

dataFile=uproot.recreate('input/data.root')
dataFile['tree']={'number':np.ones(100)*0.5}
dataFile.close()

sigFile=uproot.recreate('input/sig.root')
sigFile['tree']={'number':[0.5]}
sigFile.close()
