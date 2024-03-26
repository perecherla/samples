import logging
import sys
from logging.handlers import QueueHandler
from multiprocessing import current_process


class First:

    def __init__(self):
        pass
        # self.db_object = db_object

    def first_function(self, db_object, logger, queue):
        print('first_function')
        print(db_object)
        print(logger)
        print(queue)
        # sys.exit(1)
        # logger.info(self.db_object)
        # create a logger
        # logger = logging.getLogger('app')
        # # add a handler that uses the shared queue
        # logger.addHandler(QueueHandler(queue))
        # # log all messages, debug and up
        # logger.setLevel(logging.DEBUG)
        # get the current process
        process = current_process()
        # report initial message
        logger.info(f'first_function Child {process.name} starting.')

        File_operation(logger).file_op('first')


class Second:

    def __init__(self):
        pass
        # self.db_object = db_object

    def second_function(self, db_object, logger, queue):
        print('second_function')
        # print(data[0])
        # print(data[1])
        print(db_object)
        print(logger)
        print(queue)
        # sys.exit(1)
        # logger.info(self.db_object)
        # create a logger
        # logger = logging.getLogger('app')
        # # add a handler that uses the shared queue
        # logger.addHandler(QueueHandler(queue))
        # # log all messages, debug and up
        # logger.setLevel(logging.DEBUG)
        # get the current process
        process = current_process()
        # report initial message
        logger.info(f'second_function Child {process.name} starting.')

        File_operation(logger).file_op('second')


class File_operation:
    def __init__(self, logger):
        self.logger = logger

    def file_op(self, from_fun):
        self.logger.info(f'file_op running from {from_fun}.')
