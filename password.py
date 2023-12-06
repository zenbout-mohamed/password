import hashlib
import re
import json
import random
import string

# def generate_random_password(length=12): Cela définit la signature de la fonction. La fonction s'appelle generate_random_password
# et prend un argument optionnel length qui spécifie la longueur du mot de passe. Si aucune longueur n'est fournie,
# elle sera par défaut de 12 caractères.
def generate_random_password(length=12):
    # characters = string.ascii_letters + string.digits + string.punctuation : Cela crée une chaîne de caractères characters qui contient tous les caractères alphabétiques
    # en minuscules et en majuscules (string.ascii_letters), les chiffres (string.digits), 
    # et les caractères de ponctuation (string.punctuation).
    characters = string.ascii_letters + string.digits + string.punctuation
    # password = ''.join(random.choice(characters) for _ in range(length)) : Cela génère le mot de passe proprement dit.
    # Il utilise une expression génératrice pour créer une séquence de caractères aléatoires tirés de la chaîne characters.
    # La longueur de cette séquence est spécifiée par l'argument length. La méthode join est utilisée pour concaténer
    # ces caractères en une chaîne unique représentant le mot de passe.
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def load_passwords():
    try:
        with open('passwords.json', 'r') as file:
            passwords = json.load(file)
    except FileNotFoundError:
        passwords = {}
    return passwords
# with open('passwords.json', 'w') as file:: Cela ouvre un fichier nommé "passwords.json" en mode écriture ('w').
# Le mot-clé with est utilisé ici pour s'assurer que le fichier est correctement fermé après utilisation,
# même en cas d'erreur pendant l'exécution du bloc de code à l'intérieur.
# json.dump(passwords, file, indent=2): Cela utilise le module json pour écrire le contenu de la variable passwords dans le fichier spécifié.
# La fonction json.dump() prend trois arguments principaux :
def save_passwords(passwords):
    with open('passwords.json', 'w') as file:
        json.dump(passwords, file, indent=2)

def add_password():
    passwords = load_passwords()

def display_passwords():
    passwords = load_passwords()

    if not passwords:
        print("Aucun mot de passe enregistré.")
    else:
        print("Mots de passe enregistrés :")
        for hashed_password, original_password in passwords.items():
            print(f"{hashed_password}: {original_password}")

def check_password_strength(password):
    # Vérifier la longueur minimale de 8 catactères :
    if len(password) < 8:
        return False, "Le mot de passe doit contenir au moins 8 caractères."
    
    # any(char.isdigit() for char in password): Cette expression génère un itérable de valeurs booléennes,
    # indiquant si chaque caractère de password est un chiffre. La méthode isdigit() renvoie True si le caractère est un chiffre,
    # sinon elle renvoie False. La fonction any retourne True si au moins l'un des caractères est un chiffre, sinon elle retourne False.
    # not any(char.isdigit() for char in password): Cette partie de la condition vérifie si la négation de l'expression précédente est vraie,
    # c'est-à-dire si aucun des caractères de password n'est un chiffre.
    # Vérifier la présence de chiffres
    
    if not any(char.isdigit() for char in password):
        return False, "Le mot de passe doit contenir au moins un chiffre."

    
    # any(char.isupper() for char in password): Cette expression génère un itérable de valeurs booléennes,
    # indiquant si chaque caractère de password est une lettre majuscule.
    # La fonction any retourne True si au moins l'un des caractères est une lettre majuscule, sinon elle retourne False.
    
    # Vérifier la présence de lettres majuscules et minuscules
    if not any(char.isupper() for char in password) or not any(char.islower() for char in password):
        return False, "Le mot de passe doit contenir des lettres majuscules et minuscules."
    
    # re.search("[!@#$%^&*(),.?\":{}|<>]", password): Cette expression utilise le module re (expression régulière)
    # pour rechercher dans la chaîne password la présence d'au moins un caractère spécial. L'expression régulière [!@#$%^&*(),.?\":{}|<>]
    # spécifie un ensemble de caractères spéciaux à rechercher.
    # not re.search("[!@#$%^&*(),.?\":{}|<>]", password): 
    # Cette partie de la condition vérifie si la négation de l'expression régulière est vraie,
    # c'est-à-dire si aucun des caractères spéciaux n'a été trouvé dans le mot de passe.
    # Vérifier la présence de caractères spéciaux
    
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Le mot de passe doit contenir au moins un caractère spécial."

    return True, "Le mot de passe est suffisamment fort."

def hash_password(password):
    # Utiliser l'algorithme de hachage SHA-256
    # password.encode() : Cette partie encode la chaîne du mot de passe en une séquence d'octets,
    #  car la fonction de hachage SHA-256 opère sur des données de type bytes.
    # hashlib.sha256(...) : Cette partie crée un objet de hachage SHA-256 à l'aide du module hashlib.
    # hashed_password : La variable hashed_password stocke le résultat du hachage, qui est une chaîne hexadécimale représentant le haché SHA-256 du mot de passe
    
    hashed_password = hashlib.sha256(password.encode()).hexdigest() 
    #  Cette méthode convertit le résultat du hachage en une représentation hexadécimale, ce qui est une manière courante de représenter des hachés de manière lisible.
    # return hashed_password : La fonction renvoie le haché du mot de passe. Ainsi, lorsque vous appelez cette fonction avec un mot de passe en tant qu'argument, elle retournera le haché SHA-256 de ce mot de passe.
    return hashed_password

def main():
    # while True:: C'est une boucle infinie qui permet à l'utilisateur de choisir un mot de passe tant que celui-ci ne répond pas
    # aux critères de sécurité définis.
    while True:

        print("Menu:")
        print("1. Ajouter un nouveau mot de passe")
        print("2. Afficher les mots de passe")
        print("3. Quitter")

        choice = input("Choisissez une option (1, 2 ou 3) : ")

        if choice == '1':
            password = input("Veuillez entrer votre mot de passe : ")
            if password.lower() == 'q':
                break
            # is_strong, message = check_password_strength(password): Cette ligne appelle la fonction check_password_strength avec le mot de passe saisi
            # par l'utilisateur. La fonction renvoie deux valeurs : is_strong (un booléen indiquant si le mot de passe est suffisamment fort)
            # et message (un message décrivant la force ou la faiblesse du mot de passe).
       
            is_strong, message = check_password_strength(password)
            # if is_strong:: Cette condition vérifie si le mot de passe est considéré comme suffisamment fort en fonction des critères de sécurité définis.
            # Si c'est le cas, le bloc d'instructions suivant est exécuté.
            if is_strong:
                # hashed_password = hash_password(password): Appelle la fonction 
                # hash_password pour générer le haché SHA-256 du mot de passe.
                hashed_password = hash_password(password)
                print("Mot de passe accepté. Mot de passe haché (SHA-256) :", hashed_password)
            
                
                # Ajouter le mot de passe seulement s'il est fort
                passwords = load_passwords()
                passwords[hashed_password] = password
                save_passwords(passwords)
                print("Mot de passe ajouté avec succès.")
                
            else:
                print("Mot de passe faible. ", message)
                
            add_password()
        elif choice == '2':
            display_passwords()
        elif choice == '3':
            print("Le programme à été quitté.")
             # Arret de la boucle par break :
            break
        else:
            print("Option invalide. Veuillez choisir une option valide.")
            # La ligne de code if __name__ == "__main__": est une convention en Python qui vérifie si le script est exécuté en tant que programme principal
            # (c'est-à-dire s'il est exécuté directement et non importé en tant que module dans un autre script).
if __name__ == "__main__":
    main()


# ---------------------------------------------------------------------------------------

