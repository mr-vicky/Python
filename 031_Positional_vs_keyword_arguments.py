def net_sal(basic, allowance, deduction):
    net = basic + allowance - deduction
    return net

# positional arguments
print(net_sal(8000, 6000, 2000))

# Keyword Arguments
print(net_sal(allowance=6000, basic=8000, deduction=2000))