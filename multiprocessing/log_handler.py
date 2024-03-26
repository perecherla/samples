import logging


# executed in a process that performs logging
def logger_process(queue):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("log_file.log"),
            # logging.StreamHandler()
        ]
    )
    logger = logging.getLogger(__name__)

    # # create a logger
    # logger = logging.getLogger('app')
    # configure a stream handler
    logger.addHandler(logging.StreamHandler())
    # log all messages, debug and up
    logger.setLevel(logging.DEBUG)
    # report that the logger process is running
    logger.info(f'Logger process running.')
    # run forever
    while True:
        # consume a log message, block until one arrives
        message = queue.get()
        # check for shutdown
        if message is None:
            logger.info(f'Logger process shutting down.')
            break
        # log the message
        logger.handle(message)
