import time
import datetime
from functools import partial

from config import VERBOSE


def log(statement, verbose):
    if verbose:
        current_time = datetime.datetime.fromtimestamp(
            time.time()).strftime('%Y-%m-%d %H:%M:%S')
        print(f"{current_time}\t{statement}")


verboseprint = partial(log, verbose=VERBOSE)
