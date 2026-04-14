import argparse
import os


class LogAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}

    def analyze(self):
        with open(self.file_path, "r") as file:
            for line in file:
                for level in self.counts:
                    if level in line:
                        self.counts[level] += 1

    def get_summary(self, level=None):
        if level:
            return {level: self.counts.get(level, 0)}
        return self.counts


def main():
    parser = argparse.ArgumentParser(description="DevOps CLI Log Analyzer")

    parser.add_argument("--file", required=True, help="Path to log file")
    parser.add_argument("--out", help="Output file path")
    parser.add_argument(
        "--level",
        choices=["INFO", "WARNING", "ERROR"],
        help="Filter by log level"
    )

    args = parser.parse_args()

    # Validate file
    if not os.path.exists(args.file):
        print("❌ Error: File not found")
        return

    analyzer = LogAnalyzer(args.file)
    analyzer.analyze()

    summary = analyzer.get_summary(args.level)

    # Format output
    output = "\n".join([f"{k}: {v}" for k, v in summary.items()])

    # Print
    print("\n📊 Log Summary:")
    print(output)

    # Write to file
    if args.out:
        with open(args.out, "w") as f:
            f.write(output)
        print(f"\n✅ Saved to {args.out}")


if __name__ == "__main__":
    main()