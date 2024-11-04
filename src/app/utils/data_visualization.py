# investment_app/utils/data_visualization.py

import plotly.graph_objects as go

def plot_total_costs(option1_cost: float, option2_cost: float) -> go.Figure:
    """Crée un diagramme en barres comparant les coûts totaux des deux options.

    Args:
        option1_cost (float): Coût total pour l'Option 1.
        option2_cost (float): Coût total pour l'Option 2.

    Returns:
        go.Figure: L'objet figure contenant le graphique.
    """
    options = ['Achat Personnel', 'Achat via SCI']
    costs = [option1_cost, option2_cost]

    fig = go.Figure(data=[
        go.Bar(
            x=options,
            y=costs,
            marker_color=['#1f77b4', '#ff7f0e']
        )
    ])

    fig.update_layout(
        title='Coût Total par Option',
        xaxis_title='Option',
        yaxis_title='Coût Total (€)',
        template='plotly_white'
    )

    return fig

def plot_annual_costs(years: int, net_annual_cost: float) -> go.Figure:
    """Trace le coût cumulé annuel sur le nombre d'années spécifié.

    Args:
        years (int): Nombre d'années.
        net_annual_cost (float): Coût net annuel.

    Returns:
        go.Figure: L'objet figure contenant le graphique.
    """
    years_range = list(range(1, years + 1))
    cumulative_costs = [net_annual_cost * year for year in years_range]

    fig = go.Figure(data=[
        go.Scatter(
            x=years_range,
            y=cumulative_costs,
            mode='lines+markers',
            line=dict(color='#ff7f0e'),
            marker=dict(size=8)
        )
    ])

    fig.update_layout(
        title='Coût Cumulé sur les Années (Option 2)',
        xaxis_title='Année',
        yaxis_title='Coût Cumulé (€)',
        template='plotly_white'
    )

    return fig
