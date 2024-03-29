import sys
#import numpy
#from plugins.CSV2GML.CSV2GMLPlugin import *
from CSV2GML.CSV2GMLPlugin import *



class RemoveNegativePlugin(CSV2GMLPlugin):
   def output(self, filename):
      filestuff = open(filename, 'w')
      filestuff.write('\"\",')
      for i in range(self.n-1):
         filestuff.write(self.bacteria[i]+",")
      filestuff.write(self.bacteria[self.n-1])
      for i in range(self.n):
         if (i == self.n-1): 
            filestuff.write(self.bacteria[i][0:len(self.bacteria[i])-1]+",")
         else:
            filestuff.write(self.bacteria[i]+",")
         for j in range(self.n-1):
             if (i == j): #CSV2GML Removes This
               filestuff.write("1,")
             else:
               if (self.ADJ[i][j] < 0):
                   filestuff.write("0,")
               else:
                   filestuff.write(str(self.ADJ[i][j])+",")
               #filestuff.write(str(abs(self.ADJ[i][j]))+",")
         if (i != self.n-1):
            if (self.ADJ[i][j] < 0):
                filestuff.write("0")
            else:
                filestuff.write(str(self.ADJ[i][self.n-1]))
            #filestuff.write(str(abs(self.ADJ[i][self.n-1])))
         else:
            filestuff.write("1")
         filestuff.write("\n")




