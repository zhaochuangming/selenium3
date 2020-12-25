from util.read_ini import ReadIni
class FindElement(object):
    def __init__(self,cc):
        self.cc=cc
    def get_element(self,key):
        read_ini = ReadIni()
        data = read_ini.get_value(key)
        a = data.split('>')
        if len(a) ==2:
            by = data.split('>')[0]
            value = data.split('>')[1]
            try:
                if by == 'id':
                    return self.cc.find_element_by_id(value)
                elif by == 'class_name':
                    return self.cc.find_element_by_class_name(value)
                else:
                    return self.cc.find_element_by_xpath(value)
            except:
                return None
        else:
            by = data.split('>')[0]
            value = data.split('>')[1]
            send = data.split('>')[2]
        try:
            if by == 'id':
                return self.cc.find_element_by_id(value).send_keys(send)
            elif by == 'class_name':
                return self.cc.find_element_by_class_name(value).send_keys(send)
            else:
                return self.cc.find_element_by_xpath(value).send_keys(send)
        except:
            return None
