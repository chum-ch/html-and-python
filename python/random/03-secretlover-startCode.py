import random
studentsList = ["SARETH","SEAVY","RATHTEKA","SREYHON","VANTHORN","SOK","TOUN","SREYTOUCH","CHAINY","SOM","SIMENG","NHORK","SREYNOT","THIN","SEANGHAY","LYHUOY","SOPHANNA","NIMOUT","VOULEAK","CHET","SINY","SOTHEAN","SOPHORN","SREYHIEB","MENGHOUR","NISAI","CHANTHEA","PHEARAK","SOMOUN","SREYNICH","SAOLEE","RIN","ON","SOPHANNA","CHANTHY","MOLIKA","BUNSAL","SOKTHANG","DYNA","SARA","VOUCHLY","SOTHOUN","LYDEN","MONYRA","VUN","LANH","PHALLY","SREYPICH","SENGHIM","DAVY","CHUM","LYHEANG","KOEMSAK","VICHEKA","LAMYAI","CHANTHOU","KUNTHY","SOPHEA","VANTHEAV","SOPHEAK","NARATH","SREYNGIT","MENGHEANG","VUTHY","CHANRY","CHANNARY","LYHOR","THALY","HOUTCHHAY","SOMPHORS","SINET","SREY AEM","THON","PROS"]

name = input("What is your name: ")
indexOfName = random.randrange(0, len(studentsList))
# print(name.upper() + " secret lover is ", str(studentsList[indexOfName]))
# other way
print(name.upper() + " secret lover is ", random.choice(studentsList))