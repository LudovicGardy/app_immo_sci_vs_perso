from abc import ABC, abstractmethod

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
            dict: Résultats des calculs incluant les dividendes bruts nécessaires et le total des taxes payées.
        """
        gross_dividends_needed = self.property_price / (1 - self.dividend_tax_rate)
        total_tax_paid = gross_dividends_needed * self.dividend_tax_rate
        return {
            'gross_dividends_needed': gross_dividends_needed,
            'total_tax_paid': total_tax_paid
        }

class SCIInvestment(InvestmentOption):
    """Option d'investissement pour un achat via holding et SCI à l'IS."""

    def __init__(self, rent_per_month: float, corporate_tax_rate: float, dividend_tax_rate: float, years: int):
        """Initialise l'option d'investissement via SCI.

        Args:
            rent_per_month (float): Loyer mensuel en euros.
            corporate_tax_rate (float): Taux d'impôt sur les sociétés (décimal).
            dividend_tax_rate (float): Taux d'imposition sur les dividendes (décimal).
            years (int): Nombre d'années pour l'analyse.
        """
        self.rent_per_month = rent_per_month
        self.corporate_tax_rate = corporate_tax_rate
        self.dividend_tax_rate = dividend_tax_rate
        self.years = years

    def calculate(self) -> dict:
        """Calcule les détails financiers de l'investissement via SCI.

        Returns:
            dict: Résultats des calculs incluant le loyer annuel, les dividendes nets reçus, le coût net annuel et le coût total sur les années.
        """
        annual_rent = self.rent_per_month * 12
        sci_profit_after_tax = annual_rent * (1 - self.corporate_tax_rate)
        net_dividends_received = sci_profit_after_tax * (1 - self.dividend_tax_rate)
        net_annual_cost = annual_rent - net_dividends_received
        total_cost_over_years = net_annual_cost * self.years
        return {
            'annual_rent': annual_rent,
            'net_dividends_received': net_dividends_received,
            'net_annual_cost': net_annual_cost,
            'total_cost_over_years': total_cost_over_years
        }
