import streamlit as st

class Sidebar:
    """Classe pour gérer les éléments de la sidebar de l'application."""

    def __init__(self):
        st.sidebar.header("Paramètres")
        self.property_price = st.sidebar.number_input(
            "Prix du bien immobilier (€)", value=300000, step=10000
        )
        self.dividend_tax_rate = (
            st.sidebar.number_input(
                "Taux d'imposition sur les dividendes (%)", value=30.0, step=1.0
            ) / 100
        )
        self.rent_per_month = st.sidebar.number_input("Loyer mensuel (€)", value=700, step=50)
        self.years = st.sidebar.number_input("Période d'analyse (années)", value=20, step=1)

    def get_parameters(self):
        """Retourne les paramètres d'entrée pour les calculs."""
        return {
            "property_price": self.property_price,
            "dividend_tax_rate": self.dividend_tax_rate,
            "rent_per_month": self.rent_per_month,
            "years": self.years,
        }
