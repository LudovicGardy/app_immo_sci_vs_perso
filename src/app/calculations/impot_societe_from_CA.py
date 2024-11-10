def calculate_corporate_tax(
    gross_profit: float,
    threshold_cit: float = 42500,
    reduced_cit_rate: float = 0.15,
    normal_cit_rate: float = 0.25,
) -> float:
    """
    Calculates the corporate income tax (CIT) based on the gross profit, using a 
    reduced rate up to a specified threshold, and a normal rate above it.

    Args:
        gross_profit (float): The gross profit amount on which the CIT is calculated.
        threshold_cit (float, optional): The profit threshold for applying the reduced CIT rate. Default is 42,500 €.
        reduced_cit_rate (float, optional): The reduced CIT rate applied below the threshold. Default is 15%.
        normal_cit_rate (float, optional): The normal CIT rate applied above the threshold. Default is 25%.

    Returns:
        float: The calculated amount of corporate income tax.
    """
    if gross_profit <= threshold_cit:
        # If the gross profit is within the reduced rate threshold
        corporate_tax = gross_profit * reduced_cit_rate
    else:
        # Apply the reduced rate up to the threshold, and the normal rate above it
        tax_below_threshold = threshold_cit * reduced_cit_rate
        tax_above_threshold = (gross_profit - threshold_cit) * normal_cit_rate
        corporate_tax = tax_below_threshold + tax_above_threshold

    return corporate_tax


# Example usage
gross_profit = 100000  # Example gross profit in euros
corporate_tax = calculate_corporate_tax(gross_profit)
print(
    f"The corporate income tax for a gross profit of {gross_profit}€ is {corporate_tax:.2f}€"
)
