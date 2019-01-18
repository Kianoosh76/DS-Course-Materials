import signal


def signal_handler(signum, frame):
    raise Exception("Timed out!")


def put_limit(time):
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(time)
