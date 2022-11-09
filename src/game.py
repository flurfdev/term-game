import sys
import os
import random
import time
import pickle

versionNumber = "1.egg"


def intro():
    print('''   ___                                  ___               _ _ _             ''')
    time.sleep(.1)
    print('''  / _ \_   _ _ __   ___   ___  ___     /   \__      _____| | (_)_ __   __ _ ''')
    time.sleep(.1)
    print(''' / /_)/ | | | '_ \ / _ \ / _ \/ __|   / /\ /\ \ /\ / / _ \ | | | '_ \ / _` |''')
    time.sleep(.1)
    print('''/ ___/| |_| | |_) | (_) | (_) \__ \  / /_//  \ V  V /  __/ | | | | | | (_| |''')
    time.sleep(.1)
    print('''\/     \__, | .__/ \___/ \___/|___/ /___,'    \_/\_/ \___|_|_|_|_| |_|\__, |''')
    time.sleep(.1)
    print('''       |___/|_|                                                       |___/ ''')
    time.sleep(.1)
    print('')
    time.sleep(.1)
    print(f'By Crepe & Floof - Version {versionNumber}')
    time.sleep(.1)
    print('')
    pass


class Game:
    def __init__(self) -> None:
        self.curRoom = 'trail_in_woods'
        self.lastRoom = ''
        self.curMenu = "lobby"
        self.isExamining = False
        self.key = 0             # how many keys you have
        self.confidence = 0      # 0 = neutral, 10 = high, -10 = low
        self.battery = 100       # battery percentage
        self.flashlight = 0      # on or off
        self.showedMessage = False
        self.usernames = ['', '', '']
        self.passwords = ['', '', '']
        self.commands = ['help', 'exit', 'move',
            'directions', 'intro', 'examine', 'desc', 'clear']
        # self.rooms = ['Trail in Woods']
        self.commandDesc = ['Lists all the useful commands', 'Quits the game', 'Moves NORTH, WEST, SOUTH, or EAST',
            'Lists the directions you can use', 'Runs the intro again', 'Examines a room for useful items', 'Gives a description of the current room', 'Clears the terminal']
        self.chosenUser = random.choice(self.usernames)
        self.chosenPass = random.choice(self.passwords)
        self.sleepTime = 1
        self.menus = {"lobby": self.lobby, "game": self.game}
        self.roomDesc = {"trail_in_woods": self.trail_in_woods}

        intro()
    pass

    def lobby(self):
        print('')
        time.sleep(self.sleepTime)
        print('''●●●●●●●●●●●●●●●●●●●●●''')
        print('''You are in the lobby.''')
        time.sleep(self.sleepTime)
        print('[Play the game? - /play]')
        time.sleep(self.sleepTime)
        print('[Rules - /rules]')
        time.sleep(self.sleepTime)
        print('[Load Game - /load]')
        time.sleep(self.sleepTime)
        print('[Settings - /settings]')
        time.sleep(self.sleepTime)
        print('')
        inp = input('> ')
        print('')

        match(inp):
            case "play":
                os.system("clear" or "cls")
                self.curMenu = "game"

    def trail_in_woods(self):
        if self.isExamining:
            print("The trees are swaying, the house is creaking, and you're scared.")
            time.sleep(self.sleepTime)
        else:
            # Description
            time.sleep(self.sleepTime)
            print('''It's a dark and windy night, and you're standing in the middle of the woods with a flashlight.''')
            time.sleep(self.sleepTime)
            print('''There's an abandoned house right in front of you. You can go straight, left, or right. What do you do?''')
            time.sleep(self.sleepTime)

        pass

    def get_menu(self, key):
        return self.menus.get(key, f'Invalid menu: {key}')

    def run(self):
        while True:
            c = self.get_menu(self.curMenu)

            c()

    def get_room_desc(self, key):
        return self.roomDesc.get(key, f'Invalid room: {key}')

    def game(self):

        if not self.showedMessage:
            try:
                r: function = self.get_room_desc(self.curRoom)

                r()
                self.showedMessage = True
            except:
                # Do nothing
                print("No description for this area")
                pass
        
        print("")
        inp = input(f"~/g/{self.curRoom}$ ")
        print("")


        match(inp):
            case "help":
                print("Here are the commands you can use: \n")
                time.sleep(self.sleepTime)
                for i in range(0,len(self.commands)):
                    print(f'{self.commands[i]}: {self.commandDesc[i]}')
                    time.sleep(self.sleepTime)
                    pass
                time.sleep(self.sleepTime)
            case "exit":
                print("Leaving the game...")
                time.sleep(self.sleepTime)
                sys.exit(0)
            case "desc":
                self.showedMessage = False
            case 'intro':
                print('Running the intro...')
                time.sleep(self.sleepTime)
                intro()
            
            case "clear":
                os.system("clear" or "cls")
            
            case "examine":
                time.sleep(self.sleepTime)
                print("You decide to check your surroundings...\n")
                time.sleep(self.sleepTime)
                try:

                    self.isExamining = True
                    self.get_room_desc(self.curRoom)()
                    self.isExamining = False
                except:
                    print("You found nothing")
                

            case _:
                print(f"Command [{inp}] was not recognized")                

        pass
