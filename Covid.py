import requests
import pandas as pd

# URL de la API
url = "https://api.covidtracking.com/v1/states/daily.json"

# Realizar solicitud a la API
response = requests.get(url)

if response.status_code == 200:
    # Cargar datos en un DataFrame de pandas
    data = response.json()
    df = pd.DataFrame(data)
    
    # Convertir la columna 'date' en formato de fecha
    df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
    
    # Filtrar columnas relevantes para el análisis
    df = df[['date', 'state', 'positive', 'death', 'recovered']]
    
    # Realizar cualquier otro análisis que desees aquí
    # Por ejemplo, puedes calcular la tasa de mortalidad, la tasa de recuperación, etc.
    # Puedes usar visualizaciones para representar los datos de manera más clara.
    
    # Ejemplo: Calcular la tasa de mortalidad
    df['mortality_rate'] = df['death'] / df['positive']
    
    # Ejemplo: Filtrar datos de un estado específico (ejemplo: California)
    california_data = df[df['state'] == 'CA']
    
    # Puedes continuar haciendo más análisis según tus necesidades.
    # Una vez que hayas realizado el análisis, puedes generar el informe con tus conclusiones y descubrimientos.
else:
    print(f"Error: {response.status_code}")
