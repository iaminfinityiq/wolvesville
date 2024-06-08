import tkinter
import random
import pyttsx3

class Role:
    def __init__(self, name):
        global roles
        self.name = name
        VILLAGE = ["Doctor", "Hunter", "Jailer", "Seer", "Aura Seer", "Medium", "Avenger", "Loudmouth", "Flower Child", "Cupid"]
        WEREWOLF = ["Junior Werewolf", "Protector Wolf", "Wolf Shaman", "Wolf Seer"]
        VOTING = "Fool"
        KILLER = "Evil Detective"
        GOOD = ["Doctor", "Seer", "Aura Seer", "Avenger", "Loudmouth", "Flower Child", "Cupid"]
        UNKNOWN = ["Hunter", "Jailer", "Medium", "Protector Wolf", "Fool", "Evil Detective"]
        EVIL = ["Junior Werewolf", "Wolf Shaman", "Wolf Seer"]
        if self.name in VILLAGE:
            self.team = "Village"
        if self.name in WEREWOLF:
            self.team = "Werewolves"
        if self.name in VOTING:
            self.team = "Voting"
        if self.name in KILLER:
            self.team = "Killer"
        if self.name in GOOD:
            self.aura = "Good"
        if self.name in UNKNOWN:
            self.aura = "Unknown"
        if self.name in EVIL:
            self.aura = "Evil"

        self.description = {
            "Doctor": """Name: Doctor
Team: Village
Aura: Good
Ability: At night, you can choose a player to protect from attacks at night. You can't protect yourself and protect attacks from villagers at night.""",
            "Hunter": """Name: Hunter
Team: Village
Aura: Unknown
Ability: Once per game, at night, you can choose to hunt one player, that player will die at the end of the night. You can choose to hunt yourself""",
            "Jailer": """Name: Jailer
Team: Village
Aura: Unknown
Ability: At night, you can choose a player to be interviewed. You can ask some questions to that player. Once per game, you can choose to shoot that player, which kills them.""",
            "Seer": """Name: Seer
Team: Village
Aura: Good
Ability: At night, you can select a player to uncover their role. Their role will only be revealed to you.""",
            "Aura Seer": """Name: Aura Seer
Team: Village
Aura: Good
Ability: At night, you can select a player to uncover their aura. Their aura will only be revealed to you.""",
            "Medium": """Name: Medium
Team: Village
Aura: Unknown
Ability: At night, you can talk to the deads for some time. Once per game, at night, you can choose to revive a player at the end of that night.""",
            "Avenger": """Name: Avenger
Team: Village
Aura: Good
Ability: At night, you can choose a player as your target. When you die, that player also dies with you.""",
            "Loudmouth": """Name: Loudmouth
Team: Village
Aura: Good
Ability: At night, you can choose a player as your target. When you die, that player's role will be revealed to everyone.""",
            "Flower Child": """Name: Flower Child
Team: Village
Aura: Good
Ability: At night, you can protect a player from any attacks until the end of the game. When the player is attacked, they are no longer protected by you.""",
            "Cupid": """Name: Cupid
Team: Village
Aura: Good
Ability: At the first night, the system will randomly select a couple. If a player from the couple dies, the other also dies. If they are the only one alive, they win the whole game.""",
            "Junior Werewolf": """Name: Junior Werewolf
Team: Werewolves
Aura: Evil
Ability: At night, you can choose your target who will die with you when you die.""",
            "Protector Wolf": """Name: Protector Wolf
Team: Werewolves
Aura: Unknown
Ability: At night, you can choose a player to protect from attacks at night. You can't protect yourself and protect attacks from villagers at night.""",
            "Wolf Shaman": """Name: Wolf Shaman
Team: Werewolves
Aura: Evil
Ability: At night, you can choose a player to be shamaned. This player when checked by Seer and Aura Seer appears to be Wolf Shaman.""",
            "Wolf Seer": """Name: Wolf Seer
Team: Werewolves
Aura: Evil
Ability: At night, you can choose a player to reveal their role. Their role will only be revealed to other werewolves.""",
            "Fool": """Name: Fool
Team: Fool
Aura: Unknown
Ability: Your goal is to get the village lynch you. If you get lynched, you win.""",
            "Evil Detective": """Name: Evil Detective
Team: Evil Detective
Aura: Unknown
Ability: At night, you can choose 2 players. If they have different teams, they die. Otherwise their team will be revealed to you."""
        }[self.name]

def reset():
    global roles, votes, protected, avenger_target, loudmouth_target, flower_child_target, medium_target, couple, night, day
    roles = [
        Role("Doctor"),
        Role("Hunter"),
        Role("Jailer"),
        Role("Seer"),
        Role("Aura Seer"),
        Role("Medium"),
        Role("Avenger"),
        Role("Loudmouth"),
        Role("Flower Child"),
        Role("Cupid"),
        Role("Junior Werewolf"),
        Role("Protector Wolf"),
        Role("Wolf Shaman"),
        Role("Wolf Seer"),
        Role("Fool"),
        Role("Evil Detective")
    ]
    random.shuffle(roles)
    votes = {i: 0 for i in range(16)}
    protected = []
    avenger_target = None
    loudmouth_target = None
    flower_child_target = None
    medium_target = None
    couple = []
    night = 1
    day = 0

wd = tkinter.Tk()
wd.title("Wolvesville")
engine = pyttsx3.init()

reset()

wd.mainloop()
