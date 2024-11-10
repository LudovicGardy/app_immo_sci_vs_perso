import streamlit as st
from src.app.calculations.investment_options import PersonalPurchase, SCIInvestment
from src.app.utils.data_visualization import plot_total_costs, plot_annual_costs


class Home:
    """Classe pour gérer les calculs et l'affichage des résultats."""

    def __init__(self, params):
        self.property_price = params["property_price"]
        self.dividend_tax_rate = params["dividend_tax_rate"]
        self.rent_per_month = params["rent_per_month"]
        self.years = params["years"]

    def display(self):
        """Affiche les résultats de la comparaison des options d'investissement immobilier."""

        st.title("Comparaison des options d'investissement immobilier")

        option1 = PersonalPurchase(self.property_price, self.dividend_tax_rate)
        option1_result = option1.calculate()

        option2 = SCIInvestment(
            self.rent_per_month, self.dividend_tax_rate, int(self.years)
        )
        option2_result = option2.calculate()

        tab1, tab2 = st.tabs(["📐 Calculs", "📊 Plots"])

        with tab1:
            st.write("## 1️⃣ Achat personnel avec dividendes d'une SASU")
            st.write("### 📃 Société d'exploitation: SASU")
            with st.container(border=True):
                st.write(
                    f"📍 Montant brut de dividendes nécessaire: **{option1_result['gross_dividends_needed']:.2f} €**"
                )
                st.write(
                    f"📍 Flat tax payée sur les dividendes: :red[**{option1_result['flat_tax_paid']:.2f} €**]"
                )
                st.caption(f"""Notez que le chiffre d'affaires nécessaire pour atteindre les dividendes 
                        désirés de {option1_result['gross_dividends_needed']:.2f} € est de: 
                        {option1_result['CA_required']:.2f} €, avec un IS payé 
                        de: {option1_result['IS_paid']:.2f} €.""")

            st.write("---")

            st.write("## 2️⃣ Achat professionnel via holding + SCI à l'IS")
            st.write("### 📃 Société d'exploitation: EURL")
            with st.container(border=True):
                st.write(
                    f"📍 Loyer annuel payé: **{option2_result['annual_rent']:.2f} €**"
                )
                st.write(
                    f"📍 Dividendes nets reçus de la SCI: **{option2_result['net_dividends_received']:.2f} €**"
                )
                st.write(
                    f"📍Coût net annuel: **{option2_result['net_annual_cost']:.2f} €**"
                )
                st.write(
                    f"""📍 Coût total sur {self.years} ans: :red[**{option2_result['total_cost_over_years']:.2f} €**] 
                    [loyers: {option2_result['rent_cost_over_years']}, cout inital: 
                    {option2_result['initial_cost_holding_sci']}]"""
                )
                st.caption("""Notez que le coût de l'IS pourra ici être légèrement inférieur à celui de l'option 1, 
                        car on déduit les salaires versés aux associés. Le montant de l'IS sera le même dans 
                        les deux cas si le salaire est nul ou identique dans les deux options. Sachant
                        que par contre, le taux de charges sur les salaires est plus avantageux en EURL.""")

        with tab2:
            st.write("## Comparaison des coûts totaux")
            fig1 = plot_total_costs(
                option1_result["flat_tax_paid"], option2_result["total_cost_over_years"]
            )
            st.plotly_chart(fig1, use_container_width=True)

            st.write("## Évolution du coût net annuel sur les années (Option 2)")
            fig2 = plot_annual_costs(int(self.years), option2_result["net_annual_cost"])
            st.plotly_chart(fig2, use_container_width=True)
