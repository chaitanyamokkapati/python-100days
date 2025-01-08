@echo off
setlocal enabledelayedexpansion

:: Base directory where all the day folders will be created (optional, you can set it to any directory you want)
set BASE_DIR=.

:: Loop through days 1 to 100
for /L %%D in (1,1,100) do (
    :: Format the day number with leading zero (e.g., Day 01, Day 02, ...)
    set DAY=%%D
    if !DAY! lss 10 set DAY=0!DAY!
    
    :: Create the main directory for the day (e.g., Day 01, Day 02, ...)
    set DAY_DIR=%BASE_DIR%\Day !DAY!
    mkdir "!DAY_DIR!"
    
    :: Create the Exercises and Project subfolders
    mkdir "!DAY_DIR!\Exercises"
    mkdir "!DAY_DIR!\Project"
    
    :: Create a README.md file inside the main Day folder
    echo # Day !DAY! > "!DAY_DIR!\README.md"
    echo This folder contains the Topics for Day !DAY!. >> "!DAY_DIR!\README.md"
    
    :: Feedback to the user (optional)
    echo Created Day !DAY! folder structure.
)

echo Folder structure for days 1 to 100 has been created.
pause
