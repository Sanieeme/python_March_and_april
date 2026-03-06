import numpy as np
import matplotlib.pyplot as plt

def breakeven_point(cost_A_params, cost_B_params):
    """
    Financial Analysis / Software Subscription Models context.

    Determine the usage unit 'u' where the total cost of Plan A equals
    the total cost of Plan B. Both costs follow a linear model: C(u) = F + M * u.

    Use matplotlib and numpy to help you visualize the two cost functions and their intersection point.

    Args:
        cost_A_params (list[float]): (F_A, M_A) - Fixed cost and marginal cost for Plan A.
        cost_B_params (list[float]): (F_B, M_B) - Fixed cost and marginal cost for Plan B.

    The breakeven point is found by solving F_A + M_A * u = F_B + M_B * u for u.

    Returns:
        float: The usage unit u at the breakeven point.
               Returns -1.0 if the marginal costs are equal (parallel lines).
    """
    # x = numpy.array(cost_A_params)
    # y = numpy.array(cost_B_params)
    # plt.plot(x, y)
    # plt.show()
    F_A, M_A = cost_A_params
    F_B, M_B = cost_B_params
    if M_A == M_B:
        return -1
    
    u = (F_B - F_A) / (M_A - M_B)
    usage = np.linspace(0, 100, 100)
    
    cost_a = F_A + M_A * usage
    cost_b = F_B + M_B * usage
    plt.plot(usage, cost_a, label="A")
    plt.plot(usage, cost_b, label="B")
    break_cost = F_A + M_A * u
    plt.scatter(u, break_cost)
    plt.text(u, break_cost, "Breakeven_point")
    
    plt.xlabel("u usage")
    plt.ylabel("total Cost")
    plt.title("breakeven analysis")
    plt.legend()
    plt.show()
    return u

print(breakeven_point((50, 5), (100, 3)))
def net_flow_accumulation(flow_rate_coefficients, time_start, time_end):
    """
    Water Resource Management / System Flow Rate context.

    Given a flow rate R(t) modeled by a quadratic function R(t) = a*t^2 + b*t + c,
    compute the total net accumulated amount over a time interval [time_start, time_end].

    This requires computing the definite integral of R(t) from time_start to time_end.

    Use matplotlib and numpy to help you visualize the flow rate function and the area under the curve.

    Args:
        flow_rate_coefficients (list[float]): (a, b, c) coefficients of the quadratic rate function.
        time_start (float): The starting time t_start.
        time_end (float): The ending time t_end.

    Returns:
        float: The total accumulated net amount (Volume) over the interval.
    """

    # The antiderivative F(t) is (a/3)*t^3 + (b/2)*t^2 + c*t
    # Result is F(time_end) - F(time_start)
    a, b, c = flow_rate_coefficients

    new_start = ((a/3)*time_start**3) + ((b/2)*time_start**2) + (c*time_start)
    new_end = ((a/3)*time_end**3) + ((b/2)*time_end**2) + (c*time_end)
    
    t = np.linspace(time_start - 2, time_end + 2, 200)
    R = a * t **2 + b*t + c
    plt.plot(t, R, label="Flow Rate R(t)")
    t_fill = np.linspace(time_start, time_end, 100)
    R_fill = a * t_fill **2 + b*t_fill + c
    
    plt.fill_between(t_fill, R_fill)
    plt.xlabel("Time")
    plt.ylabel("flow Rate")
    plt.title("Net Flow Accumulation")
    plt.legend()
    plt.show()
    return new_end - new_start

print(net_flow_accumulation([50, -20, 5], 1, 3))
