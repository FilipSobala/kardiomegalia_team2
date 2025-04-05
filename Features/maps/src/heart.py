STATE_PATH = 'labelki.csv'

def get_state(id, path):
    with open(path, 'r') as f:
        dump = f.readline()  # Skip the first line (header)
        raw = f.readlines()

    lables = {}
    for line in raw:
        line = line.strip("\n")
        split = line.split(',')
        lables[split[0]] = bool(split[1] == '1')

    #print(lables)
    return lables[str(id)]
    

class Heart():
    def __init__(self,img, id, state:bool,img_res=(512, 512), features={}):
        self.id = id
        self.img = img
        self.state = get_state(id,STATE_PATH)  # True - have cardiomegalia, False - no cardiomegalia
        self.img_res = img_res
        self.features = features
     
    def get_features(self):
        return self.features
    
    def add_feature(self, feature, name):
        self.features[name] = feature
    
    def get_img(self):
        return self.img
    
    def is_cardiomegalia(self):
        return self.state
