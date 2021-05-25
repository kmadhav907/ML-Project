
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

def Img2Vector(filename):
    # Return matrix
    ret_val = np.zeros((1, 1024))
    # Read file's content
    file = open(filename)
    content = file.readlines()
    for i in range(32):
        line = content[i]
        for j in range(32):
            ret_val[0, 32 * i + j] = int(line[j])
    return ret_val
def test_your_image(file_name):
    sc_X = StandardScaler()

    loaded_model = pickle.load(open("E:/web/maithli/MLminiproj/finalized_model.sav", 'rb'))
    your_vector = Img2Vector(file_name)
    your_vector = sc_X.fit_transform(your_vector)
    your_vector = sc_X.transform(your_vector)

    result = loaded_model.predict(your_vector)
    return result[0]
