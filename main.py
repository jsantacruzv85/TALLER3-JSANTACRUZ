from models.boa_constrictor import Boa_Constrictor
from models.huron import Huron

def main():
    # Creación de una boa constrictor
    boa = Boa_Constrictor(nombre="Boa1", peso=15, edad=5, pais_origen="Brasil", impuestos=20.5)
    boa.agregar_raton()
    print(f"Boa sonido: {boa.hacer_sonido()}")
    print(f"Boa ratones comidos: {boa.ratones_comidos}")
    print(f"Boa flete: {boa.calcular_flete()}")

    # Creación de un hurón
    huron = Huron(nombre="Huron1", peso=2, edad=3, pais_origen="Argentina", impuestos=10.0)
    print(f"Huron sonido: {huron.hacer_sonido()}")
    print(f"Huron flete: {huron.calcular_flete()}")

if __name__ == "__main__":
    main()
