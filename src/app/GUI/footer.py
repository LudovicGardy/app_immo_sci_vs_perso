import streamlit as st

class Footer:
    """Classe pour afficher le footer de l'application."""

    def __init__(self):
        """Initialisation de la classe."""
        self.footer = st.empty()

    def display(self):
        """Affichage du footer."""
        st.write("---")
        st.caption(
            "D'autres optimisations fiscales peuvent être envisagées pour réduire les coûts. Comme le remboursement d'une partie du loyer par une autre société (sous-location), la déduction de certains coûts du bénéfice de la SCI: notaire, travaux, comptable..."
        )
        st.write("---")