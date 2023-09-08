import time
import sys

def main():
    while True:
        # print('hi from worker2')
        sys.stderr.write("hi from worker2\n")
        time.sleep(5)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
