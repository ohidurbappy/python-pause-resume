import time
import pickle
import os
import sys

save_file = "save_file.tmp"

if os.path.exists(save_file):
    with open(save_file, "rb") as in_file:
        try:
            my_array = pickle.loads(in_file.read()) # reload the last operation
        except Exception:
            my_array = []
else:
    my_array = []

while True:
    try:
        time.sleep(1)
        print('.',end='',flush=True)
        my_array.append("next") # here you can do what you want replace this part
    except KeyboardInterrupt:
        print (my_array)
        with open(save_file, "wb") as out_file:
            out_file.write(pickle.dumps(my_array))
        sys.exit()