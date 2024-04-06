
# Installation and Running
---
- Install [Docker](https://docs.docker.com/engine/install/) using Docker Desktop on Windows or your native package manager on Linux
- Build the Docker Compose file using `docker compose build` and run the containers using `docker compose up`
- Access the Backend endpoint using `http://0.0.0.0:8000/`

# For Development
---
Install Python

Make a virtual environment and activate it
- Windows
```sh
python -m venv venv
venv\Scripts\activate.bat # For Command Prompt
venv\Scripts\activate.ps1 # For powershell
```
- Linux (using Bash)
```bash
python -m venv venv
source venv/bin/activate
```
Install the required packages
```sh
python -m pip install --upgrade pip
pip install -r requirements.txt
```
