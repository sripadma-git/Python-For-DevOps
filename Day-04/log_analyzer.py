import os

def analyze_log_file(input_file, output_file):
    """Reads a log file and counts occurrences of log levels."""
    
    # Initialize our counters
    log_counts = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    try:
        # 1. Read the log file
        with open(input_file, 'r') as file:
            lines = file.readlines()
            
            if not lines:
                print(f"Warning: The file '{input_file}' is empty.")
                return

            for line in lines:
                # 2. Identify and count log levels
                for level in log_counts.keys():
                    if level in line.upper():
                        log_counts[level] += 1

        # 3. Print summary to terminal
        print(f"\n--- Log Analysis Summary: {input_file} ---")
        for level, count in log_counts.items():
            print(f"{level}: {count}")

        # 4. Write the summary to an output file
        with open(output_file, 'w') as out:
            out.write(f"Log Analysis Report\n")
            out.write(f"Source: {input_file}\n")
            out.write("-" * 20 + "\n")
            for level, count in log_counts.items():
                out.write(f"{level}: {count}\n")
        
        print(f"\nSummary successfully saved to: {output_file}")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied when accessing files.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # You can change these filenames as needed
    INPUT_LOG = "app.log"
    OUTPUT_REPORT = "log_summary.txt"
    
    analyze_log_file(INPUT_LOG, OUTPUT_REPORT)
    
