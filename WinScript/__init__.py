import os

SPACE = " "
INFOR = "\t"

class Win:
    def __init__(self):
        self.ScriptVar = "" 
        pass
    
    def Start(self, args, other=""):
        if other == "":
            # Send with first argument
            self.ScriptVar += f"Start {str(args)}\n"
        elif other != "":
            # Send with other arguments
            self.ScriptVar += f"Start {str(args)} /k {str(other)}\n"
    
    def Pause(self):
        # Pause
        self.ScriptVar += f"Pause\n"
    
    def Execute(self, args):
        # Send command
        self.ScriptVar += args + "\n"

    def Exit(self):
        self.ScriptVar += "exit\n"

    def SetList(self, name, _list: list):
        self.ScriptVar += f"set {name}="
        for i,v in enumerate(_list):
            self.ScriptVar += f"{str(v)} "
        self.ScriptVar += "\n"
    
    def ForList(self, var, name):
        self.ScriptVar += f"(for %%{str(var)} in (%{name}%) do (\n"
    
    def End(self, amount=1):
        string = ""
        for i in range(amount):
            string += ")"
        self.ScriptVar += f"{string}\n"
    
    def CreateScript(self):
        # Create script
        with open("script.bat", "w") as script:
            script.write(self.ScriptVar)
            script.close()

    def Goto(self, var):
        self.ScriptVar += f"goto :{var}\n"
    
    def SetGoto(self, var):
        self.ScriptVar += f":{var}\n"
    
    def SetEcho(self, bool=False):
        if bool == False:
            self.ScriptVar += "@echo off\n"
        else:
            self.ScriptVar += "@echo on\n"

    def Curl(self, site, args=[]):
        argString = ""
        if len(args) == 0:
            self.ScriptVar += "curl" + site + "\n"
        else:
            for i in range(len(args)):
                argString += "--" + args[i] + " "
            self.ScriptVar += "curl" + " " + site + " " + argString + "\n"

    def Remove(self, path):
        self.ScriptVar += f"del \"" + path + "\"\n"

    DATE = "%DATE%"
    TIME = "%TIME%"
    YEAR = "%year%"
    MONTH = "%month%"
    DAY = "%day%"
    LISTEND = 2
    RANDOM = "%RANDOM%"