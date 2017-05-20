import json
class notebook:
    def readProgram(self,builder, day):
        with open('program.json') as data_file:
            data = json.load(data_file)
        txt0709 = builder.get_object("entry1")
        txt0911 = builder.get_object("entry2")
        txt1214 = builder.get_object("entry3")
        txt1416 = builder.get_object("entry4")
        txt1618 = builder.get_object("entry5")
        txt1820 = builder.get_object("entry6")
        txt2022 = builder.get_object("entry7")
        txt2224 = builder.get_object("entry8")
        txt0002 = builder.get_object("entry9")
        txt0709.set_text(data[day][0])
        txt0911.set_text(data[day][1])
        txt1214.set_text(data[day][2])
        txt1416.set_text(data[day][3])
        txt1618.set_text(data[day][4])
        txt1820.set_text(data[day][5])
        txt2022.set_text(data[day][6])
        txt2224.set_text(data[day][7])
        txt0002.set_text(data[day][8])

    def writeProgram(self,builder, day):
        txt0709 = builder.get_object("entry1")
        txt0911 = builder.get_object("entry2")
        txt1214 = builder.get_object("entry3")
        txt1416 = builder.get_object("entry4")
        txt1618 = builder.get_object("entry5")
        txt1820 = builder.get_object("entry6")
        txt2022 = builder.get_object("entry7")
        txt2224 = builder.get_object("entry8")
        txt0002 = builder.get_object("entry9")
        with open('program.json') as data_file:
            data = json.load(data_file)
        data[day][0] = txt0709.get_text()
        data[day][1] = txt0911.get_text()
        data[day][2] = txt1214.get_text()
        data[day][3] = txt1416.get_text()
        data[day][4] = txt1618.get_text()
        data[day][5] = txt1820.get_text()
        data[day][6] = txt2022.get_text()
        data[day][7] = txt2224.get_text()
        data[day][8] = txt0002.get_text()
        with open('program.json', 'w') as outfile:
            json.dump(data, outfile)