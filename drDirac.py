import numpy as np
#P(knows the material | answers correctly)
#P(knows the material) = 0.60
#P(answers correctly | knows material) = 1 - 0.15
#P(knows material | answers correctly)
print(0.85*0.6/(0.85*0.6 + 0.2*0.4))