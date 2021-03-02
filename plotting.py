import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from run_scenarios import run_all_scenarios, run_model1


def plotbar(): # Plots comparative bar graph of average waiting times for each vehicle for each model
    wait_times = run_all_scenarios()

    model1_wait_times = wait_times[0]
    model2_wait_times = wait_times[1]
    model3_wait_times = wait_times[2]

    all_average1 = sum([model1_wait_times[i]['all'] for i in range(len(model1_wait_times))]) / len(model1_wait_times)
    small_average1 = sum([model1_wait_times[i]['small'] for i in range(len(model1_wait_times))]) / len(
        model1_wait_times)
    large_average1 = sum([model1_wait_times[i]['large'] for i in range(len(model1_wait_times))]) / len(
        model1_wait_times)

    all_average2 = sum([model2_wait_times[i]['all'] for i in range(len(model2_wait_times))]) / len(model2_wait_times)
    small_average2 = sum([model2_wait_times[i]['small'] for i in range(len(model2_wait_times))]) / len(
        model2_wait_times)
    large_average2 = sum([model2_wait_times[i]['large'] for i in range(len(model2_wait_times))]) / len(
        model2_wait_times)

    all_average3 = sum([model3_wait_times[i]['all'] for i in range(len(model3_wait_times))]) / len(model3_wait_times)
    small_average3 = sum([model3_wait_times[i]['small'] for i in range(len(model3_wait_times))]) / len(
        model3_wait_times)
    large_average3 = sum([model3_wait_times[i]['large'] for i in range(len(model3_wait_times))]) / len(
        model3_wait_times)

    print("all1:", all_average1)
    print("small1:", small_average1)
    print("large1:", large_average1)
    print("all2:", all_average2)
    print("small2:", small_average2)
    print("large2:", large_average2)
    print("all3:", all_average3)
    print("small3:", small_average3)
    print("large3:", large_average3)

    small_car_averages = [small_average1, small_average2, small_average3]
    large_vehicle_averages = [large_average1, large_average2, large_average3]
    all_vehicle_averages = [all_average1, all_average2, all_average3]

    labels = ['0', '1', '2']

    x = np.arange(len(labels))  # the label locations
    width = 0.25  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width, all_vehicle_averages, width, label='All Vehicles')
    rects2 = ax.bar(x, small_car_averages, width, label='Small Cars')
    rects3 = ax.bar(x + width, large_vehicle_averages, width, label='Large Vehicles')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Average Waiting Time')
    ax.set_xlabel('Large Vehicle Storage Capacity')
    ax.set_title('Average Waiting Times For Different Large Vehicle Storage Capacities')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    fig.tight_layout()

    plt.show()


def plothistogram(): # Plots histogram

    model1_wait_times = run_model1()

    all_average1 = sum([model1_wait_times[i]['all'] for i in range(len(model1_wait_times))]) / len(model1_wait_times)
    small_average1 = sum([model1_wait_times[i]['small'] for i in range(len(model1_wait_times))]) / len(
        model1_wait_times)
    large_average1 = sum([model1_wait_times[i]['large'] for i in range(len(model1_wait_times))]) / len(
        model1_wait_times)

    fig = plt.figure()

    plt.hist([float(model1_wait_times[i]["all"]) for i in range(len(model1_wait_times))])

    plt.show()

plotbar()