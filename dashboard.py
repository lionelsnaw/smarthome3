import pathlib
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

app_path = str(pathlib.Path(__file__).parent.resolve())
df = pd.read_csv(os.path.join(app_path, os.path.join("data", "smarthome.csv")))

app = dash.Dash(__name__, url_base_pathname='/dashboard/')
server = app.server

theme = {
    'background': '#111111',
    'text': '#7FDBFF'
}


def build_banner():
    return html.Div(
        className='col-sm-10 row banner',
        children=[
            html.Div(
                className='banner-text',
                children=[
                    html.H5('Enegry Consumption'),
                ],
            ),
        ],
    )


def build_graph():
    return dcc.Graph(
        id='basic-interactions',
        figure={
            'data': [
                {
                    'x': df['time'],
                    'y': df['acc_x'],
                    'name': 'Accelerometer by X-axis',
                    'marker': {'size': 12}
                },
                {
                    'x': df['time'],
                    'y': df['acc_z'],
                    'name': 'Accelerometer by Y-axis',
                    'marker': {'size': 12}
                },
                {
                    'x': df['time'],
                    'y': df['gyro_x'],
                    'name': 'Gyroscope by X-axis',
                    'marker': {'size': 12}
                },
                {
                    'x': df['time'],
                    'y': df['gyro_y'][:50],
                    'name': 'Gyroscope by Y-axis',
                    'marker': {'size': 12}
                },
                {
                    'x': df['time'],
                    'y': df['gyro_x'],
                    'name': 'Gyroscope by Z-axis',
                    'marker': {'size': 12}
                },
            ],
            'layout': {
                'plot_bgcolor': theme['background'],
                'paper_bgcolor': theme['background'],
                'font': {
                    'color': theme['text']
                }
            }
        }
    )


app.layout = html.Div(
    className='big-app-container',
    children=[
        build_banner(),
        html.Div(
            className='app-container',
            children=[
                build_graph(),
            ]
        )
    ]
)
