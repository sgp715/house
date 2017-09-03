import time
import sys
import os.path
import pandas as pd

def create_episode_df(filename):
    """
    reads episode data and saves a pickled version
    """
    with open(filename) as house:
        subs = {"start":[], "end":[], "text":[]}
        state = 0
        start = None
        # end = None
        for line in house:
            print(line)
            # time.sleep(1)
            if state == 0:
                state = 1
                continue
            elif state == 1:
                start, end = line.split("-->")
                start = start.strip().split(',')[0]
                end = end.strip().split(',')[1]
                state = 2
            elif state == 2:
                if line == "\n":
                    state = 0
                else:
                    subs["start"].append(start)
                    subs["end"] = end
                    subs["text"].append(line.replace('\n',''))
                # print(line)
        # print("subs:")
        # print(subs)
    df = pd.DataFrame.from_dict(subs)
    df.to_pickle(filename + ".pkl")
    return df

def load_data(filename):
    data = None
    if not(os.path.isfile(filename + ".pkl")):
        df = create_episode_df(filename)
    df = pd.read_pickle(filename + ".pkl")
    return df
