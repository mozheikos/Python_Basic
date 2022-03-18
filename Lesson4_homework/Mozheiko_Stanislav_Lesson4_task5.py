import sys
import utils

__name__ = sys.argv[0]

command = sys.argv[1]

if command == 'rate':
    command = utils.currency_rates(sys.argv[2])
