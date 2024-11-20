import pandas as pd
from django.core.management.base import BaseCommand
from api.models import cliente

class Command(BaseCommand):
    help = 'Importa datos desde un archivo CSV a la tabla Cliente'

    def add_arguments(self, parser):
            parser.add_argument('clientes_limpios.csv', type=str, help='Ruta del archivo CSV a importar')

    def handle(self, *args, **kwargs):
        # Leemos el archivo y lo agregamos a la variable df o DataFrame
        csv_file = kwargs['clientes_limpios.csv']
        try:
            df = pd.read_csv(csv_file)
        except FileNotFoundError:
            self.stderr.write(f"El archivo {csv_file} no fue encontrado.")
            return
        except Exception as e:
            self.stderr.write(f"Error al leer el archivo CSV: {e}")
            return 

        # Iteracion sobre el DataFrame y crear las instacias del modelo
        for _, row in df.iterrows():    
            try:
                # Validación y creación del cliente
                cliente.objects.create(
                    cliente_id=row['Cliente_ID'],
                    edad=int(row['Edad']),  # Convertir a entero
                    genero=row['Genero'],
                    saldo=float(row['Saldo']),  # Convertir a flotante
                    active=bool(row['Activo']),  # Convertir de 1/0 a booleano
                    nivel_de_satisfaccion=int(row['Nivel_de_Satisfaccion'])  # Convertir a entero
                )
            except Exception as e:
                print(f"Error al procesar la fila {row.to_dict()}: {e}")
        self.stdout.write(self.style.SUCCESS("Datos importados correctamente"))