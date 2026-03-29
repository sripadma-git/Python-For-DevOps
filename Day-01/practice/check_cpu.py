import psutil


def get_cpu_threshold():
    cpu_threshold = int(input("Enter the CPU Threshold")) 
    current_cpu = psutil.cpu_percent(interval=1)
    print("current CPU %:", current_cpu)

    if current_cpu > cpu_threshold:
        print("CPU Alert Email sent...")
    else:
        print("CPU is under control...")

get_cpu_threshold()