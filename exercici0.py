class Cotxe:
    def __init__(self, model, any, color, en_venda):
        self.model = model
        self.any = any
        self.color = color
        self.en_venda = en_venda
        self.quilometratge = 0

    def start(self):
        print(f"Cotxe {self.model} en marxa ")

    def stop(self):
        print(f"Cotxe {self.model} aturat")
        
    def descripcio(self):
        
        print("----------------------")
        print(f"Model:{self.model}")
        print(f"Any:{self.any}")
        print(f"Color:{self.color}")
        print(f"Quilometratge:{self.quilometratge}")
        # if (self.en_venda):
        #     print("En venda:SI")
        # else:
        #     print("En venda:NO")
        print(f"En venda:{'SI' if self.en_venda else 'NO'}")
        print("----------------------")

        
    def posa_en_venda(self):   
        x = self.en_venda 
        #seguint amb opcio TERNARI, FICANT EN COMPTES DE TRUE/FALSE si esta en venta o no
        result = "si esta en venda" if x == True else "no esta en venda"
        print(result)
        
        print(f"En venda: {'SI' if self.en_venda else 'NO'}") #-->MILLOR OPCIO QUE L'ANTERIOR
        #if self.en_venda == True else False
        #    print("Si esta venda")
        #else:
        #    print("No està en venda")
    
    def augmenta_quilometratge(self, q):
        if (q < 0):
            print("De que vas estafador!")
        else:
            self.quilometratge = self.quilometratge + q
        
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