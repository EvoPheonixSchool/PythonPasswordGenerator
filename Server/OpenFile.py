# this class will handle opening the file and splitting the data
# Author: Sheldon McGrath
# Last Updated: 17-12-2017
class OpenFile:

    #this method opens the file and returns a file object
    def open(self, filename, filemode):
        file = open(filename, filemode)
        return file


    #this method returns the list of EST values from the file in a list
    def StripEST(self, f):
        file = f
        ESTlist = []
        run = True

        #this loops through reading every line of the file
        #eventually will strip the EST value out and place it in the list
        while run == True:
            line = file.readline()
            # stops loop if end is reached
            if line == "":
                run = False
            else:
                line = line.replace('\n', '')
                ESTlist += line.split(',')

        #sets the file pointer to the start
        file.seek(0)

        return ESTlist
