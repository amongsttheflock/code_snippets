from itertools import combinations


def people():
    people = []
    while True:
        print("### If you finish entering players names - type 'exit'.")
        print("We have aready {} players in the game!".format(len(people)))
        name = input("Enter player's name: ")
        print("")
        if name == "exit":
            break
        else:
            people.append(name)
    return people



def evr_vs_evr(players):
    #  prawie skończone - główne założenia każdy z każdym działają.
    matches = list(combinations(players, 2))
    wins = {k: 0 for k in players}
    for p1, p2 in matches:
        print("Match between {} and {}".format(p1, p2))
        winner = input("The winner is: ")
        #  zabezpieczyć możliwość wprowadzenia błędnego imienia!
        wins[winner] += 1
    table = sorted(wins.items(), key=lambda x: x[1], reverse="True")
    print("\nTABELA WYNIKÓW: ")
    for player, score in table:
        print("{} - {} points.".format(player, score))


def rounds(people):
    nextround = []
    if len(people) % 2 == 0:
        for i in range(0, len(people), 2):
            print("Match between {} and {}".format(people[i], people[i + 1]))
            winner = input("The winner is: ")
            nextround.append(winner)
    return nextround


def main():
    players = people()
    # print("Yaaay, we have {} and {} in the game!\n".format(", ".join(people[:-1]) if len(people) > 2 else people[0], people[-1]))
    if len(players) < 6:
        evr_vs_evr(players)
    elif len(players) == 6:
        evr_vs_evr(rounds(players))
    else:
        pass
