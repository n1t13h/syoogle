import time
import definitions

class Logger:

    def on_start(self,name):
        self.name = name
        with open(definitions.ROOT_DIR + "game.txt","a") as file:
            file.write("\n##################################### SESSION STARTED #####################################")
            curr_time = time.strftime("%m/%d/%y %r")
            file.write("\n recorded time and date - {}".format(curr_time))
            file.write("\n Game started by {}".format(self.name))

    def add_message(self,message):
        with open(definitions.ROOT_DIR + "game.txt","a") as file:
            file.write(message)

    def on_end(self):
        with open(definitions.ROOT_DIR + "game.txt","a") as file:
            file.write("\n##################################### SESSION ENDED #####################################")
            curr_time = time.strftime("%m/%d/%y %r")
            file.write("\n recorded time and date - {}".format(curr_time))