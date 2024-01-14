from loguru import logger

class SetLog:   
    def __init__(self):
        logger.remove()       
        logger.add(
            'LOG.txt'
        )
    message = ""

    def set_log_info(self, message= ''):
        logger.info(message)
        logger.remove()

    def set_log_error(self, message=''):
        logger.error(message)
        logger.remove()

    def close_log(self):
        logger.remove()
