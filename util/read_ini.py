import configparser
class ReadIni(object):

    def __init__(self,file_neme=None,node=None):
        if file_neme == None:
            file_neme = r"D:\Program Files\Cczcmily\PycharmProjects\selenium3\config\config.ini"
        if node == None:
            self.node = "RegisterElement"
        else:
            self.node = node
        self.cf = self.load_ini(file_neme)
#加载文件
    def load_ini(self,file_neme):
        cf = configparser.ConfigParser()
        cf.read(file_neme)
        return cf
#获取value的值
    def get_value(self,key):
        data = self.cf.get(self.node,key)
        return data


if __name__ ==  '__main__':
    read_init = ReadIni()
    print(read_init.get_value('p'))

