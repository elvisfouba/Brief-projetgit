import mysql.connector
mybd = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        port=3308,
        database="plateforme")

mycursor = mybd.cursor()
data=("1 er Arrondissement", "2021-11-30", "Masculin", "NDJAMENA", "173", "2021-6-3", "Kevin Mogota", " Mogota père", "Sarh", "1980-10-21", "Fonctionnaire", "Mogotine mère", "Kyabe", "1982-10-21", "Managere")

#mycursor.execute("CREATE TABLE acte_naissance(Id int(11) PRIMARY KEY AUTO_INCREMENT, de varchar(255) , le date , enfant_de_sexe varchar(255), survenue_a varchar(255), rue varchar(255), le2 date, nomme varchar(255), fils_ou_fille_de varchar(255) , ne_a varchar(255), le3 date, profession varchar(255) , et_de varchar(255), nee_a varchar(255) , le4 date, profession_m varchar(255)) ")

mycursor.execute("INSERT INTO `acte_naissance`(`de`, `le`, `enfant_de_sexe`, `survenue_a`, `rue`, `le2`, `nomme`, `fils_ou_fille_de`, `ne_a`, `le3`, `profession`, `et_de`, `nee_a`, `le4`, `profession_m`)  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s)",data)
mybd.commit()
