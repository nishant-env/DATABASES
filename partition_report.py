from tokenize import String
from venv import create
import pandas as pd
import os
import argparse


def create_chunk(chunk_size,csv_path):
    counter = 1
    offset = 0
    large_csv = pd.read_csv(csv_path)
    dir_name = os.path.dirname(csv_path)
    file_name = os.path.basename(csv_path).split(".")[-2]
    if (os.path.isdir(dir_name+'\\'+file_name)):
        pass
    else:
        os.mkdir(dir_name+'\\'+file_name)

    while offset <= len(large_csv):
        chunk = large_csv[offset:(offset+chunk_size-1)]
        chunk.to_csv(dir_name+'\\'+file_name+'\\'+file_name+'_'+str(counter)+'.csv',index=False)
        counter+=1
        offset+=chunk_size



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--chunk', type=int, required=False,default=1000000,help='Chunk Size (default is 10 lakhs)')
    parser.add_argument('--path', type=str, required=True,help='Enter File Path')
    args = parser.parse_args()
    create_chunk(args.chunk,args.path)