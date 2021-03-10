import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from run_scenarios import run_varying_buffer_capacity_model, run_varying_spawn_rate_model


def plot_varying_buffer_barchart(): # Plots comparative bar graph of average waiting times for each vehicle for each model
    wait_times = run_varying_buffer_capacity_model()

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
    width = 0.3  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width, all_vehicle_averages, width, label='All Vehicles')
    rects2 = ax.bar(x, small_car_averages, width, label='Small Cars')
    rects3 = ax.bar(x + width, large_vehicle_averages, width, label='Large Vehicles')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Average Waiting Time (seconds)')
    ax.set_xlabel('Large Vehicle Buffer Capacity')
    ax.set_title('Average Waiting Times For Varying Large Vehicle Buffer Capacities')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    fig.tight_layout()

    plt.show()


def plot_varying_spawn_rate_capacity_0_barchart(): # Plots bar graph with spawn rate varying 0.01-.08 and buffer 0
    wait_times = run_varying_spawn_rate_model(buffer_size=0)

    model1_wait_times = wait_times[0]
    model2_wait_times = wait_times[1]
    model3_wait_times = wait_times[2]
    model4_wait_times = wait_times[3]
    model5_wait_times = wait_times[4]
    model6_wait_times = wait_times[5]
    model7_wait_times = wait_times[6]
    model8_wait_times = wait_times[7]

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

    all_average6 = sum([model6_wait_times[i]['all'] for i in range(len(model6_wait_times))]) / len(model6_wait_times)
    small_average6 = sum([model6_wait_times[i]['small'] for i in range(len(model6_wait_times))]) / len(
        model6_wait_times)
    large_average6 = sum([model6_wait_times[i]['large'] for i in range(len(model6_wait_times))]) / len(
        model6_wait_times)

    all_average7 = sum([model7_wait_times[i]['all'] for i in range(len(model7_wait_times))]) / len(model7_wait_times)
    small_average7 = sum([model7_wait_times[i]['small'] for i in range(len(model7_wait_times))]) / len(
        model7_wait_times)
    large_average7 = sum([model7_wait_times[i]['large'] for i in range(len(model7_wait_times))]) / len(
        model7_wait_times)

    all_average8 = sum([model8_wait_times[i]['all'] for i in range(len(model8_wait_times))]) / len(model8_wait_times)
    small_average8 = sum([model8_wait_times[i]['small'] for i in range(len(model8_wait_times))]) / len(
        model8_wait_times)
    large_average8 = sum([model8_wait_times[i]['large'] for i in range(len(model8_wait_times))]) / len(
        model8_wait_times)

    small_car_averages = [small_average1, small_average2, small_average3, small_average4,
                          small_average5, small_average6, small_average7, small_average8]
    large_vehicle_averages = [large_average1, large_average2, large_average3, large_average4,
                              large_average5, large_average6, large_average7, large_average8]
    all_vehicle_averages = [all_average1, all_average2, all_average3, all_average4, all_average5, all_average6,
                            all_average7, all_average8]

    labels = ['0.01', '0.02', '0.03', '0.04', '0.05', '0.06', '0.07', '0.08']

    x = np.arange(len(labels))  # the label locations
    width = 0.3  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width, all_vehicle_averages, width, label='All Vehicles')
    rects2 = ax.bar(x, small_car_averages, width, label='Small Cars')
    rects3 = ax.bar(x + width, large_vehicle_averages, width, label='Large Vehicles')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Average Waiting Time (seconds)')
    ax.set_xlabel('Vehicle Spawn Rate')
    ax.set_title('Average Waiting Times For Varying Vehicle Spawn Rate And Buffer Size 0')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    fig.tight_layout()

    plt.show()


def plot_varying_spawn_rate_capacity_3_barchart():  # Plots bar graph with spawn rate varying 0.01-.08 and buffer 3
    wait_times = run_varying_spawn_rate_model(buffer_size=3)

    model1_wait_times = wait_times[0]
    model2_wait_times = wait_times[1]
    model3_wait_times = wait_times[2]
    model4_wait_times = wait_times[3]
    model5_wait_times = wait_times[4]
    model6_wait_times = wait_times[5]
    model7_wait_times = wait_times[6]
    model8_wait_times = wait_times[7]

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

    all_average6 = sum([model6_wait_times[i]['all'] for i in range(len(model6_wait_times))]) / len(model6_wait_times)
    small_average6 = sum([model6_wait_times[i]['small'] for i in range(len(model6_wait_times))]) / len(
        model6_wait_times)
    large_average6 = sum([model6_wait_times[i]['large'] for i in range(len(model6_wait_times))]) / len(
        model6_wait_times)

    all_average7 = sum([model7_wait_times[i]['all'] for i in range(len(model7_wait_times))]) / len(model7_wait_times)
    small_average7 = sum([model7_wait_times[i]['small'] for i in range(len(model7_wait_times))]) / len(
        model7_wait_times)
    large_average7 = sum([model7_wait_times[i]['large'] for i in range(len(model7_wait_times))]) / len(
        model7_wait_times)

    all_average8 = sum([model8_wait_times[i]['all'] for i in range(len(model8_wait_times))]) / len(model8_wait_times)
    small_average8 = sum([model8_wait_times[i]['small'] for i in range(len(model8_wait_times))]) / len(
        model8_wait_times)
    large_average8 = sum([model8_wait_times[i]['large'] for i in range(len(model8_wait_times))]) / len(
        model8_wait_times)

    small_car_averages = [small_average1, small_average2, small_average3, small_average4,
                          small_average5, small_average6, small_average7, small_average8]
    large_vehicle_averages = [large_average1, large_average2, large_average3, large_average4,
                              large_average5, large_average6, large_average7, large_average8]
    all_vehicle_averages = [all_average1, all_average2, all_average3, all_average4, all_average5, all_average6,
                            all_average7, all_average8]

    labels = ['0.01', '0.02', '0.03', '0.04', '0.05', '0.06', '0.07', '0.08']

    x = np.arange(len(labels))  # the label locations
    width = 0.3  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width, all_vehicle_averages, width, label='All Vehicles')
    rects2 = ax.bar(x, small_car_averages, width, label='Small Cars')
    rects3 = ax.bar(x + width, large_vehicle_averages, width, label='Large Vehicles')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Average Waiting Time (seconds)')
    ax.set_xlabel('Vehicle Spawn Rate')
    ax.set_title('Average Waiting Times For Varying Vehicle Spawn Rate And Buffer Size 3')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    fig.tight_layout()

    plt.show()


def plot_varying_spawn_rate_capacity_5_barchart():  # Plots bar graph with spawn rate varying 0.01-.08 and buffer 5
    wait_times = run_varying_spawn_rate_model(buffer_size=5)

    model1_wait_times = wait_times[0]
    model2_wait_times = wait_times[1]
    model3_wait_times = wait_times[2]
    model4_wait_times = wait_times[3]
    model5_wait_times = wait_times[4]
    model6_wait_times = wait_times[5]
    model7_wait_times = wait_times[6]
    model8_wait_times = wait_times[7]

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

    all_average6 = sum([model6_wait_times[i]['all'] for i in range(len(model6_wait_times))]) / len(model6_wait_times)
    small_average6 = sum([model6_wait_times[i]['small'] for i in range(len(model6_wait_times))]) / len(
        model6_wait_times)
    large_average6 = sum([model6_wait_times[i]['large'] for i in range(len(model6_wait_times))]) / len(
        model6_wait_times)

    all_average7 = sum([model7_wait_times[i]['all'] for i in range(len(model7_wait_times))]) / len(model7_wait_times)
    small_average7 = sum([model7_wait_times[i]['small'] for i in range(len(model7_wait_times))]) / len(
        model7_wait_times)
    large_average7 = sum([model7_wait_times[i]['large'] for i in range(len(model7_wait_times))]) / len(
        model7_wait_times)

    all_average8 = sum([model8_wait_times[i]['all'] for i in range(len(model8_wait_times))]) / len(model8_wait_times)
    small_average8 = sum([model8_wait_times[i]['small'] for i in range(len(model8_wait_times))]) / len(
        model8_wait_times)
    large_average8 = sum([model8_wait_times[i]['large'] for i in range(len(model8_wait_times))]) / len(
        model8_wait_times)

    small_car_averages = [small_average1, small_average2, small_average3, small_average4,
                          small_average5, small_average6, small_average7, small_average8]
    large_vehicle_averages = [large_average1, large_average2, large_average3, large_average4,
                              large_average5, large_average6, large_average7, large_average8]
    all_vehicle_averages = [all_average1, all_average2, all_average3, all_average4, all_average5, all_average6,
                            all_average7, all_average8]

    labels = ['0.01', '0.02', '0.03', '0.04', '0.05', '0.06', '0.07', '0.08']

    x = np.arange(len(labels))  # the label locations
    width = 0.3  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width, all_vehicle_averages, width, label='All Vehicles')
    rects2 = ax.bar(x, small_car_averages, width, label='Small Cars')
    rects3 = ax.bar(x + width, large_vehicle_averages, width, label='Large Vehicles')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Average Waiting Time (seconds)')
    ax.set_xlabel('Vehicle Spawn Rate')
    ax.set_title('Average Waiting Times For Varying Vehicle Spawn Rate And Buffer Size 5')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    fig.tight_layout()

    plt.show()


run = True
while run:
    choice = input("Which chart would you like to plot?"
                   "\n1 (Varying buffer size, fixed spawn rate 0.05)"
                   "\n2 (Varying spawn rate 0.01-.08, fixed capacity 0)"
                   "\n3 (Varying spawn rate 0.01-.08, fixed capacity 3)"
                   "\n4 (Varying spawn rate 0.01-.08, fixed capacity 5)"
                   "\nq (Quit program)")

    if choice == "q":
        run = False
    elif choice == "1":
        plot_varying_buffer_barchart()
    elif choice == "2":
        plot_varying_spawn_rate_capacity_0_barchart()
    elif choice == "3":
        plot_varying_spawn_rate_capacity_3_barchart()
    elif choice == "4":
        plot_varying_spawn_rate_capacity_5_barchart()
