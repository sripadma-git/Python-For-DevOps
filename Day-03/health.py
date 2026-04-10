import psutil
import logging

# Configure logging for better DevOps practices
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def check_cpu_usage(threshold=80):
    """Checks the current CPU usage and alerts if above threshold."""
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        if cpu_usage > threshold:
            logging.warning(f"High CPU usage detected: {cpu_usage}%")
        else:
            logging.info(f"CPU Usage is normal: {cpu_usage}%")
    except Exception as e:
        logging.error(f"Could not retrieve CPU metrics: {e}")

def check_disk_usage(path="/"):
    """Checks disk usage for a given path."""
    try:
        disk_info = psutil.disk_usage(path)
        usage_percent = disk_info.percent
        
        if usage_percent > 90:
            logging.warning(f"Disk space is running low: {usage_percent}%")
        else:
            logging.info(f"Disk Usage: {usage_percent}%")
    except FileNotFoundError:
        logging.error(f"The path '{path}' was not found.")
    except Exception as e:
        logging.error(f"An unexpected error occurred while checking disk: {e}")

def main():
    """Main execution block."""
    print("--- System Health Check Starting ---")
    check_cpu_usage()
    check_disk_usage()
    print("--- Health Check Complete ---")

if __name__ == "__main__":
    main()