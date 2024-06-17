from zynet import zynet
from zynet import utils
import numpy as np

def genMnistZynet(dataWidth,sigmoidSize):
    model = zynet.model()

    model.add(zynet.layer("flatten", 188))
    model.add(zynet.layer("Dense",512,"elu"))
    model.add(zynet.layer("Dense",256,"elu"))
    model.add(zynet.layer("Dense",128,"elu"))
    model.add(zynet.layer("Dense", 12,"elu"))

    weightArray = utils.genWeightArray('WeigntsAndBiasesSigmoid.txt')
    biasArray   = utils.genBiasArray('WeigntsAndBiasesSigmoid.txt')

    model.compile(pretrained    = 'Yes', 
		  weights       = weightArray,
                  biases        = biasArray, 
                  dataWidth     = dataWidth,
                  sigmoidSize   = sigmoidSize,
                  weightIntSize = 4,
                  inputIntSize  = 1 )
    
    zynet.makeXilinxProject('MLP_Project','xc7z020clg484-1')
    zynet.makeIP('MLP_Project')
    zynet.makeSystem('MLP_Project','MLP_Block')
    
if __name__ == "__main__":
    genMnistZynet(dataWidth=31,sigmoidSize=5)
