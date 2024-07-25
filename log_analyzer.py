import sys
from scripts.Log_parser import parse_log_file
from scripts.log_stats import log_stastistics, genrate_report

def main(log_file_path, report_file_path):
    parsed_logs = parse_log_file(log_file_path)
    stats = log_stastistics(parsed_logs)
    genrate_report(stats, report_file_path)
    print(f"Report generated: { report_file_path}")

if __name__ == "__main__":
   if len(sys.argv) !=3:
       print("Usage: python log_analyzer.py <log_file_path> <report_file_path>")
       sys.exit(1)
log_file_path =sys.exit(1)
report_file_path =sys.exit(1)
main(log_file_path,report_file_path )
