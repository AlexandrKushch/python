import sys
import logging
import datetime
import click
sys.path.append("../../")
from lab13_14.src.api import api
from lab13_14.src.bs import bs
from lab15.src.main import graphs

logging.basicConfig(level='INFO')
logger = logging.getLogger()


@click.command()
@click.option('--function', type=click.Choice(['api', 'bs', 'graphs']))
@click.option('--author', type=str, help='Need for api')
def main(function, author):
    start = datetime.datetime.now()
    if function == 'api':
        logger.info("API script has started")

        try:
            api(author)
        except Exception as e:
            print(e)
            print('Enter --author')
    elif function == 'bs':
        logger.info("Beautiful soup script has started")

        bs()
    elif function == 'graphs':
        logger.info("Graphic's script has started")

        graphs()

    end = datetime.datetime.now()
    logger.info(f"Time: {end - start}")


if __name__ == '__main__':
    main()