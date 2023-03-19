import traceback
from datetime import datetime
from os import environ


class Logger:
    #TODO: add doc string

    @classmethod
    def __write(cls, filename, log):

        with open(filename,'w+') as fptr:
            fptr.write(log)

    @classmethod
    def __construct_log(cls, log_level, log_msg, trace):

        return f"""{log_level}: {log_msg}\n 
                    TIMESTAMP: {datetime.now()}\n
                    TRACE: {trace}\n
                """

    @classmethod
    def __get_trace(cls, err):

        return ''.join(
                    traceback.format_exception(
                        None, err, err.__traceback__
                    )
                )

    @classmethod
    def error(cls, err, log_level="ERROR", 
        log_msg="Default message"
    ):

        try:

            # Get trace of the error to ease debugging
            trace = cls.__get_trace(err)

            # Construct log message
            log = cls.__construct_log(
                log_level, log_msg, trace
            )

            # Print log to terminal when in debug mode
            # Else append to error.log file
            if environ.get('DEBUG', False):
                print(log)
            
            else:
                cls.__write('error.log', log)

        except Exception as e:
            cls.__write('error.log', log)
