"""Command line script."""


import argparse
import sys

import astronomical

from ..model.location import Requirements
from ..model.real_world_calculations import Alarms, Time
from ..service.configuration import Defaults
from ..service.logging import logger
from ..service.requirements import AlarmsService, Sun, TimeService


def main():
    """Provide options for script."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--version", help="show the version and exit",
                        action="store_true")
    parser.add_argument("-s", "--sun", help=Sun.__doc__.lower()[:-1],
                        action="store_true")
    parser.add_argument("-t", "--time", help=TimeService.__doc__.lower()[:-1],
                        action="store_true")
    parser.add_argument("-a", "--alarms",
                        help=AlarmsService.__doc__.lower()[:-1],
                        action="store_true")
    args = parser.parse_args()

    # supply config
    locale = Defaults().location()
    requirements = Requirements()

    # parse main function arguments
    if args.version:
        print(astronomical.__version__)
        sys.exit(0)
    elif args.sun:
        logger.debug(f"CLI OPTION: \"sun\" invoked.")
        sun = Sun()
        print(sun)
    elif args.time:
        logger.debug(f"CLI OPTION: \"time\" invoked.")
        time = TimeService(Time(locale))
        print(time)
    elif args.alarms:
        logger.debug(f"CLI OPTION: \"alarms\" invoked.")
        alarms = AlarmsService(Alarms(requirements, locale))
        print(alarms)
