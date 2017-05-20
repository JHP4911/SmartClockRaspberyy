import datetime
import os

class systemTime():  

    def save(self,_time_tuple):     
        txttime='sudo date  -s "20170520 19:53"'
        txt='sudo date -s \"'+_time_tuple[0]+_time_tuple[1]+_time_tuple[2]+" "+_time_tuple[3]+":"+_time_tuple[4]+'\"'
        os.system(txt)
     
