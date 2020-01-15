import time

class Logger:

    def on_start(self,file):
        with open(root_dir + "game.txt",a) as file:
            file.write("##################################### SESSION STARTED #####################################")
            curr_time = time.strftime("%m/%d/%y %r")
            file.write("\n recorded time and date - {}".format(curr_time))

    def add_message(self,file,message):
        with open(root_dir + "game.txt",a) as file:
            file.write(message)

    def on_end(self,file):
        with open(root_dir + "game.txt",a) as file:
            file.write("##################################### SESSION ENDED #####################################")
            curr_time = time.strftime("%m/%d/%y %r")
            file.write("\n recorded time and date - {}".format(curr_time))