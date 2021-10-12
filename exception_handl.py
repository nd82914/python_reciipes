def testfunction(x):
    return 1/x
try:
    testfunction(0)
except:
    pass

class AutoDownload():
    def __init__(self, filepath):
        self.filepath = filepath
        self.label_num = 0

    def __enter__(self):
        self.f = open(self.filepath, "w")
        return self
    
    def __exit__(self, exception_type, exception_value, traceback):
        self.f.close()
        
    def set_item_option():    
        return 0
        
    def setXMLoption():
        return 0
            
    def setHive_option():
        return 0
        
with AutoDownload as AD:
    csvlist, path=AutoDownload("./hogehoge.csv")