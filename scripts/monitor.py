#!/usr/bin/env python3

import os
from datetime import datetime

LOG_FILE = "/home/devops-monitoring-project/logs/system_health.log"

def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}"
    print(log_entry)
    with open(LOG_FILE, "a") as f:
        f.write(log_entry + "\n")

log_message("DevOps Monitoring Script Started")
log_message("Checking system health...")

# CPU Monitoring
cpu_load = os.getloadavg()[0]
log_message(f"CPU Load (1 min average): {cpu_load}")

if cpu_load > 1.5:
    log_message("ALERT: High CPU usage detected!")
else:
    log_message("CPU usage is normal.")

# Memory Monitoring
with open("/proc/meminfo") as f:
    meminfo = f.readlines()

mem_total = int(meminfo[0].split()[1])
mem_free = int(meminfo[1].split()[1])

used_memory = mem_total - mem_free
used_memory_percent = (used_memory / mem_total) * 100

log_message(f"Memory Usage: {used_memory_percent:.2f}%")

if used_memory_percent > 80:
    log_message("ALERT: High memory usage detected!")
else:
    log_message("Memory usage is normal.")

# Disk Monitoring
st = os.statvfs('/')
total_disk = st.f_blocks * st.f_frsize
free_disk = st.f_bavail * st.f_frsize
used_disk = total_disk - free_disk

disk_usage_percent = (used_disk / total_disk) * 100

log_message(f"Disk Usage: {disk_usage_percent:.2f}%")

if disk_usage_percent > 80:
    log_message("ALERT: High disk usage detected!")
else:
    log_message("Disk usage is normal.")
if __name__ == "__main__":
    main()
