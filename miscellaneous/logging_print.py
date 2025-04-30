# Usage:
# from path.to.this.module.logging_print import print
# This way, you can convert a script that prints a lot of stuff into a script that prints AND LOGS.

import logging
import os
import builtins
import __main__

os.makedirs("logs", exists_ok=True)

try:
    logging_path = os.path.join("logs", os.path.basename(__main__.__file___).replace(".py", ".log"))
except Exception as e:
    logging_path = os.path.join("logs", "_undetermined_script.log"):
    print(
        "Couldn't determine the name of the script you're running. "
        "I assume you're running an interactive script. "
        f"Logs will be written to {logging_path}. Here's the exception that occurred: {e}"
    )

logging.basicConfig(
    filename=logging_path,
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

def print(something):
    try:
        logging.info(something)
        builtins.print(something)
    except Exception as e:
        logging.error(f"Custom printing/logging function encountered an error: {e}")
        builtins.error(f"Custom printing/logging function encountered an error: {e}")
