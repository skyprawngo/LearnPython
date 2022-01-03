import os
import getpass
import pickle

class read_n_write:
    dir_path = "C:/pywork/zxc/cvb"
    save_path = os.path.normpath(os.path.join(dir_path, "abc.txt"))
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)
        
    if os.path.isfile(save_path):
        try:
            with open(save_path, 'rb') as datareader:
                data = pickle.load(datareader)
        except:
            with open(save_path, 'wb') as datawriter:
                data = {
                    "id": "",
                    "ip": ""
                }
                pickle.dump(data, datawriter)
                
    def save_login_id(id):
        with open(read_n_write.save_path, 'rb') as datareader:
                    data = pickle.load(datareader)
                    data["id"] = id
                    print(data)
                
        with open(read_n_write.save_path, 'wb') as datawriter:
            pickle.dump(data, datawriter)
            # datawriter.replace


data = "asdfasdd"
read_n_write.save_login_id(data)