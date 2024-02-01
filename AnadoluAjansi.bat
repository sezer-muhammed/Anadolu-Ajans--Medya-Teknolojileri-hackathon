@echo off

REM Set script directory path
set SCRIPT_DIR=%~dp0

REM Create repositories and cache directories if they do not exist
if not exist "%SCRIPT_DIR%repositories\" mkdir "%SCRIPT_DIR%repositories"
if not exist "%SCRIPT_DIR%cache\pip\" mkdir "%SCRIPT_DIR%cache\pip"

REM Convert script directory to a relative path for Docker (if necessary)
REM Example: set RELATIVE_PATH=..\..\DockerVolumes

REM Check for network connectivity
ping -n 1 www.google.com >nul 2>&1
if errorlevel 1 (
    echo You must be connected to the internet to run this script.
    exit /b
)

REM Check for Docker installation and start Docker
where docker >nul 2>&1
if errorlevel 1 (
    echo Docker is not installed. Please install Docker and run this script again.
    exit /b
) else (
    echo Starting Docker...
    start "" "docker"
    REM Add logic to wait for Docker to be ready
)

REM Check for Git installation
where git >nul 2>&1
if errorlevel 1 (
    echo Git is not installed. Please install Git and run this script again.
    exit /b
)

REM Check for Python installation
where python >nul 2>&1
if errorlevel 1 (
    echo Python is not installed. Please install Python and run this script again.
    exit /b
)

REM Start Docker Desktop (if not already started)
echo Starting Docker Desktop...
start "" "C:\Program Files\Docker\Docker\Docker Desktop.exe"

REM Wait for Docker Desktop to be ready
echo Waiting for Docker Desktop to be ready...
:WaitForDocker
timeout /t 1 >nul
docker info >nul 2>&1
if errorlevel 1 goto WaitForDocker
echo Docker Desktop is ready.

REM Set the code page to UTF-8 for handling Turkish characters
echo Setting code page to UTF-8...
chcp 65001

REM Run the Docker container with relative paths
echo Running the Docker container...
docker run -d --gpus=all -e NVIDIA_DRIVER_CAPABILITIES=compute,utility -e NVIDIA_VISIBLE_DEVICES=all -v "%SCRIPT_DIR%repositories:/app/repositories" -v "%SCRIPT_DIR%cache\pip:/root/.cache/pip" -p 8888:8888 konieshadow/fooocus-api

REM Check if the repo exists
echo Checking for existing Git repository...
if not exist "%SCRIPT_DIR%Anadolu-Ajans--Medya-Teknolojileri-hackathon\.git" (
    echo Cloning the repository...
    git clone https://github.com/sezer-muhammed/Anadolu-Ajans--Medya-Teknolojileri-hackathon.git
) else (
    echo Repository found. Pulling latest changes...
    cd Anadolu-Ajans--Medya-Teknolojileri-hackathon
    git pull
    cd ..
)

REM Navigate to the project directory and run the server
echo Navigating to the project directory...

cd Anadolu-Ajans--Medya-Teknolojileri-hackathon

echo Installing and updating Requirements
pip install -r requirements.txt

cd AnadoluAjansiMedyaTeknolojileriWebApp

echo Starting Django server...
start python manage.py runserver

REM Wait a bit for the server to start
timeout /t 10

REM Open the web page
echo Opening web page...
start http://127.0.0.1:8000//GUI/upload
