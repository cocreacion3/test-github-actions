import time
import sys
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.StreamHandler(),  # Log to console
        logging.FileHandler('/app/logs/app.log')  # Log to file within the container
    ]
)

def main():
    while True:
        # print('hi from worker2')
        # sys.stderr.write("hi from worker2\n")
        logging.info('hi from worker3')
        time.sleep(5)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
