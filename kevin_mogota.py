

def login_session():
    while 1:
        print("")
        print("*" * 50)
        print("ACCEUIL")
        print("1. Vous authentifiez")
        print("2. S'inscrire dans le registre si vous n'avez pas un login")
        print("3. Quitter") 
        print("*" * 50)
        print("")

        user_option = input(str("Option : "))
        if user_option == "1":
            print("")
            print("_" * 50)
            print("AUTHENTIFICATION")
            print("")
            username = input(str("username : "))
            password = input(str("password : "))
            print("_" * 50)
            print("Bienvenue")

        elif user_option == "2":
            print("")
            print("FORMULAIRE MEDECIN")
            print("")
            print("_" * 50)
            nom = input(str("Veuillez entrer votre nom : "))
            prenom = input(str("Veuillez entrer votre prenom : "))
            username = input(str("Veuillez entrer votre username : "))
            while True:
                password = input(str("Entrer un mot de passe (min 8 caractères) : "))
                mdp_trop_court = "votre mot de passe est trop court."
                if len(password) == 0:
                    print(mdp_trop_court.upper())
                elif len(password) < 8: 
                    print(mdp_trop_court.capitalize())
                elif password.isdigit():
                    print("Votre mot de passe ne contient que des nombres.")
                    confirme_password = input(str("Veuillez confirmer votre password : "))
                if password == confirme_password:
                    print("Inscription terminéé.")
                    break
                else:
                    print("votre mot de passe n'est identique veuillez réessayer à nouveau")
                print("_" * 50)
        elif user_option == "3":
            break
        else:
            print("Veuillez entrer un choix valide... ")


#def registre():

def vue_plateforme():
     while True:
        print("")
        print("Menu")
        print("")
        print("*" * 50)
        print("1. Declaration")
        print("2. Registre")
        print("3. Modification")
        print("4. Supprimer")
        print("5. Officier")
        print("6. Quitter")
        print("*" * 50)
        
        user_option = input(str("Option : "))
        if user_option == "1":
            print("")
            print("Formulaire de la declaration")
            print("")
            print("_" * 50)
            nom = input(str("nom : "))
            prenom = input(str("prenom : "))
            nom_du_pere = input(str("nom du père : "))
            nom_du_mere = input(str("nom du mère : "))
            situation_matrimoniale_du_pere = input(str("situation matrimoniale du père : "))
            situation_matrimoniale_du_mere = input(str("situation matrimoniale du mère : "))
            sexe_enfant = input(str("Sexe de l'enfant : "))
            lieu_de_Naissance = input(str("Sexe de l'enfant : "))
            annee_de_naissance= input(str("Année de naissance : "))



            

       
def admin_session():
    while True:
        print("")
        print("AUTHENTIFICATION")
        print("")
        print("_" * 50)
        username = input(str("username : "))
        password = input(str("password : "))
        print("_" * 50)
        print("")
        vue_plateforme()
        



def main(): 
    while True:
        print("")
        print("Bienvenue dans la plateforme système naissance")
        print("")
        print("*" * 50)
        print("1: Login de Medecin")
        print("2: Login de Parent")
        print("3: Login de Admin")
        print("4: Quitter")
        print("*" * 50)

        user_option = input(str("Option : "))
        if user_option =="1":
            print("Medecin Login")
            login_session()
        elif user_option =="2":
            print("Parent Login")
            login_session()
        elif user_option =="3":
            print("Admin Login") 
            admin_session()
        elif user_option =="4":
            print("A bientôt!") 
        else:
            print("Veuillez entrer un choix valide...")

main()
