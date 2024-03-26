import logging
import sys
from logging.handlers import QueueHandler
from multiprocessing import Pool, Manager

from class_handler import First, Second
from log_handler import logger_process


# entry point
def main():
    data = []
    pool = Pool(processes=2)

    db_object = object

    # create the shared queue and get the proxy object
    queue = Manager().Queue()
    # create a logger
    logger = logging.getLogger('app')
    # add a handler that uses the shared queue
    logger.addHandler(QueueHandler(queue))
    # log all messages, debug and up
    logger.setLevel(logging.DEBUG)

    # issue a long-running task to receive logging messages
    _ = pool.apply_async(logger_process, args=(queue,))
    # report initial message
    logger.info('Main process started.')

    # data = (db_object, logger, queue)

    p1 = pool.map_async(First().first_function(db_object, logger, queue), data)
    p2 = pool.map_async(Second().second_function(db_object, logger, queue), data)

    # wait for all issued tasks to complete
    logger.info('Main process waiting...')
    # for result in results:
    #     result.wait()
    # report final message
    logger.info('Main process done.')
    # shutdown the long-running logger task
    queue.put(None)
    # close the process pool
    pool.close()
    # wait for all tasks to complete (e.g. the logger to close)
    pool.join()


def job(instance):
    instance.func()
    return instance


if __name__ == '__main__':
    main()
