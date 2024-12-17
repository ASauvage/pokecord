import asyncio
from argparse import ArgumentParser
from pokebot import PokeBot, VERSION


if __name__ == '__main__':
    ap = ArgumentParser(prog='pokecord', description='')
    ap.add_argument('-v', '--version', action='version', version='%(prog)s v' + VERSION,
                    help="Show %(prog)s version")
    sp = ap.add_subparsers(dest='command')

    # run command
    run_ap = sp.add_parser('run', description='Run app',
                           help="Run app")

    args = ap.parse_args()

    match args.command:
        case 'run':
            asyncio.run(PokeBot().run_pokebot())
        case _:
            ap.print_usage()
