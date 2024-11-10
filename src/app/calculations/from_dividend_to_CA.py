def calculate_revenue_for_dividends(net_dividends: float, threshold_cit: float = 42500, reduced_cit_rate: float = 0.15, normal_cit_rate: float = 0.25) -> float:
    """
    Calculates the required revenue to achieve a given net dividend amount, considering applicable corporate income tax (CIT) rates.

    Args:
        net_dividends (float): Desired net dividend amount (in euros).
        threshold_cit (float, optional): Profit threshold for applying the reduced CIT rate. Default is 42,500 €.
        reduced_cit_rate (float, optional): Reduced CIT rate below the threshold. Default is 15%.
        normal_cit_rate (float, optional): Normal CIT rate above the threshold. Default is 25%.

    Returns:
        float: The required revenue to obtain the specified net dividend amount after taxes.
    """
    # Calculate the required profit after tax
    required_profit = net_dividends

    # Calculate the required gross profit based on CIT rates
    if required_profit <= threshold_cit * (1 - reduced_cit_rate):
        # If the required profit is below the threshold, only the reduced rate applies
        gross_profit = required_profit / (1 - reduced_cit_rate)
    else:
        # If the required profit exceeds the threshold, both rates apply
        remaining_profit = required_profit - threshold_cit * (1 - reduced_cit_rate)
        gross_profit = threshold_cit + (remaining_profit / (1 - normal_cit_rate))

    # With no expenses, the required revenue is equal to the required gross profit
    revenue = gross_profit
    return revenue
