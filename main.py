import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filename_snapshot = "Dataset/snapshots_arabia_t_5040.csv"
filename_overview = "Dataset/aoe_data.csv"





def plot_elo_time(data, overview):
    plt.figure()
    plt.title("Time Over Average ELO")
    plt.xlabel("Average ELO")
    plt.ylabel("Time")
    
    data_x = data["avg_elo"]
    data_y = data["duration"]
    data_order = np.argsort(data_x)
    plt.plot(data_x[data_order], data_y[data_order])
    
    plt.show()
    
    

def plot_time_progression(data, overview):
    plt.figure()
    plt.title("Age Progression Significance")
    plt.xlabel("Time")
    plt.ylabel("Winrate")
    
    data_win = data["winner"]
    data_times = [
        [
            data["p1 Feudal Age Time"],
            data["p1 Castle Age Time"],
            data["p1 Imperial Age Time"]
        ],
        [
            data["p2 Feudal Age Time"],
            data["p2 Castle Age Time"],
            data["p2 Imperial Age Time"]
        ]
    ]
    
    data_x = np.linspace(0, 5000, 100)
    
    wins    = np.zeros((3, 100))
    losses  = np.zeros((3, 100))
    
    for i, winner in enumerate(data_win):
        for j in range(0, 2):
            t = data_times[j]
            for k, age in enumerate(t):
                time = age[i]
                bucket = (time + 50) // 100
                if bucket >= 100 or bucket < 0:
                    continue
                (wins if (winner == j) else losses)[k][bucket] += 1
    
    data_y = [[], [], []]
    for i in range(3):
        for j in range(100):
            w = wins[i][j]
            l = losses[i][j]
            if j == 0 or w < 10 or l < 10:
                data_y[i].append(float('nan'))
                continue
            winrate = (w / (w + l)) * 100
            data_y[i].append(winrate)
    
    plt.plot(data_x, data_y[0])
    plt.plot(data_x, data_y[1])
    plt.plot(data_x, data_y[2])
    
    plt.show()






def main():
    data        = pd.read_csv(filename_snapshot)
    print("Loaded data")
    
    overview    = pd.read_csv(filename_overview)
    print("Loaded overview", )
    
    # plot_elo_time(data, overview)
    plot_time_progression(data, overview)
    

if __name__ == "__main__":
    main()
