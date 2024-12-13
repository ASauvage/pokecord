from argparse import ArgumentParser
from pokemon import Pokemon


MAJOR_VERSION = 1
MINOR_VERSION = 1
VERSION = '.'.join((str(MAJOR_VERSION), str(MINOR_VERSION)))


if __name__ == '__main__':
    ap = ArgumentParser(prog='pokecord', description='')
    ap.add_argument('-v', '--version', action='version', version='%(prog)s v' + VERSION,
                    help="Show %(prog)s version")
    sp = ap.add_subparsers(dest='command')

    run_ap = sp.add_parser('run', description='Run app',
                           help="Run app")

    refresh_ap = sp.add_parser('refresh', decription='Refresh data cache',
                               help="Refresh data cache")

    pokemon_ap = sp.add_parser('pokemon', description='',
                               help="")
    pokemon_ap.add_argument('id', dest='id', type=int,
                            help="Return pokemon info")

    args = ap.parse_args()

    match args.command:
        case 'run':
            pass
        case 'refresh':
            pass
        case 'pokemon':
            print(Pokemon(args.id).name)
        case _:
            ap.print_usage()
