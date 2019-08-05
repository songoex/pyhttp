import hashlib 
import re
import time
import uuid
import datetime
from HttpTesting.library.scripts import parse_args_func

"""
User-defined extension function import
"""
try:
    from HttpTesting.case.extfunc import Extend
except ImportError:
    Extend = object

class FUNC(Extend):
    """
    Framework function library.

    Usage:
        from HttpTesting.library.func import FUNC

        %{FUNC.md5(txt)}%
        %{FUNC.timestamp()}%
    """

    @staticmethod
    def md5(txt=''):
        """
        The md5 string is generated.

        Args:
            txt: The string to generate md5.
        Usage:
            ret = md5(txt)
        Return:
            ret: The md5 string is generated.
        """
        mo = hashlib.md5()
        src = txt.encode(encoding='utf-8')
        mo.update(src)   
        
        return mo.hexdigest()


    @staticmethod
    def timestamp():
        """
        The timestamp
        """
        return int(time.time())


    @staticmethod
    def datetimestr():
        """
        Generate date-time strings.

        Args:

        Return:
            String  2019-07-16 10:50:16
        """
        datetime= str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        return datetime


    @staticmethod
    def uuid1():
        """
        Generate uuid1.

        Usage:
            ret = FUNC.uuid1()
        Return:
            String uuid1  example: ad7678fe-a775-11e9-907f-88b111064583
        """

        return str(uuid.uuid1()).replace('-','')


    @staticmethod
    def mstimestamp():
        """
        Millisecond time stamp.  20 bit
        """
        ret = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
        return ret

    @staticmethod
    def sleep_time(ses):
        """
        Main thread sleep time.

        Args:
            ses: seconds; Support decimals such as 0.5 or 0.8.
            1, 1 seconds, 0.5, 500 milliseconds.
        
        Usage:
            import time
            sleep_time(0.5) #500 milliseconds.

        Returns:
            There is no return.
        """
        time.sleep(ses)


if __name__ == "__main__":
    a = FUNC.uuid1()
    print(a)
    