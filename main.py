import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import graphs as g
from graphs import create_map, create_counters

stl = {'textAlign': 'left','font-family': "asimov",'color':'#cccccc'}
app = dash.Dash()
app.layout = html.Div(className='row', children=
    [
    html.H1(children = "Credit card fraud transaction simulator", style=stl),
    html.Div(children ='Note: double click on a category to only show it, single click to exclude it ', style=stl),
    dcc.Graph(
        id = "map_graph",
        animate = True,
        figure =g.fig,
        style={'width': '100vh', 'height': '50vh'}
    ),
    dcc.Graph(
        id = "fraud_counters",
        animate = True,
        style={'width': '100vh', 'height': '50vh'},
        figure =g.fig2
    ),dcc.Interval(id = 'interval-component', interval = 500,n_intervals = 0)
])

@app.callback(
    [Output('map_graph', 'figure'),Output('fraud_counters','figure')],
    [Input('interval-component', 'n_intervals')]
)

def update_graph(n):
    g.fig = create_map()
    g.fig2 = create_counters()
    return g.fig, g.fig2

if __name__ == '__main__':
    app.run(debug=True)