def funktsioon(värv, ristkülik, ekraan):
   uus_värv = []
   uus_värv.append(255 - värv[0])
   uus_värv.append(255 - värv[1])
   uus_värv.append(255 - värv[2])
   ekraan.fill(uus_värv, ristkülik)
