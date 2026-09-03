db_config = { 
    "connection": { 
        "host": "production-db.internal", 
        "port": 5432, 
        "user": "postgres" 
    } 
}


host = db_config["connection"]["host"]
port = db_config["connection"]["port"]
ssl_key = db_config["connection"].get("ssl_settings") if db_config["connection"].get("ssl_settings") else "verify-full"

db_config["connection"]["user"] = "admin"
db_config["connection"]["max_connections"] = 100


print("SSL Mode: {}\nПараметры соединения:".format(ssl_key))

for key, val in db_config["connection"].items():
    print(f"* {key}: {val}")
