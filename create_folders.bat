@echo off
setlocal enabledelayedexpansion

:: Base directory where all the day folders will be created
:: Change this path if you want the folders to be created elsewhere
set "BASE_DIR=."

:: Total number of days to create folders for
set "TOTAL_DAYS=100"

:: Loop through days 1 to TOTAL_DAYS
for /L %%D in (1,1,%TOTAL_DAYS%) do (
    :: Format the day number with leading zero (e.g., Day 01, Day 02, ...)
    set "DAY=%%D"
    if !DAY! lss 10 set "DAY=0!DAY!"

    :: Define the path for the day's main directory
    set "DAY_DIR=%BASE_DIR%\Day !DAY!"

    :: Check if the day's directory already exists
    if not exist "!DAY_DIR!" (
        :: Create the main directory for the day
        mkdir "!DAY_DIR!"
        if errorlevel 1 (
            echo Failed to create directory "!DAY_DIR!".
            exit /b 1
        )
        echo Created directory "!DAY_DIR!".
    ) else (
        echo Directory "!DAY_DIR!" already exists. Skipping creation.
    )

    :: Check and create 'Exercises' subfolder if it doesn't exist
    if not exist "!DAY_DIR!\Exercises" (
        mkdir "!DAY_DIR!\Exercises"
        if errorlevel 1 (
            echo Failed to create subdirectory "!DAY_DIR!\Exercises".
            exit /b 1
        )
        echo Created subdirectory "!DAY_DIR!\Exercises".
    ) else (
        echo Subdirectory "!DAY_DIR!\Exercises" already exists. Skipping creation.
    )

    :: Check and create 'Project' subfolder if it doesn't exist
    if not exist "!DAY_DIR!\Project" (
        mkdir "!DAY_DIR!\Project"
        if errorlevel 1 (
            echo Failed to create subdirectory "!DAY_DIR!\Project".
            exit /b 1
        )
        echo Created subdirectory "!DAY_DIR!\Project".
    ) else (
        echo Subdirectory "!DAY_DIR!\Project" already exists. Skipping creation.
    )

    :: Create README.md only if it doesn't exist
    if not exist "!DAY_DIR!\README.md" (
        (
            echo # Day !DAY!
            echo This folder contains the Topics for Day !DAY!.
        ) > "!DAY_DIR!\README.md"
        echo Created README.md for Day !DAY!.
    ) else (
        echo README.md already exists for Day !DAY!. Skipping creation.
    )

    echo ----------------------------------------
)

echo.
echo Folder structure for days 1 to %TOTAL_DAYS% has been processed.
pause
