from exercici0 import Cotxe

cotxe1 = Cotxe("Dacia Spring", 2023, "verd", True)
cotxe2 = Cotxe("Seat Xolon", 2022, "taronja", False)
cotxe3 = Cotxe("Ferrari F1", 2021, "negre", True)
#print(cotxe1)

cotxe1.descripcio()
cotxe1.posa_en_venda()
cotxe1.augmenta_quilometratge(1000)

cotxe2.descripcio()
cotxe2.posa_en_venda()
cotxe2.augmenta_quilometratge(-500) #=>de que vas estafador

cotxe3.descripcio()
cotxe3.posa_en_venda()
cotxe3.augmenta_quilometratge(200)