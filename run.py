import argparse
from generator import Genreator
import time
from loguru import logger

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config',type=str, default=r'D:\devs\codes\data_faker\configs\spsc_8tn_13dr.yaml', help='')
    parser.add_argument('--work_dir',type=str, default=r'D:\devs\codes\data_faker\outputs', help='')
    args = parser.parse_args()
    return args

def run():
    start_time = time.time()
    args = parse()
    generator = Genreator(args)
    generator.run()
    end_time = time.time()
    print(f'time-cost: {round(end_time-start_time,3)} seconds')

if __name__=='__main__':
    run()