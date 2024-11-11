import streamlit as st
from typing import Callable

from src.app.config import page_config

class Sidebar:
    """Classe pour gérer les éléments de la sidebar de l'application."""

    def __init__(self):
        self.init_sidebar(page_config)

        st.sidebar.header("Paramètres")
        self.property_price = st.sidebar.number_input(
            "Prix du bien immobilier (€)", value=200000, step=10000
        )
        self.dividend_tax_rate = (
            st.sidebar.number_input(
                "Montant de la flax tax (%)", value=30.0, step=1.0
            ) / 100
        )
        self.rent_per_month = st.sidebar.number_input("Loyer mensuel (€)", value=700, step=50)
        self.years = st.sidebar.number_input("Période d'analyse (années)", value=20, step=1)

    def init_sidebar(self, page_config: Callable):
        with st.sidebar:
            try:
                logo_path = page_config().get("page_logo")
            except FileNotFoundError:
                raise FileNotFoundError("page_logo path not found")

            desired_width = 60

            col1, col2 = st.columns([1, 3])

            with col1:
                st.image(logo_path, width=desired_width)
            with col2:
                st.write(page_config().get("sidebar_title"))

            st.caption(page_config().get("page_description"))
            st.divider()

    def get_parameters(self) -> dict:
        """Retourne les paramètres d'entrée pour les calculs."""
        return {
            "property_price": self.property_price,
            "dividend_tax_rate": self.dividend_tax_rate,
            "rent_per_month": self.rent_per_month,
            "years": self.years,
        }
