import re
def parse_log_line(line):
    log_pattern =re.compile(
        r'(?P< timestamp>\'S+) (?P<log_level>\S+) (?P<message>.+)')
    match=log_pattern.match(line)
    if match:
       return match.groupdict()
    return None
def parse_log_file(log_file_path):
    parsed_logs=[]
    with open(log_file_path,'r') as file:
         for line in file:
            parsed_line = parse_log_line(line)
            if parsed_line:
             parsed_logs .append(parsed_line)
    return parsed_logs