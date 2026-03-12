import math
def average_speeds(locations, times):
    """
    Given a list of n-dimensional coordinates and a list of times,
    calculate the average speed of the traveller during each interval.

    Given lists of length m, this function will produce a list of length m-1.
    """

    my_list = []
    for i in range(len(locations) - 1):
        x = locations[i + 1][0] - locations[i][0]
        y = locations[i + 1][1] - locations[i][1]
        distance = math.sqrt(x ** 2 + y **2)
        time = times[i + 1] - times[i]
        speed = distance / time
        my_list.append(speed)

    return my_list

print(average_speeds([[0, 0], [0, 10], [10, 10]], [0, 1, 3]))
def moving_average(values, window_size):
    """
    Given a list of numerical values and a window size 'k',
    return a list of averages of every 'k' consecutive elements.

    Given a list of length n, this function produces a list of length n - k + 1.
    """
    length_list = []
    for i in range(len(values) - window_size + 1):
        sums = 0
        for j in range(window_size):
            sums += values[i + j]
        count = 0
        count = sums / window_size
        length_list.append(float(count))

    if len(length_list) == 0:
        return 0
    return length_list

# print(moving_average( [10, 20, 0, 40], 2))
def probability_of_condition(prevalence, sensitivity, specificity):
    """
    Calculate the probability that a patient actually has a condition
    given a positive test result.

    - prevalence: How common the condition is (0.0 to 1.0).
    - sensitivity: Chance the test says 'positive' when the patient HAS it.
    - specificity: Chance the test says 'negative' when the patient DOES NOT have it.

    Hint: Think of this as a 2x2 table of possibilities.
    """
    ppv = (prevalence * sensitivity) / ((prevalence * sensitivity) + ((1 - specificity) * (1 - prevalence)))
    
    return ppv

print(probability_of_condition(0.01, 0.99, 0.95))
def common_destinations(alice, bob):
    """
    Given two lists of travel destinations (strings),
    return a list of destinations that appear in both lists.
    """
    my_list = []
    for a in alice:
        if a in bob:
            my_list.append(a)
    if my_list == []:
        return []
    return set(my_list)


def max_stock_profit(prices):
    """
    Given a list of daily stock prices, determine the maximum profit
    possible by buying one share and selling it on a later day.

    If no profit is possible (prices only go down), return 0.
    """
    min_price = prices[0]   
    max_profit = 0

    for price in prices:
        
        if price < min_price:
            min_price = price
       
        profit = price - min_price

        if profit > max_profit:
            max_profit = profit

    return max_profit
        
print(max_stock_profit([10, 5, 15, 20]))

def viral_growth_projection(initial_users, daily_growth_rate, days):
    """
    Context: A startup needs to estimate server capacity for a new app launch.
    The user base grows exponentially.

    Formula: Future Users = Initial Users * (1 + growth_rate) ^ days

    Args:
        initial_users (int): Users on day 0.
        daily_growth_rate (float): e.g., 0.20 for 20% growth.
        days (int): Number of days to project into the future.

    Return the projected integer number of users (truncate/floor decimals).
    """
    Future_Users = initial_users * (1 + daily_growth_rate) ** days

    return Future_Users


def calculate_break_even_point(fixed_cost, cost_per_unit, sell_price):
    """
    Context: A manufacturer needs to know how many units they must sell
    to cover their costs.

    Return the number of units required to break even.
    """
    unit = fixed_cost / (-cost_per_unit + sell_price)

    return unit

# print(calculate_break_even_point(1000, 5, 15))
def validate_truck_load(boxes, weight_limit, volume_limit):
    """
    Context: Logistics. Can a specific list of boxes fit into a delivery truck
    without exceeding the Maximum Weight OR the Maximum Volume?

    Args:
        boxes (list of tuples): Each tuple is (weight, volume) for one box.
        weight_limit (float): Max weight truck can carry.
        volume_limit (float): Max space in the truck.
    """
    weight_count = 0
    volume_count = 0
    for (weight, volume) in boxes:
        weight_count += weight
        volume_count += volume
    if weight_count <= weight_limit and volume_count <= volume_limit:
        return True

    return False
