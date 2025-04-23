"""
    Evaluación Final: Cálculo Numérico.

    Análisis de Datos Climáticos.

    Desarrollado por: Juan Diego Cordero, Nelson Guerrero, Luis León, Alejandro López y Eduardo Tovar.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carga de datos desde el archivo CSV.
df = pd.read_csv('https://raw.githubusercontent.com/CAChemE/curso-python-datos/master/data/weather_data.csv')

# Eliminación de los registros con null, NaN, 0 o 'value'.
df.replace('Varias', pd.NA, inplace = True)  # Reemplazar 'value' con NaN.
df = df.replace(0, pd.NA)  # Reemplazar 0 con NaN.
df.dropna(inplace = True)  # Eliminar filas con NaN.
df.dropna()

# Eliminación de los registros con NaN, value y 0.
csv = df

# Imprimir la tabla.
print(csv)

# Filtrado de data.
dataframe = csv[['fecha', 'presMax', 'presMin', 'tmax', 'tmed', 'tmin', 'velmedia', 'sol']]
dataframe.columns = ['Fecha', 'Presión Máx.', 'Presión Mín.', 'Temperatura Máx.', 'Temperatura Med.', 'Temperatura Mín.', 'Velocidad Med.', 'Sol']

# Conversión de la columna 'fecha' a tipo 'datetime'.
dataframe.loc[:, 'Fecha'] = pd.to_datetime(dataframe['Fecha']).dt.date

# Cálculo de la temperatura media del período registrado.
tmed = dataframe['Temperatura Med.'].mean()
print(f'Temperatura media del periodo registrado: {tmed:.2f} °C')

# Cálculo de la temperatura máxima (incluyendo la fecha).
tmax = dataframe['Temperatura Máx.'].max()
fecha_tmax = dataframe.loc[dataframe['Temperatura Máx.'] == tmax, 'Fecha'].values[0]
print(f'Temperatura máxima del periodo registrado: {tmax:.2f} °C, Fecha: {fecha_tmax}')

# Cálculo de la temperatura mínima (incluyendo la fecha).
tmin = dataframe['Temperatura Mín.'].min()
fecha_tmin = dataframe.loc[dataframe['Temperatura Mín.'] == tmin, 'Fecha'].values[0]
print(f'Temperatura mínima del periodo registrado: {tmin:.2f} °C, Fecha: {fecha_tmin}')

# Cálculo del rango de temperatura.
trange = tmax - tmin
print(f'Rango de temperatura: {trange:.2f} °C')

# Gráfico de Líneas: Evolución de la temperatura máxima y mínima a lo largo del tiempo.
plt.figure(figsize = (10, 6))
plt.plot(dataframe['Fecha'], dataframe['Temperatura Máx.'], label = 'Temperatura Máxima', color = 'red')
plt.plot(dataframe['Fecha'], dataframe['Temperatura Mín.'], label = 'Temperatura Mínima', color = 'blue')
plt.title('Evolución de la Temperatura Máxima y Mínima', fontsize = 16)
plt.xlabel('Fecha')
plt.ylabel('Temperatura (°C)')
plt.legend()
plt.show()

# Boxplot: Temperatura media.
plt.figure(figsize = (10, 5))
sns.boxplot(x = dataframe['Temperatura Med.'])
plt.title('Boxplot de la Temperatura Media', fontsize = 16)
plt.xlabel('Temperatura Media (°C)')
plt.show()

# Dataframe de variables climáticas relevantes para las gráficas 3 y 4.
data = dataframe[['Presión Máx.', 'Presión Mín.', 'Temperatura Máx.', 'Temperatura Med.', 'Temperatura Mín.', 'Velocidad Med.', 'Sol']]

# Mapa de Calor: Matriz de correlaciones entre la presión (máxima y mínima), la temperatura (máxima, media y mínima), la velocidad media y el sol.
matriz_correlaciones = data.corr()

plt.figure(figsize = (10, 7))
sns.heatmap(matriz_correlaciones, annot = True, cmap = 'coolwarm', fmt = '.2f')
plt.title('Matriz de Correlaciones entre Variables Climáticas', fontsize = 16)
plt.xticks(rotation = 30, ha = 'right', fontsize = 8)
plt.yticks(fontsize = 8)
plt.show() 

# Diagrama de Dispersión: Presión (máxima y mínima) y Temperatura (máxima, media y mínima).

sns.pairplot(data[['Presión Máx.', 'Presión Mín.', ]], height = 1.5)
sns.pairplot(data[['Temperatura Máx.', 'Temperatura Med.', 'Temperatura Mín.']], height = 1.5)
plt.show()