from random import sample


def calculate_members_per_team(number_of_members):
    team_a = int(number_of_members / 2)
    team_b = int(number_of_members - team_a)
    teams = [team_a, team_b]
    return teams


def main():
    # Get the players that are going to play in the custom match
    member_names = input("Insert all players names separated by ', '. E.g: PlayerAlpha, PlayerBeta, PlayerCharlie."
                         "\nPlayers: ")

    member_list = member_names.split(', ')  # Convert the string given by the user into a list with the players as elements

    number_of_members = len(member_list)  # Get the total number of players by counting how many elements are in the string

    if number_of_members <= 10:
        members_per_team = calculate_members_per_team(number_of_members)  # Using the function declared before to calculate how many players have to be in each team

        member_list = sample(member_list, k=number_of_members)  # Randomly orders the list using the function 'sample()' from the library 'random'

        team_a = []
        team_b = []

        i = members_per_team[0] - 1
        while i >= 0:
            team_a.append(member_list[i])
            member_list.remove(member_list[i])
            i -= 1

        i = members_per_team[1] - 1
        while i >= 0:
            team_b.append(member_list[i])
            i -= 1

        """Print the result"""
        players_team_a = ', '.join(team_a)
        players_team_b = ', '.join(team_b)
        print("Team A: {}"
              "\nTeam B: {}".format(players_team_a, players_team_b))

    else:
        print("Number of players exceeded, maximum is 10")

    """Just for debugging"""
    print("Number of players: {}".format(number_of_members))
    # print(members_per_team)


if __name__ == '__main__':
    main()
