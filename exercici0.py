class Cotxe:
    def __init__(self, model, any, color, en_venda):
        self.model = model
        self.any = any
        self.color = color
        self.en_venda = en_venda

    
    def descripcio(self):
        
        
        print(f"Cotxe {self.model},{self.any},{self.color},{self.en_venda}")
        
        
        x = self.en_venda 
        #seguint amb opcio TERNARI, FICANT EN COMPTES DE TRUE/FALSE si esta en venta o no
        result = "si esta en venda" if x == True else "no esta en venda"
        print(result)
        
        print(f"En venda: {'SI' if self.en_venda else 'NO'}") #-->MILLOR OPCIO QUE L'ANTERIOR
        #if self.en_venda == True else False
        #    print("Si esta venda")
        #else:
        #    print("No està en venda")
        
cotxe1 = Cotxe("Dacia Spring", 2023, "verd", True)
cotxe2 = Cotxe("Seat Xolon", 2022, "taronja", False)
cotxe3 = Cotxe("Ferrari F1", 2021, "negre", True)
#print(cotxe1)

cotxe1.descripcio()
cotxe2.descripcio()
cotxe3.descripcio()