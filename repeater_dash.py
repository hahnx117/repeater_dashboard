from dash import Dash, html, dash_table, dcc, callback, Output, Input
import json

FILENAME = 'repeater_dict.json'

with open(FILENAME, 'r') as f:
    REPEATER_INFO = json.loads(f.read()) 

frequency_list = list(REPEATER_INFO.keys())

app = Dash(__name__)

app.layout = [
    html.Div(className='row', children='Repeater Info by Frequency',
             style={'textAlign': 'center', 'color': 'blue', 'fontSize': 30}),
    html.Div(className='row', children=[
        dcc.Dropdown(frequency_list, frequency_list[0], id='frequency-dropdown'),
        ]
    ),
    html.Div(className='row', id='dd-output-container'),
    html.Div(className='row', children=[
        html.Div(className='column'),
        html.Div(className='column'),
        html.Div(className='column'),
    ])
]

@callback(
    Output('dd-output-container', 'children'),
    Input('frequency-dropdown', 'value')
)
def update_output(value):
    return f"{value}, {REPEATER_INFO[str(value)]['callsign']}: The distance is {REPEATER_INFO[str(value)]['distance']:.2f} miles. The bearing is {REPEATER_INFO[str(value)]['bearing']:.2f} degrees."

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)