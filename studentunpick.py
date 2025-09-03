import pickle
class studentunpick:
    def readdata(self):
        try:
            with open("studentrecord1.data","rb") as rp:
                while True:
                    try:
                        record=pickle.load(rp)
                        #print(type(record))
                        print(record.name,record.number,record.marks)
                    except EOFError:
                        break
        except FileNotFoundError:
            print("File not found")
s=studentunpick()
s.readdata()
