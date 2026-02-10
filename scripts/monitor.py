#!/usr/bin/env python3

import os
from datetime import datetime

LOG_FILE = "/home/devops-monitoring-project/logs/system_health.log"

CPU_THRESHOLD = 1.5
MEM_THRESHOLD = 80
DISK_THRESHOLD = 80


def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}"
    print(log_entry)
    with open(LOG_FILE, "a") as f:
        f.write(log_entry + "\n")


def main():
    log_message("DevOps Monitoring Script Started")
    log_message("Checking system health...")

    # CPU
    cpu_load = os.getloadavg()[0]
    log_message(f"CPU Load (1 min average): {cpu_load}")

    if cpu_load > CPU_THRESHOLD:
        log_message("ALERT: High CPU usage detected!")
    else:
        log_message("CPU usage is normal.")

    # Memory
    with open("/proc/meminfo") as f:
        meminfo = f.readlines()

    mem_total = int(meminfo[0].split()[1])
    mem_free = int(meminfo[1].split()[1])

    used_memory_percent = ((mem_total - mem_free) / mem_total) * 100
    log_message(f"Memory Usage: {used_memory_percent:.2f}%")

    if used_memory_percent > MEM_THRESHOLD:
        log_message("ALERT: High Memory usage detected!")
    else:
        log_message("Memory usage is normal.")

    # Disk
    stat = os.statvfs("/")
    disk_total = stat.f_blocks * stat.f_frsize
    disk_free = stat.f_bfree * stat.f_frsize
    disk_used_percent = ((disk_total - disk_free) / disk_total) * 100

    log_message(f"Disk Usage: {disk_used_percent:.2f}%")

    if disk_used_percent > DISK_THRESHOLD:
        log_message("ALERT: High Disk usage detected!")
    else:
        log_message("Disk usage is normal.")


if __name__ == "__main__":
    main()
