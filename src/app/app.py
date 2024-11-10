import streamlit as st
from src.app.GUI.sidebar import Sidebar
from src.app.GUI.home import Home

def main():
    """Fonction principale pour exécuter l'application Streamlit."""
    # Sidebar
    sidebar = Sidebar()
    params = sidebar.get_parameters()

    # Home
    home = Home(params)
    home.display()

    # Shared accross pages
    st.write("---")
    st.caption(
        "D'autres optimisations fiscales peuvent être envisagées pour réduire les coûts. Comme le remboursement d'une partie du loyer par une autre société (sous-location), la déduction de certains coûts du bénéfice de la SCI: notaire, travaux, comptable..."
    )
    st.write("---")

if __name__ == "__main__":
    main()
