import WinScript

Script = WinScript.Win()

#taskkill notepad
Script.Execute("taskkill /F /IM notepad.exe")

#set list
Script.SetList("testlist", [1, 2, 3, 4])

#for loop testlist
Script.ForList("a", "testlist")
Script.Execute("echo %%a")
Script.End(2)

#add pause
Script.Pause()

#generate script
Script.CreateScript()