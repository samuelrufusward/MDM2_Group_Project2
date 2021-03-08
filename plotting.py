import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from run_scenarios import run_all_scenarios


def plotbar(): # Plots comparative bar graph of average waiting times for each vehicle for each model
    wait_times = run_all_scenarios()

    model0_wait_times = wait_times[0]
    model1_wait_times = wait_times[1]
    model2_wait_times = wait_times[2]
    model3_wait_times = wait_times[3]
    model4_wait_times = wait_times[4]
    model5_wait_times = wait_times[5]

    all_average0 = sum([model0_wait_times[i]['all'] for i in range(len(model0_wait_times))]) / len(model0_wait_times)
    small_average0 = sum([model0_wait_times[i]['small'] for i in range(len(model0_wait_times))]) / len(
        model0_wait_times)
    large_average0 = sum([model0_wait_times[i]['large'] for i in range(len(model0_wait_times))]) / len(
        model0_wait_times)

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

    all_average4 = sum([model4_wait_times[i]['all'] for i in range(len(model4_wait_times))]) / len(model4_wait_times)
    small_average4 = sum([model4_wait_times[i]['small'] for i in range(len(model4_wait_times))]) / len(
        model4_wait_times)
    large_average4 = sum([model4_wait_times[i]['large'] for i in range(len(model4_wait_times))]) / len(
        model4_wait_times)

    all_average5 = sum([model5_wait_times[i]['all'] for i in range(len(model5_wait_times))]) / len(model5_wait_times)
    small_average5 = sum([model5_wait_times[i]['small'] for i in range(len(model5_wait_times))]) / len(
        model5_wait_times)
    large_average5 = sum([model5_wait_times[i]['large'] for i in range(len(model5_wait_times))]) / len(
        model5_wait_times)

    small_car_averages = [small_average0, small_average1, small_average2, small_average3, small_average4, small_average5]
    large_vehicle_averages = [large_average0, large_average1, large_average2, large_average3, large_average4, large_average5]
    all_vehicle_averages = [all_average0, all_average1, all_average2, all_average3, all_average4, all_average5]

    labels = ['0', '1', '2', '3', '4', '5']

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

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

plotbar()