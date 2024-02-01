# Mozaik: Revolutionizing Content Creation with AI

[![Django CI](https://github.com/sezer-muhammed/Anadolu-Ajans--Medya-Teknolojileri-hackathon/actions/workflows/django.yml/badge.svg)](https://github.com/sezer-muhammed/Anadolu-Ajans--Medya-Teknolojileri-hackathon/actions/workflows/django.yml)

## Usage

This script is designed for users with a specific setup, including Windows Subsystem for Linux (WSL), Docker, Python, Git installed, and authorized access to a specific GitHub repository. Follow the steps below to use the `AnadoluAjansi.bat` batch script effectively:

1. **Pre-requisites:**
   - Ensure that you have **Windows Subsystem for Linux (WSL)** installed and configured on your Windows machine.
   - Make sure **Docker** is installed and set up to run on your system. Docker Desktop for Windows is recommended for ease of use.
   - **Python** must be installed and accessible from the command line. This script assumes Python is added to the system's PATH.
   - **Git** should be installed and configured for command line use, with access to clone and pull from repositories.
   - You must have **authorization** to access the `https://github.com/sezer-muhammed/Anadolu-Ajans--Medya-Teknolojileri-hackathon.git` repository, either through SSH keys or HTTPS credentials saved in your Git configuration.

2. **Running the Script:**
   - Locate the `AnadoluAjansi.bat` file. If you do not have it, you may need to download or copy it from the provided source.
   - Double-click the `AnadoluAjansi.bat` file to run it. Ensure you do this within a user account that has the necessary permissions for all operations the script will attempt (e.g., accessing Docker, modifying files, running network commands).

3. **What Happens Next:**
   - The script automatically checks for network connectivity, ensuring you are connected to the internet.
   - It verifies the installations of Docker, Git, and Python, providing instructions if any are not found.
   - Docker Desktop is started, and the script waits until it is ready.
   - The script sets the code page to UTF-8 to handle special characters correctly.
   - A Docker container is run with specific environment variables and volume mappings.
   - It checks for the existence of the specified Git repository locally. If not found, it clones the repository; if it exists, it updates it with the latest changes.
   - The script navigates to the project directory, installs required Python packages, and starts a Django web server.
   - After waiting a brief period for the server to start, it automatically opens the project's upload page in your default web browser.

4. **After Execution:**
   - Wait until your web browser opens the project's upload page automatically. This indicates the script has completed its tasks, and the Django server is running.
   - If the page does not open, check the command line output for any error messages that might indicate what went wrong.

**Note:** This script assumes a certain level of familiarity with command line operations and may require administrative privileges for some operations (such as installing software or starting services). Ensure you understand the actions performed by the script before running it, as it will make changes to your system's configuration and start services automatically.

## Ethical Considerations

At Mozaik, we're committed to ethical AI use. We continually monitor our models to prevent the generation of content that includes unacceptable levels of violence or sexual content. Our goal is to foster a positive and creative environment for all users.

## Mozaik License Agreement

Mozaik is free for personal use. For commercial applications, please contact us to discuss licensing arrangements. We're committed to fair use and fostering a creative and collaborative community.

## Acknowledgments

Special thanks to the Anadolu Agency Hackathon for the inspiration and opportunity to develop Mozaik. We're excited to contribute to the future of AI-driven content creation and distribution.

Join us in revolutionizing content creation with Mozaik - your platform for creativity and innovation.
