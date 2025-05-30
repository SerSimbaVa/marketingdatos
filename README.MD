# Integración de Métricas Simulada para Marketing

Este proyecto simula la extracción, procesamiento y almacenamiento de métricas clave desde plataformas de medios utilizando una API pública como placeholder.

## Estructura del Proyecto

```
├── extractor.py          # Obtiene y guarda los datos de usuarios y posts
├── db_loader.py          # Carga CSVs en SQLite y ejecuta consultas
├── main.py               # Orquestador del flujo
├── output/               # Contiene los archivos CSV y la base de datos SQLite
├── .gitignore
├── requirements.txt
└── README.md
```

## Requisitos

Instalar dependencias con:

```bash
pip install -r requirements.txt
```

##  Cómo usar

1. Ejecutar el flujo completo:

```bash
python main.py
```

2. Esto generará los CSVs, los cargará en SQLite y mostrará los resultados de las consultas:
   - Usuarios ordenados por ciudad
   - Cantidad de posts por usuario




