import logging

class Logger:
    def __init__(self, name: str, level: str = None, config:dict = None):
        # set dictConfig
        self.config = config
        if config != None:
            from logging.config import dictConfig
            dictConfig(config)
        
        # set logger name & level
        self.name = name
        self.level = level
        self.log_levels = {
            None: logging.INFO,
            "debug": logging.DEBUG,
            "warning": logging.WARNING,
            "error": logging.ERROR,
            "critical": logging.CRITICAL
        }
        self.logger = logging.getLogger(name)
        self.logger.setLevel(self.log_levels.get(self.level, logging.INFO))
        
        print("successfully created logger") # test
        
    # def __init__(self, name:str, level:str=None):
    #     self.name = name
    #     self.level = level
    #     self.logger = logging.getLogger(name)
    #     self.logger.setLevel(logging.INFO) if self.level == None \
    #         else self.logger.setLevel(logging.DEBUG) if self.level == "debug" \
    #         else self.logger.setLevel(logging.WARNING) if self.level == "warning" \
    #         else self.logger.setLevel(logging.ERROR) if self.level == "error" \
    #         else self.logger.setLevel(logging.CRITICAL) if self.level == "critical" \
    #         else print("Wrong log level input.")
                
    def add_file_handler(self, log_dir: str):
        from datetime import datetime
        import os
        
        # check log dir
        os.makedirs(log_dir) if not os.path.exists(log_dir) else True
        
        # define & add file handler
        log_format = "%(asctime)s - %(levelname)s - %(message)s"
        file_handler = logging.FileHandler(f"{log_dir}/{datetime.now().strftime('%Y-%m-%d_%H')}.log", encoding="utf-8")
        file_handler.setFormatter(logging.Formatter(log_format))
        self.logger.addHandler(file_handler)
        
    def remove_logger(self):
        # close handler        
        for handler in self.logger.handlers[:]:
            handler.close()
            self.logger.removeHandler(handler)

        # remove filter
        for filter_ in self.logger.filters[:]:
            self.logger.removeFilter(filter_)

if __name__ == "__main__":
    logger = Logger(name = "demo")
    logger.add_file_handler(log_dir="/Users/kimdohoon/git/study/python-logging/log")
    logger.remove_logger()
    