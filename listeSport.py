import csv


# DISPLAY FUNCTION

def displayFile():
    file = open("listeSport.csv", "r")
    for line in file:
        tab = line.split(";")
        print("{} {} {} {}".format(tab[0], tab[1], tab[2], tab[3]))
    file.close()


# ---------------------------------------------------------------------------------------------------------------------

# ADDING FUNCTION

def addTeam():
    # enter the elements needed, the sport, the team, the competition and the rank
    file = open("listeSport.csv", "a")
    sport = input("Enter sport :\n")
    team = input("Enter name :\n")
    competition = input("Enter competition :\n")
    rank = input("Enter rank :\n")
    file.write("{};{};{};{}\n".format(sport, team, competition, rank))
    file.close()
    # option to add another team
    print("\n\nDo you want to add annother team? yes/no : ")
    choice = input("")
    if choice == "yes":
        addTeam()
    else:
        print("\nalright here's the entire list")
        displayFile()


# ---------------------------------------------------------------------------------------------------------------------

# SEARCH FUNCTIONS

# search the sport
def searchBySport():
    sport = input("enter sport : ")
    file = csv.reader(open("listeSport.csv", "r"), delimiter=';')
    for row in file:
        if sport == row[0]:
            print(row)


# search the team
def searchByTeam():
    team = input("enter team : ")
    file = csv.reader(open("listeSport.csv", "r"), delimiter=';')
    for row in file:
        if team == row[1]:
            print(row)


# search the competition
def searchByCompetition():
    competition = input("enter competition : ")
    file = csv.reader(open("listeSport.csv", "r"), delimiter=';')
    for row in file:
        if competition == row[2]:
            print(row)


# search the ranking
def searchByRank():
    rank = input("enter Rank : ")
    competition = input("enter competition : ")
    file = csv.reader(open("listeSport.csv", "r"), delimiter=';')
    for row in file:
        if rank == row[3] and competition == row[2]:
            print("the {} in {}".format(rank, competition))
            print(row)


# ---------------------------------------------------------------------------------------------------------------------

# SEARCH MENU FUNCTION
# gives you the choice for what you're looking for, a sport, a team, a competition or the ranking
def searchMenu():
    print("Enter 1 to search for a sport")
    print("Enter 2 to search for a team")
    print("Enter 3 to search for a competition")
    print("Enter 4 to search the rank in a competition")

    src = int(input('Enter here : '))

    if src == 1:
        searchBySport()
    elif src == 2:
        searchByTeam()
    elif src == 3:
        searchByCompetition()
    elif src == 4:
        searchByRank()
    else:
        print('sorry invalid input')


# ---------------------------------------------------------------------------------------------------------------------

# MENU
# gives you the choice to choose and when done calls the function loop to either quit or remake a choice
def menu():
    print("Enter 0 to quit")
    print("enter 1 to see the entire list of teams")
    print("Enter 2 to search")
    print("Enter 3 to add a team\n")
    choix = int(input("----> "))
    if choix == 0:
        print("\nWe hope you had fun, see you next time!")
        quit()
    elif choix == 1:
        displayFile()
        loop()
    elif choix == 2:
        searchMenu()
        loop()
    elif choix == 3:
        addTeam()
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
