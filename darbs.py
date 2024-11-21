# Uzraksti programmu, kurā  dators izvēlas 100 skaitļus robežās no 101 līdz 500. Izvēlētie skaitļi tiek izvadīti terminālī.

import random

for i in range(100):  #Izveidoju lai izvēlas 100 skaitlus
    random_skaitlis = random.randint(100, 501)  # Lai nejauši izvēlas skaitļus no 100 lidz 500 robežās
    print(random_skaitlis)  # Random skaitli lai izdrukā 

