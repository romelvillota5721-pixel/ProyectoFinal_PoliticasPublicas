import json
import pandas as pd

# 1. Cargar el archivo de homicidios intencionales
archivo_excel = "mdi_homicidiosintencionales_pm_2014_2025.xlsx"
df = pd.read_excel(archivo_excel, sheet_name="1. Homicidios Intencionales")

# 2. Convertir la fecha y crear columna de año
df["fecha_infraccion"] = pd.to_datetime(df["fecha_infraccion"])
df["anio"] = df["fecha_infraccion"].dt.year

# 3. Filtrar únicamente los datos del cantón Santo Domingo
df_sd = df[df["canton"] == "SANTO DOMINGO"].copy()

# 4. Agrupar homicidios por año
conteo_por_anio = df_sd.groupby("anio")["tipo_muerte"].count().to_dict()

# 5. Organizar los datos para el Dashboard
datos_dashboard = {
    "canton": "Santo Domingo",
    "provincia": "Santo Domingo de los Tsáchilas",
    "periodo": "2014-2025",
    "serie_homicidios": conteo_por_anio,
    "total_homicidios_periodo": int(df_sd["tipo_muerte"].count()),
    "pico_maximo": {
        "anio": int(max(conteo_por_anio, key=conteo_por_anio.get)),
        "casos": int(max(conteo_por_anio.values())),
    },
}

# 6. Guardar los resultados procesados en un archivo JSON
with open("datos_seguridad_sd.json", "w", encoding="utf-8") as f:
    json.dump(datos_dashboard, f, ensure_ascii=False, indent=4)

print("--------------------------------------------------")
print(" ¡ÉXITO! Los datos de Santo Domingo han sido procesados.")
print(" Se ha creado el archivo 'datos_seguridad_sd.json'.")
print("--------------------------------------------------")