import dill
import time
import sys


def square(number):
    return number*number


count=1

if __name__=="__main__":
    try:
        try:
            dill.load_session('session.pkl')
        except:
            pass
    
        while True:
            count+=1
            print(count)
            time.sleep(.01)

    except KeyboardInterrupt:
        dill.dump_session('session.pkl')
        sys.exit()
