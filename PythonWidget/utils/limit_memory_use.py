# just support linux

import resource

def limit_memory(maxsize: int = 50):
    """
    :param maxsize: 最大限制内存使用量 GB
    :return: None
    """
    maxsize = maxsize * (1024 ** 3)
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    resource.setrlimit(resource.RLIMIT_AS, (maxsize, hard))

