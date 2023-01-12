# lowXXX
#reasonableXXX
# highXXX

# Saidas
'''
Saida
lowLive
averageLive
highLive

lowVod
averageVod
highVod


rulebase.addRule(new IT2_Rule(new IT2_Antecedent[]{ highFPLMean,highFPLStd,lowBiatTotal },highVideo));
'''


import csv
import re
from re import search

def is_not_blank(s):
    return bool(s and not s.isspace())


def termo(atributo,valor):
#   r_low = range(0, 3.99999, 0.1)
#   r_reasonable = range(4, 6.99999, 0.1)
#   r_high = range(7, 10, 0.1)
#   if valor in _rlow :
#   print valor + atributo
   if 0 <= float(valor) <= 0.099999:
      return "veryLow" + atributo
   if 0.100000 <= float(valor) <= 1.599999:
      return "low" + atributo
   if 1.600000 <= float(valor) <= 3.999999:
      return  "bellowReasonable" + atributo
   if 4 <= float(valor) <= 8.999999:
      return "reasonable" + atributo
#   if 5 <= float(valor) <= 6.99999: 
#      return  "belowhigh" + atributo
   if 9 <= float(valor) <= 10: 
      return  "high" + atributo


def termo_saida_video(label):
#   print label
   if search("quic",label) or search("https",label):
      return "averageVideo"
#   if search("quic",label) or search("https",label):
#      return "averageVod"
#   if search("quic",label) or search("https",label):
#      return "averageLive"
   if search("dns",label) or search(r'\b' + "http" + r'\b',label) or search("outros",label):
      return  "lowVideo"
#   if search("dns",label) or search(r'\b' + "http" + r'\b',label) or search("outros",label):
#      return  "lowVod"
#   if search("dns",label) or search(r'\b' + "http" + r'\b',label) or search("outros",label):
#      return  "lowLive"
   if search("vod",label) or search("live",label):
      return  "highVideo"
#   if search("vod",label):
#      return  "highVod"
#   if search("live",label):
#      return  "highLive"


def termo_saida_live(label):
#   print label
   if search("quic",label) or search("https",label) or search("vod",label):
      return "averageLive"
   if search("dns",label) or search(r'\b' + "http" + r'\b',label) or search("outros",label):
      return  "lowLive"
   if search("live",label):
      return  "highLive"

def termo_saida_vod(label):
#   print label
   if search("quic",label) or search("https",label) or search("live",label):
      return "averageVod"
   if search("dns",label) or search(r'\b' + "http" + r'\b',label) or search("outros",label):
      return  "lowVod"
   if search("vod",label):
      return  "highVod"

def conta_atributos(list):
   atributos_video = ['bellowReasonableNormBwd_Packet_Length_Std','bellowReasonableNormFwd_Packet_Length_Mean','bellowReasonableNormFwd_Packet_Length_Std','highNormBwd_Packet_Length_Mean','highNormBwd_Packet_Length_Std','highNormPacket_Length_Mean','highNormPacket_Length_Std','lowNormBwd_Packet_Length_Std''lowNormFwd_IAT_Mean','lowNormFwd_Packet_Length_Mean','reasonableNormBwd_Packet_Length_Std','reasonableNormFwd_Packet_Length_Mean','reasonableNormFwd_Packet_Length_Std','reasonableNormPacket_Length_Mean','reasonableNormPacket_Length_Std','veryLowNormBwd_IAT_Mean','veryLowNormFlow_IAT_Mean','veryLowNormFlow_IAT_Std','veryLowNormFwd_IAT_Mean','veryLowNormFwd_IAT_Std']
   quantos=0
   for i in range(len(list)):
       for x in range(len(atributos_video)):
           if list[i] == atributos_video[x]:
	       quantos=quantos+1
   return quantos


mycsv = csv.reader(open("regras_limpa.csv"),delimiter=';')
for row in mycsv:
   l_regras = []
   if is_not_blank(row[0]) and search("Norm",row[1]):
      text = row[1]
      y = text.split("(")
      atributo = y[1].split(" ")
#      print  atributo[0] + " " +   atributo[2]
#      print termo(atributo[0],atributo[2])
      l_regras.append(termo(atributo[0],atributo[2]))
#      print "Norm" + y[1]

   if is_not_blank(row[1]) and search("Norm",row[1]):
      text = row[1]
      y = text.split("(")
      atributo = y[1].split(" ")
#      print  atributo[0] + " " +   atributo[2]
#      print termo(atributo[0],atributo[2])
      l_regras.append(termo(atributo[0],atributo[2]))
#      print "Norm" + y[1]

   if is_not_blank(row[2]) and search("Norm",row[2]):
      text = row[2]
      y = text.split("(")
      atributo = y[1].split(" ")
#      print  atributo[0] + " " +   atributo[2]
#      print termo(atributo[0],atributo[2])
      l_regras.append(termo(atributo[0],atributo[2]))
#      print "Norm" + y[1]

   if is_not_blank(row[3]) and search("Norm",row[3]):
      text = row[3]
      y = text.split("(")
      atributo = y[1].split(" ")
#      print  atributo[0] + " " +   atributo[2]
#      print termo(atributo[0],atributo[2])
      l_regras.append(termo(atributo[0],atributo[2]))
#      print "Norm" + y[1]

   if is_not_blank(row[4]) and search("Norm",row[4]):
      text = row[4]
      y = text.split("(")
      atributo = y[1].split(" ")
#      print  atributo[0] + " " +   atributo[2]
#      print termo(atributo[0],atributo[2])
      l_regras.append(termo(atributo[0],atributo[2]))
#      print "Norm" + y[1]

   if is_not_blank(row[5]) and search("Norm",row[5]):
      text = row[5]
      y = text.split("(")
      atributo = y[1].split(" ")
#      print  atributo[0] + " " +   atributo[2]
#      print termo(atributo[0],atributo[2])
      l_regras.append(termo(atributo[0],atributo[2]))
#      print "Norm" + y[1]

   if is_not_blank(row[6]) and search("Norm",row[6]):
      text = row[6]
      y = text.split("(")
      atributo = y[1].split(" ")
#      print  atributo[0] + " " +   atributo[2]
#      print termo(atributo[0],atributo[2])
      l_regras.append(termo(atributo[0],atributo[2]))
#      print "Norm" + y[1]

   if is_not_blank(row[7]) and search("Norm",row[7]):
      text = row[7]
      y = text.split("(")
      atributo = y[1].split(" ")
#      print  atributo[0] + " " +   atributo[2]
#      print termo(atributo[0],atributo[2])
      l_regras.append(termo(atributo[0],atributo[2]))
#      print "Norm" + y[1]

   if is_not_blank(row[8]) and search("Norm",row[8]):
      text = row[8]
      y = text.split("(")
      atributo = y[1].split(" ")
#      print  atributo[0] + " " +   atributo[2]
#      print termo(atributo[0],atributo[2])
      l_regras.append(termo(atributo[0],atributo[2]))
#      print "Norm" + y[1]


   '''
   if is_not_blank(row[2]):
      text = row[2]
      print text
   if is_not_blank(row[3]):
      text = row[3]
      print text
   if is_not_blank(row[4]):
      text = row[4]
      print text
   if is_not_blank(row[5]):
      text = row[5]
      print text
   if is_not_blank(row[6]):
      text = row[6]
      print text
   if is_not_blank(row[7]):
      text = row[7]
      print text
   if is_not_blank(row[8]):
      text = row[8]
      print text
   '''
# Extracao de label   
   if is_not_blank(row[0]) and search("Label",row[0]):
      text = row[1]
      y = text.split(" ")
      label=(re.sub('Label=', '', y[1]))
      l_regras.append(termo_saida_video(label))

   if is_not_blank(row[1]) and search("Label",row[1]):
      text = row[1]
      y = text.split(" ")
      label=(re.sub('Label=', '', y[1]))
      l_regras.append(termo_saida_video(label))

   if is_not_blank(row[2]) and search("Label",row[2]):
      text = row[2]
      y = text.split(" ")
      label=(re.sub('Label=', '', y[1]))
      l_regras.append(termo_saida_video(label))

   if is_not_blank(row[3]) and search("Label",row[3]):
      text = row[3]
      y = text.split(" ")
      label=(re.sub('Label=', '', y[1]))
      l_regras.append(termo_saida_video(label))

   if is_not_blank(row[4]) and search("Label",row[4]):
      text = row[4]
      y = text.split(" ")
      label=(re.sub('Label=', '', y[1]))
      l_regras.append(termo_saida_video(label))

   if is_not_blank(row[5]) and search("Label",row[5]):
      text = row[5]
      y = text.split(" ")
      label=(re.sub('Label=', '', y[1]))
      l_regras.append(termo_saida_video(label))

   if is_not_blank(row[6]) and search("Label",row[6]):
      text = row[6]
      y = text.split(" ")
      label=(re.sub('Label=', '', y[1]))
      l_regras.append(termo_saida_video(label))

   if is_not_blank(row[7]) and search("Label",row[7]):
      text = row[7]
      y = text.split(" ")
      label=(re.sub('Label=', '', y[1]))
      l_regras.append(termo_saida_video(label))

   if is_not_blank(row[8]) and search("Label",row[8]):
      text = row[8]
      y = text.split(" ")
      label=(re.sub('Label=', '', y[1]))
      l_regras.append(termo_saida_video(label))


#   print l_regras
   # Monta regra do juzzy
   saida=l_regras[-1]
   s_l_regras = l_regras[ : -1]
   if saida == "highVideo":
      print "rulebase.addRule(new IT2_Rule(new IT2_Antecedent[]{ " +  (','.join(s_l_regras)) + " }," + saida + "));"
   else:
      acertos=conta_atributos(s_l_regras)
#      print acertos
      if acertos < 2:
    	  print "rulebase.addRule(new IT2_Rule(new IT2_Antecedent[]{ " +  (','.join(s_l_regras)) + " }," + saida + "));"
      
