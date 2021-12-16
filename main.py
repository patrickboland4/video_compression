import os
import subprocess

from app.reader import Reader
from meetings import MEETINGS as meetings
from app.compressor import Compressor

def main():
    #########
    # download all videos
    #########
    for url, pw, date, completed in meetings:
        if completed:
            continue
        else:
            r = subprocess.run([
                "zoomdl", "-u", f"{url}", "-p", f"{pw}", "-f", f"./uncompressed/ytt{date}" 
            ])
            assert(type(r) is subprocess.CompletedProcess) # TODO right now everything is of this type, catch instances where the video is not found

    #########
    # compress videos
    #########
    c = Compressor("uncompressed", "compressed")
    for f in os.listdir("./uncompressed"):
        c.compress(f)

    ########
    # load to drive
    ########

    print("all done") 
            




if __name__ == "__main__":
    main()