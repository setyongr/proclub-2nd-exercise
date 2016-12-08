class Law:
    def __init__(self,length):
        self.length = int(length)
        self.array = list()
        self.conray = list()
        for i in range(self.length):
            cond = False
            while not(cond):
                tmp = input('Input element: ')
                if ((tmp % 2)==1):
                    self.array.append(tmp)
                    self.conray.append(False)
                    cond = True
                else :
                    print 'It is not odd number, re-input'
    def CarPas(self):
        for i in range(0,self.length-1):
            for j in range(i+1,self.length):
                if (self.array[j]==self.array[i]) and not(self.conray[j])and not(self.conray[i]):
                    self.conray[j] = True
                    self.conray[i] = True
                    break
        for i in range (self.length):
            if not(self.conray[i]):
                print 'Index ke-%d(%d) Jomblo'%(i,self.array[i])
N = input('Masukan jumlah element: ')
listed = Law(N)
listed.CarPas()
