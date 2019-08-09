#GENERATOR GRAFFIC IMAGE
import matplotlib.pyplot as pict

D = {u'TestLabel1':30, u'TestLabel2': 21, u'TestLabel3':34}

pict.bar(range(len(D)), list(D.values()), align='center')
pict.xticks(range(len(D)), list(D.keys()))
pict.show()
#Coded By ParinovYT#
