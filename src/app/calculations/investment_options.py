from abc import ABC, abstractmethod

from src.app.calculations.from_dividend_to_CA import calculate_revenue_for_dividends
from src.app.calculations.impot_societe_from_CA import calculate_corporate_tax


class InvestmentOption(ABC):
    """Classe de base abstraite pour les options d'investissement."""

    @abstractmethod
    def calculate(self) -> dict:
        """Calcule les détails financiers de l'option d'investissement.

        Returns:
            dict: Un dictionnaire contenant les résultats des calculs.
        """
        pass


class PersonalPurchase(InvestmentOption):
    """Option d'investissement pour un achat personnel avec dividendes."""

    def __init__(self, property_price: float, dividend_tax_rate: float):
        """Initialise l'option d'achat personnel.

        Args:
            property_price (float): Prix du bien immobilier en euros.
            dividend_tax_rate (float): Taux d'imposition sur les dividendes (décimal).
        """
        self.property_price = property_price
        self.dividend_tax_rate = dividend_tax_rate

    def calculate(self) -> dict:
        """Calcule les dividendes bruts nécessaires et le total des taxes payées.

        Returns:
            dict: Résultats des calculs incluant les dividendes bruts nécessaires et 
            le total des taxes payées.
        """
        gross_dividends_needed = self.property_price / (1 - self.dividend_tax_rate)
        flat_tax_paid = gross_dividends_needed * self.dividend_tax_rate
        CA_required = calculate_revenue_for_dividends(gross_dividends_needed)
        return {
            "gross_dividends_needed": gross_dividends_needed,
            "CA_required": CA_required,
            "IS_paid": calculate_corporate_tax(CA_required),
            "flat_tax_paid": flat_tax_paid,
        }


class SCIInvestment(InvestmentOption):
    """Option d'investissement pour un achat via holding et SCI à l'IS."""

    def __init__(
        self,
        rent_per_month: float,
        dividend_tax_rate: float,
        years: int,
    ):
        """Initialise l'option d'investissement via SCI.

        Args:
            rent_per_month (float): Loyer mensuel en euros.
            dividend_tax_rate (float): Taux d'imposition sur les dividendes (décimal).
            years (int): Nombre d'années pour l'analyse.
        """
        self.rent_per_month = rent_per_month
        self.dividend_tax_rate = dividend_tax_rate
        self.years = years

    def calculate(self) -> dict:
        """Calcule les détails financiers de l'investissement via SCI.

        Returns:
            dict: Résultats des calculs incluant le loyer annuel, les dividendes nets reçus,
            le coût net annuel et le coût total sur les années.
        """
        annual_rent = self.rent_per_month * 12
        corporate_tax = calculate_corporate_tax(annual_rent)
        sci_profit_after_tax = annual_rent - corporate_tax
        net_dividends_received = sci_profit_after_tax * (1 - self.dividend_tax_rate)
        net_annual_cost = annual_rent - net_dividends_received
        total_cost_over_years = net_annual_cost * self.years
        initial_cost_holding_sci = 10000.0
        return {
            "initial_cost_holding_sci": initial_cost_holding_sci,
            "annual_rent": annual_rent,
            "net_dividends_received": net_dividends_received,
            "net_annual_cost": net_annual_cost,
            "rent_cost_over_years": total_cost_over_years,
            "total_cost_over_years": total_cost_over_years + initial_cost_holding_sci,
        }
