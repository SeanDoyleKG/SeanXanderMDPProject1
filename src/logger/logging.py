'''
logging file for use in other files
'''

import logging

def message_output(line: bool = True, time: bool = True, name: bool = False):
    output_str = '%(levelname)s - %(message)s'
    if line:
        output_str = 'Line %(lineno)d: ' + output_str
    if time:
        output_str += ' @ %(asctime)s'
    if name:
        output_str += ' in %(name)s'
    return logging.Formatter(output_str)


def file_handler(level: str, filename: str, line: bool = True, time: bool = True, name: bool = False):
    handler = logging.FileHandler(filename)
    handler.setLevel(level)
    handler.setFormatter(message_output(line=line, time=time, name=name))
    return handler
    

def console_handler(level: str, line: bool = True, time: bool = True, name: bool = False):
    handler = logging.StreamHandler()
    handler.setLevel(level)
    handler.setFormatter(message_output(line=line, time=time, name=name))
    return handler
    

def default_logger(level: str = 'WARNING', filename: str = 'output.log', line: bool = True, time: bool = True, name: bool = False):
    out_logger = logging.getLogger(__name__)
    out_logger.setLevel(level)

    out_logger.addHandler(file_handler(level, filename, line=line, time=time, name=name))
    out_logger.addHandler(console_handler(level, line=line, time=time, name=name))
    return out_logger
