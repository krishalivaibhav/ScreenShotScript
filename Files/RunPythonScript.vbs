' Create a WshShell object to run external commands
Set WshShell = CreateObject("WScript.Shell")

' Get the directory path where this script is located
currentPath = CreateObject("Scripting.FileSystemObject").GetParentFolderName(WScript.ScriptFullName)

' Run the batch file (automatic.bat) located in the same directory, with no window display
' Chr(34) is used to add double quotes around the path in case it contains spaces
WshShell.Run Chr(34) & currentPath & "\automatic.bat" & Chr(34), 0, False
