import tables
import os

class JetDataset():

    def __init__(self,filepath:str = os.path.join(os.path.dirname(os.path.realpath(__file__)),"data","all.h5")):

        self._file = tables.open_file(filepath,mode="r")
        self.data = self._file.root["data"]

    def __del__(self):
        self._file.close()

    def __len__(self):
        return len(self.data)

    def __getitem__(self, item):

        return self.data[item].reshape(-1,4)
