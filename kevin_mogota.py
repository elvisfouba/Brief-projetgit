
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
            pass_word = input(str("pass_word : "))
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
                if len(pass_word) == 0:
                    print(mdp_trop_court.upper())
                elif len(pass_word) < 8: 
                    print(mdp_trop_court.capitalize())
                elif pass_word.isdigit():
                    print("Votre mot de passe ne contient que des nombres.")
                    confirme_password = input(str("Veuillez confirmer votre password : "))
                if pass_word == confirme_password:
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

def acte_naissance():
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
            print("Center d'Etat civil PRINCIPAL")
            de = input(str("de : "))
            le1 = input(str("le : "))
            print("S'est presente(e) suivant la déclaration des parents de l'enfant")
            print("qui a declaré la naissance d'un ")
            enfant_de_sexe =input(str("enfant du sexe: "))
            survenue_a = input(str("survenue à: "))
            rue = input(str("Rue: "))
            le2 = input(str("Le : "))
            nomme = input(str(" Nom complet de enfant : "))
            fils_ou_fille_de = input(str("Nom complet du père : "))
            ne_a = input(str("Né à : "))
            le3 = input(str("Le : "))
            profession = input(str("Profession : "))
            et_de = input(str("Nom complet de la mère : "))
            nee_a = input(str("Née à : "))
            le4 = input(str("Le : "))
            profession_m = input(str("Profession : "))
            print("Sa legistime épouse")
            print("")
            print("L'officier d'Etat civil")
            print("")
            print("")
            print("")
            print("")
            print("Fait à N'Djamena")
            print("")
            print("Votre declaration a bien été enregistré")
            print("_" * 50)

#L'administration doit l'authentifier à partir de ce login directement
# car on peut laisser la main pour son inscription du fait qu'il contrôle tous
#donc son non d'utilisateur et et son mot de passe sont enregistrer directement dans la base de donnée

def admin_session():
    while True:
        print("")
        print("AUTHENTIFICATION")
        print("")
        print("_" * 50)
        username = input(str("username : "))
        pass_word = input(str("pass_word : "))
        print("_" * 50)
        print("")
        acte_naissance()
        



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