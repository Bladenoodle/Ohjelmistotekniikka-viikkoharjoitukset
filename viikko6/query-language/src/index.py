from player_reader import PlayerReader
from statistics_1 import Statistics
from matchers import And, PlaysIn, HasAtLeast, Not, HasFewerThan, All, Or

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players.txt"

    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = And(
        Not(HasAtLeast(2, "goals")),
        PlaysIn("NYR")
    )

    print("Testi 1:")
    for p in stats.matches(matcher):
        print(p)
    print()

    matcher = And(
        HasFewerThan(2, "goals"),
        PlaysIn("NYR")
    )

    print("Testi 2:")
    for p in stats.matches(matcher):
        print(p)
    print()

    print("Testi 3 (All):")
    print(len(stats.matches(All())))
    print()
    
    print("Testi 4.1 (Or):")
    matcher = Or(
        HasAtLeast(45, "goals"),
        HasAtLeast(70, "assists")
    )

    for player in stats.matches(matcher):
        print(player)

    print("Testi 4.2 (Or):")

    matcher = And(
    HasAtLeast(70, "points"),
    Or(
        PlaysIn("COL"),
        PlaysIn("FLA"),
        PlaysIn("BOS")
    )
    )
    for player in stats.matches(matcher):
        print(player)

if __name__ == "__main__":
    main()
