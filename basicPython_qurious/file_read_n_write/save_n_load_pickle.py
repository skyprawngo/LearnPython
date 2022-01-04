import os
import getpass
import pickle

class read_n_write:
    dir_path = "C:/pywork/anything/basicPython_qurious/file_read_n_write/zxc/cvb"
    save_path = os.path.normpath(os.path.join(dir_path, "abc.txt"))
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)
        
    if not os.path.isfile(save_path):
        with open(save_path, 'wb') as datawriter:
                data = {
                    "id": "",
                    "ip": ""
                }
                pickle.dump(data, datawriter)
        pass
    
    if os.path.isfile(save_path):
        with open(save_path, 'rb') as datareader:
            data = pickle.load(datareader)
    
    def save_login_id(id):
        with open(read_n_write.save_path, 'rb') as datareader:
            data = pickle.load(datareader)
                   
        with open(read_n_write.save_path, 'wb') as datawriter:
            data["id"] = id
            pickle.dump(data, datawriter)
            # datawriter.replace
    
    def load_login_id():
        with open(read_n_write.save_path, 'rb') as datareader:
            data = pickle.load(datareader)
        return data["id"]

data = "daf,kvnk"
read_n_write.save_login_id(data)

print(read_n_write.load_login_id())