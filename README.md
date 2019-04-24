# Deployment
- Copy master files to repo to destination
- Make sure Python 3, pip, pipenv are installed
- Provide API keys:
  - Octoprint - File name must be `octoprint-api-key` and must contain only the key
  - Google API - Provide a Google API credentials file. This file is downloaded from the Google API Service account key related to your Google API Project which must have access to read and write on Google Sheets and Google Drive. File must be renamed to `OctoprintReporting-GoogleAPI-credentials.json`.
- To execute, use run.bat (Windows) or run.sh (Linux).
  - On Linux make sure that the run.sh is executable. Do this with: `chmod +x run.sh`
  - Running automatically on Linux - You can make a chrontab edit to this with `chrontab -e` then then add this line (runs every hour) --> `*/1 * * * * . cd <location of run.sh> && ./run.sh > <location log file>/octoprint-crontab-log.txt 2>&1`
    - To run every 2 hrs use this instead --> `0 */2 * * *`
    - To run every day at midnight --> `0 0 * * *1`
  - Running automatically on Windows - Use Task Scheduler. Add any condition of choice then add the action:
    - Program/script - `".\run.bat"`
    - Start in - `C:\Users\sparc\Documents\Python Scripts\octo-print-reporting`

# Links
- Project Drive directory containing my private spreadsheet and API keys:
  - https://drive.google.com/drive/folders/1jjrGEm1GOYuwre_8iOc9Bc-qpjF-c5u9
