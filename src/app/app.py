import streamlit as st
from src.app.calculations.investment_options import PersonalPurchase, SCIInvestment
from src.app.utils.data_visualization import plot_total_costs, plot_annual_costs

def main():
    """Fonction principale pour exécuter l'application Streamlit."""
    st.title("Comparaison des options d'investissement immobilier")

    st.sidebar.header("Paramètres")

    # Paramètres d'entrée
    property_price = st.sidebar.number_input("Prix du bien immobilier (€)", value=300000, step=10000)
    dividend_tax_rate = st.sidebar.number_input("Taux d'imposition sur les dividendes (%)", value=30.0, step=0.1) / 100
    corporate_tax_rate = st.sidebar.number_input("Taux d'impôt sur les sociétés (%)", value=25.0, step=0.1) / 100
    rent_per_month = st.sidebar.number_input("Loyer mensuel (€)", value=700, step=50)
    years = st.sidebar.number_input("Période d'analyse (années)", value=20, step=1)

    # Calculs
    option1 = PersonalPurchase(property_price, dividend_tax_rate)
    option1_result = option1.calculate()

    option2 = SCIInvestment(rent_per_month, corporate_tax_rate, dividend_tax_rate, int(years))
    option2_result = option2.calculate()

    # Affichage des résultats
    st.write("## Option 1: Achat personnel avec dividendes")
    st.write(f"Montant brut de dividendes nécessaire: **{option1_result['gross_dividends_needed']:.2f} €**")
    st.write(f"Total des taxes payées sur les dividendes: **{option1_result['total_tax_paid']:.2f} €**")

    st.write("---")

    st.write("## Option 2: Achat via holding + SCI à l'IS")
    st.write(f"Loyer annuel payé: **{option2_result['annual_rent']:.2f} €**")
    st.write(f"Dividendes nets reçus de la SCI: **{option2_result['net_dividends_received']:.2f} €**")
    st.write(f"Coût net annuel: **{option2_result['net_annual_cost']:.2f} €**")
    st.write(f"Coût total des loyers sur {years} ans: **{option2_result['total_cost_over_years']:.2f} €**")
    
    st.write("---")
    
    st.write("A noter que d'autres optimisations fiscales peuvent être envisagées pour réduire les coûts. Comme le remboursement d'une partie du loyer par une autre société (sous-location), la déduction de certains coûts du bénéfice de la SCI: notaire, travaux, comptable...")

    st.write("---")

    # Visualisations avec Plotly
    st.write("## Comparaison des coûts totaux")
    fig1 = plot_total_costs(option1_result['total_tax_paid'], option2_result['total_cost_over_years'])
    st.plotly_chart(fig1, use_container_width=True)

    st.write("## Évolution du coût net annuel sur les années (Option 2)")
    fig2 = plot_annual_costs(int(years), option2_result['net_annual_cost'])
    st.plotly_chart(fig2, use_container_width=True)