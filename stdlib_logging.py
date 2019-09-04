import os
import platform
import logging

# 'startwith'
if platform.platform().startswith("Windows"):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'),
                                os.getenv('HOMEPATH'),
                                'test.txt')

elif platform.system() == "Linux":
    logging_file = os.path.join(os.getenv('HOME'),
                                'test.txt')

print(f'Logging to file: {logging_file}')


logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s:%(name)s:%(message)s',
    filename=logging_file,
    filemode='a'
)


logging.debug("Debug level message")
logging.info("Info level message")
logging.warning("Warning level message")

