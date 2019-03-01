import logging


def set_loggers():

    # set up logging
    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(asctime)s] [%(name)-12s] [%(levelname)-6s] (%(message)s)',
        datefmt='%Y-%m-%d %H:%M:%S',
    )


set_loggers()

logging.info('LOGGERS READY')
