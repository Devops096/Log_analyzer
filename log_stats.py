import pandas as pd 
from datetime import datetime
def log_stastistics(parsed_logs): 
    df = pd.  DataFrame(parsed_logs)
    df['timestamp'] = pd. to_datetime(df['timestamp'])
    df['hour'] = df['timestamp'].dt.hour

    stats ={
        'total_logs': len(df),
        'logs_per_hour': df.groupby('hour').size().to_dict(),
        'logs_by_level': df['log_level'].value_counts().to_dict()
    }
    return stats
def genrate_report(stats, output_path):
    with open(output_path, 'w') as file:
        file.write("Log File Statistics\n")
        file.write("===================\n")
        file.write(f"Total Logs: {stats['total_logs']}\n")
        file.write("Log per Hour:\n")
        for hour, count in stats['logs_per_hour'].items():
            file.write(f"{hour}:{count}\n")
        file.write(f"{hour}:{count}\n")
        for level, count in stats['logs_by_level'].items():
            file.write(f"{level}:{count}\n")