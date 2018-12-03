#Faire un agenda où on peut ajouter ou supprimer un contact
#structure:
#Nom, prenom, telephone, adresse, email.
#Ajouter - done
#Modifier
#search - done
#Supprimer
#Supprimer tous les contacts
import getpass

import csv

# DISPLAY FUNCTION

def displayContacts():
    file = open("Agenda.csv", "r")
    for line in file:
        tab = line.split(";")
        print("{}; {}; {}; {}; {}".format(tab[0], tab[1], tab[2], tab[3], tab[4]))
    file.close()

# ---------------------------------------------------------------------------------------------------------------------
# ADDING FUNCTION

def addContact():
    # enter the elements needed, the sport, the team, the competition and the rank
    file = open("Agenda.csv", "a")
    familyName = input("Enter Name :\n")
    name = input("Enter firstname :\n")
    phoneNb = input("Enter phone number :\n")
    adresse = input("Enter adress :\n")
    email = input("Enter email adress :\n")
    file.write("{};{};{};{};{}\n".format(familyName,name,phoneNb,adresse,email))
    file.close()
    # option to add another team
    print("\n\nDo you want to add annother contact? yes/no : ")
    choice = input("")
    if choice == "yes":
        addContact()
    else:
        print("\nalright here's the entire list")
        displayContacts()

# ---------------------------------------------------------------------------------------------------------------------
# MODIFY CONTACT
def tab():
    with open("Agenda.csv", 'r') as Fichier:
        n = []
        p = []
        t = []
        a = []
        m = []

        for line in Fichier.readlines():
            name, firstname, phone, address, mail = line.replace("\n", "").split(";")
            n.append(name)
            p.append(firstname)
            t.append(phone)
            a.append(address)
            m.append(mail)

    return n, p, t, a, m

def renew_file(a, b, c, d, e):
    """
    La fonction renouvelle le fichier csv en utilisant les elements présents en parametres.
    :param a: list
    :param b: list
    :param c: list
    :param d: list
    :param e: list
    :return: ecrire dans le fichier csv
    """
    with open("Agenda.csv", "w") as fichier:
        for i in range(len(a)):
            fichier.write("{};{};{};{};{}\n".format(a[i], b[i], c[i], d[i], e[i]))

def show(x):

    compt = []
    mot = []
    name, firstname, phone, address, mail = tab()
    for elem in name, firstname:
        for a, b in enumerate(elem):
            if x.lower() == b.lower():
                print("Name: {}".format(name[a]))
                print("Firstname: {}".format(firstname[a]))
                print("phone: {}".format(phone[a]))
                print("Adress: {}".format(address[a]))
                print("Email Adress: {}\n".format(mail[a]))
                compt.append(a)
                mot.append(b)

    return compt, mot

def modifyContact():

    contact_modify = str
    Find = False
    g = True
    while g:
        name, firstname, phone, address, mail = tab()
        contact_modify = input("Which contact do you want to modify? ")
        for elem in name, firstname:
            for a, b in enumerate(elem):
                if contact_modify.lower() == b.lower():
                    print("\nhere's the contacts info {}".format(b))
                    ind_elem, element = show(b)
                    Find = True
                    if len(ind_elem) > 1:
                        print("You have numerous {} in your contact list, Which one do you want to modify?".format(b))
                        for h, j in enumerate(element):
                            print("\n{}- {} {}".format(h, name[ind_elem[h]], firstname[ind_elem[h]]))
                        modification = int(input("\nWhich one do you want to modify? ---> "))
                        element_modifie = ind_elem[modification]

                    else:
                        element_modifie = ind_elem[0]
                    choix_user = input("\nDo you still want to modify the contacts info? (yes/no) ---> ")
                    if choix_user.lower() == "yes":
                        elem_modify = int(input("What do you want to modify?"
                                                "\n1- Name"
                                                "\n2- Firstname"
                                                "\n3- Phone"
                                                "\n4- Adress"
                                                "\n5- Email adress"
                                                "\nVotre choix! ---> "))

                        if elem_modify == 1:
                            new_name = input("enter new name: ")
                            name[element_modifie] = new_name
                        elif elem_modify == 2:
                            new_prenom = input("Enter new firstname: ")
                            firstname[element_modifie] = new_prenom
                        elif elem_modify == 3:
                            new_phone = input("Enter new phone number: ")
                            phone[element_modifie] = new_phone
                        elif elem_modify == 4:
                            new_address = input("Enter new adress: ")
                            address[element_modifie] = new_address
                        elif elem_modify == 5:
                            new_mail = input("Enter new email adress: ")
                            mail[element_modifie] = new_mail

                        renew_file(name, firstname, phone, address, mail)

                        g = False

                    elif choix_user.lower() == "no":
                        break
                    break
                g = False

    while Find is False:
        ajout = input("\n '{}' isn't in your contact list do you want to add him/her to your contact list? (yes/no)\n ---> ".format(contact_modify))
        if ajout.lower() == "yes":
            addContact()
            Find = True
        elif ajout.lower() == "no":
            Find = True

# ---------------------------------------------------------------------------------------------------------------------
# SEARCH FUNCTIONS

# search by Family Name
def searchByFamilyName():
    FamilyName = input("enter Family Name : ")
    file = csv.reader(open("Agenda.csv", "r"), delimiter=';')
    for row in file:
        if searchByFamilyName() == row[0]:
            print(row)

# search by Name
def searchByName():
    name = input("enter name : ")
    file = csv.reader(open("Agenda.csv", "r"), delimiter=';')
    for row in file:
        if name == row[1]:
            print(row)

# search by phone number
def searchByPhoneNB():
    phoneNb = input("enter phone number : ")
    file = csv.reader(open("Agenda.csv", "r"), delimiter=';')
    for row in file:
        if phoneNb == row[2]:
            print(row)

# search by adress
def searchByAdress():
    adress = input("enter adress : ")
    file = csv.reader(open("Agenda.csv", "r"), delimiter=';')
    for row in file:
        if adress == row[3]:
            print(row)

# search by email adress
def searchByEmail():
    email = input("enter email : ")
    file = csv.reader(open("Agenda.csv", "r"), delimiter=';')
    for row in file:
        if email == row[4]:
            print(row)

# ---------------------------------------------------------------------------------------------------------------------
# SEARCH MENU FUNCTION
# gives you the choice for what you're looking for, a sport, a team, a competition or the ranking

def search():
    print("Enter 1 to search by Family Name")
    print("Enter 2 to search by Name")
    print("Enter 3 to search by phone Number")
    print("Enter 4 to search by adress")
    print("Enter 5 to search by email adress")

    src = int(input('Enter here : '))

    if src == 1:
        searchByFamilyName()
    elif src == 2:
        searchByName()
    elif src == 3:
        searchByPhoneNB()
    elif src == 4:
        searchByAdress()
    elif src == 6:
        searchByEmail()
    else:
        print('sorry invalid input')


# ---------------------------------------------------------------------------------------------------------------------
# DELETE CONTACT

def deleteContact():

    element_modifie = int
    fini = False
    id_elem = []
    element = []
    name, firstname, phone, address, mail = tab()
    c_delete = input("Who do you want to delete? ")
    for elem in name, firstname:
        for a, b in enumerate(elem):
            if c_delete.lower() == b.lower():
                id_elem.append(a)
                element.append(b)

    while fini is False:
        if len(id_elem) > 1:
            print("You have numerous {} in your contact list.\n".format(c_delete))
            for h, j in enumerate(element):
                print("{} {} {}\n".format(h, name[id_elem[h]], firstname[id_elem[h]]))
            modification = int(input("\nWhich one do you want to delete? ---> "))
            element_modifie = id_elem[modification]
            fini = True

        else:
            element_modifie = id_elem[0]
            break

    for i in name, firstname, phone, address, mail:
        i.remove(i[element_modifie])

    renew_file(name, firstname, phone, address, mail)


# ---------------------------------------------------------------------------------------------------------------------
# DELETE ALL CONTACTS`

def reEnterPassword():
    pswd = '12345'
    password = input('re-enter password: ')
    if password == pswd:
        with open("Agenda.csv", "w") as f:
            f.write("Nom;Prenom;Telephone;Adresse;Email\n")
    return password



def deleteAllContacts():
    pswd = '12345'
    ch = False
    while ch is False:
        user_choice = input("Are you sure you want to delete all of your contacts? (yes/no)\n---> ")
        if user_choice.lower() == "yes":
            password = input('password:')
            while(password!=pswd):
                print("Wrong password")
                password = reEnterPassword()
                if password == pswd:
                    with open("Agenda.csv", "w") as f:
                        f.write("Nom;Prenom;Telephone;Adresse;Email\n")
                        ch = True

        elif user_choice.lower() == "no":
            ch = True

    displayContacts()

# ---------------------------------------------------------------------------------------------------------------------
# MENU
# gives you the choice to choose and when done calls the function loop to either quit or remake a choice
def menu():
    print("Enter 0 to quit")
    print("enter 1 to see contact list")
    print("Enter 2 to modify a contact")
    print("Enter 3 to search a contact")
    print("Enter 4 to add a contact")
    print("Enter 5 to delete a contact")
    print("Enter 6 to delete all contacts")
    choix = int(input("----> "))
    if choix == 0:
        print("\nWe hope you had fun, see you next time!")
        quit()
    elif choix == 1:
        displayContacts()
        loop()
    elif choix == 2:
        modifyContact()
        loop()
    elif choix == 3:
        search()
        loop()
    elif choix == 4:
        addContact()
        loop()
    elif choix == 5:
        deleteContact()
        loop()
    elif choix == 6:
        deleteAllContacts()
        loop()

# ---------------------------------------------------------------------------------------------------------------------
# LOOPING MENU FUNCTION
# gives you the choice to come back to the menu after an action

def loop():
    print("\n\nDo you want to go back to the menu? yes/no : ")
    choice = input("")
    if choice == "yes":
        menu()
    else:
        print("\nWe hope you had fun, see you next time!")
        quit()

# ---------------------------------------------------------------------------------------------------------------------
# MAIN
def main():
    print("\nWelcome to Sports Illustrated ")
    print("- we strive to bring the trends, news, and articles that are relevant to any sports fan.\n")
    menu()

main()
