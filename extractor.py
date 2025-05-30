import requests
import csv
from pathlib import Path


# Extrae la informacion segun el endpoint dado de jsonplaceholder.typicode.com/users y /posts
def fetch_data():
    users_url = "https://jsonplaceholder.typicode.com/users"
    posts_url = "https://jsonplaceholder.typicode.com/posts"

    users = requests.get(users_url).json()
    posts = requests.get(posts_url).json()
    return users, posts

# Procesa los datos extraidos y reemplaza el name y lastname por apellido y nombre antes de salvarlos en el cvs


def process_users(users):
    processed = []
    for user in users:
        first_name, *last_name_parts = user["name"].split()
        last_name = " ".join(last_name_parts)
        processed.append({
            "id": user["id"],
            "Nombre": first_name,
            "Apellido": last_name,
            "email": user["email"],
            "company": user["company"]["name"],
            "city": user["address"]["city"],
            "username": user["username"]
        })
    return processed

# Crea la carpeta "output" si no existe ya que alli se guardara los csv y la BD


def save_csv(data, filename):
    Path("output").mkdir(exist_ok=True)
    with open(f"output/{filename}", "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


# Por ultimo salva la data de los users y posts
def extract_and_save():
    users, posts = fetch_data()
    processed_users = process_users(users)
    save_csv(processed_users, "clientes_api.csv")
    save_csv(posts, "posts_api.csv")
