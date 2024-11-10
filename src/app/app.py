import streamlit as st
from src.app.GUI.sidebar import Sidebar
from src.app.GUI.home import Home
from src.app.GUI.footer import Footer

def main():
    """Fonction principale pour exécuter l'application Streamlit."""
    st.title("Comparaison des options d'investissement immobilier")

    # Sidebar
    sidebar = Sidebar()
    params = sidebar.get_parameters()

    # Home
    home = Home(params)
    home.display()

    # Shared accross pages
    footer = Footer()
    footer.display()

if __name__ == "__main__":
    main()
