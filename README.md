# DevOps System & Port Monitoring Project

## Project Overview
This project is a Python-based DevOps monitoring solution designed to check system health and port availability on a Linux server. 
It is integrated with Jenkins to automate monitoring tasks and generate logs for operational visibility.

The project simulates real-world DevOps monitoring activities used in production environments.

---

## Technologies Used
- Python
- Linux (RHEL / Ubuntu)
- Jenkins
- Shell Scripting
- Git & GitHub

---

## Features
- System health monitoring (CPU, memory, disk usage)
- Port monitoring to verify service availability
- Log generation for monitoring results
- Jenkins job integration for automated execution
- Linux permission handling for secure log management

---

## How the Project Works
1. Jenkins job triggers the monitoring script
2. Python script checks system metrics and port status
3. Results are written into log files
4. Jenkins console shows execution status (success/failure)

---

## Project Structure
devops-monitoring-project/
|-- scripts/
| |-- monitor.py
|-- logs/
|-- README.md
|-- requirements.txt
|-- .gitignore

---

## How to Run Locally
```bash
pip install -r requirements.txt
python scripts/monitor.py

---

## Security Considerations

- No credentials or sensitive data are stored in the repository
- Logs and environment files are excluded using .gitignore
- Suitable for public GitHub sharing

---

Author

Priyanka Srivastava
Engineer | CI/CD & Monitoring


---

## GitHub push commands (final step)

```bash
git init
git add .
git commit -m "Initial commit: DevOps system and port monitoring project"
git branch -M main
git remote add origin https://github.com/USERNAME/devops-monitoring-project.git
git push -u origin main
