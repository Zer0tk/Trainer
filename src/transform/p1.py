raw_user_record = " 10827 ; aLeXanDer_vLaDimiRov ; mInSk ; ACTIVE "

user_record = [record.strip() for record in raw_user_record.strip().split(";")]

uid = "UID-" + user_record[0]
full_name = " ".join([name.capitalize() for name in user_record[1].split("_")])
city = user_record[2].upper()
active = user_record[3].lower()


print(f"Нормализованная запись: {uid} | {full_name} | {city} | {active}")
