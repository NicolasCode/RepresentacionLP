# import plotly.graph_objects as go
import dash
from dash.dependencies import State, Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import numpy as np
import base64

# values = [['a11', 'a21', 'a31'], #1st col
#             ['a12', 'a22', 'a32'], #1st col
#             ['a13', 'a23', 'a33'], #1st col
#             ]
#
# fig = go.Figure(data=[go.Table(
#   columnorder = [1,2,3],
#   columnwidth = [10,10,10],
#   # header = dict(
#   #   values = [['<b>EXPENSES</b><br>as of July 2017'],
#   #                 ['<b>DESCRIPTION</b>'],
#   #                 ['<b>Otra</b>']],
#   #   line_color='darkslategray',
#   #   fill_color='royalblue',
#   #   align=['center','center','center'],
#   #   font=dict(color='white', size=12),
#   #   height=40
#   # ),
#   cells=dict(
#     values=values,
#     line_color='darkslategray',
#     fill=dict(color=['paleturquoise', 'white']),
#     align=['left', 'center'],
#     font_size=12,
#     height=30)
#     )
# ])

# triqui = dash.Dash()
app = dash.Dash(external_stylesheets=[dbc.themes.LUX])
app.title='Triqui'

colors = {
    'background': '#b2b5df',
    'text': '#6c788e',
    'Nada': '#b2b5df'
}

ficha = {}
for i in range(3):
    for j in range(3):
        ficha[str(i + 1) + str(j + 1)] = '_'

ficha['22'] = 'O'

app.layout = dbc.Container(fluid=True, children=[
    html.Br(),
    ## Top
    html.H1(children = 'El juego del TRIQUI',
        style = {
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Br(),
    html.Br(),
    html.H6(children = 'Haga su jugada con las \'X\''+\
                       ' dando click en alguna de las casillas libres:',
        style = {'color': colors['text']}
    ),
    html.Br(),
    html.Br(),
    dbc.Row([
        dbc.Col(''),
        dbc.Col(children=[
            dbc.Row([
                dbc.Col(dbc.Button(ficha['11'],
                                    id="boton-11",
                                    style={'font-size':'30px'}
                                    )
                        ),
                dbc.Col(dbc.Button(ficha['12'],
                                    id="boton-12",
                                    style = {'font-size':'30px'}
                                    )
                        ),
                dbc.Col(dbc.Button(ficha['13'],
                                    id="boton-13",
                                    style = {'font-size':'30px'}
                                    ))
            ]),
            dbc.Row([
                dbc.Col(dbc.Button(ficha['21'],
                                    id="boton-21",
                                    style = {'font-size':'30px'}
                                    )),
                dbc.Col(dbc.Button(ficha['22'],
                                    id="boton-22",
                                    style = {'font-size':'30px'}
                                    )),
                dbc.Col(dbc.Button(ficha['23'],
                                    id="boton-23",
                                    style = {'font-size':'30px'}
                                    ))
            ]),
            dbc.Row([
                dbc.Col(dbc.Button(ficha['31'],
                                    id="boton-31",
                                    style = {'font-size':'30px'}
                                    )),
                dbc.Col(dbc.Button(ficha['32'],
                                    id="boton-32",
                                    style = {'font-size':'30px'}
                                    )),
                dbc.Col(dbc.Button(ficha['33'],
                                    id="boton-33",
                                    style = {'font-size':'30px'}
                                    ))
            ])
        ]),
        dbc.Col('')
    ]),
    html.Br(),
    html.Br(),
    dbc.Row([
        dbc.Col('Computador en espera', id='comp_status'),
        dbc.Col(''),
        dbc.Col('')
    ])
])


###############################################
# BOTON-11
# Pone una X en el boton-11
@app.callback([Output('boton-11', 'children'),
Output('boton-11', 'disabled'),#
#Output('comp_status', 'children')
], [Input('boton-11', 'n_clicks')])
def on_button_click(n):
    if n is None:
        return '_', False#, 'Computador en espera'
    else:
        return 'X', True#, 'Computando jugada...'
# BOTON-12
@app.callback([Output('boton-12', 'children'),
Output('boton-12', 'disabled')#,
#Output('comp_status', 'children')
], [Input('boton-12', 'n_clicks')])
def on_button_click(n):
    if n is None:
        return '_', False#, 'Computador en espera'
    else:
        return 'X', True#, 'Computando jugada...'

# BOTON-13
@app.callback([Output('boton-13', 'children'),
Output('boton-13', 'disabled')],
[Input('boton-13', 'n_clicks')])
def on_button_click(n):
    if n is None:
        return '_', False
    else:
        return 'X', True

# BOTON-21
@app.callback([Output('boton-21', 'children'),
Output('boton-21', 'disabled')],
[Input('boton-21', 'n_clicks')])
def on_button_click(n):
    if n is None:
        return '_', False
    else:
        return 'X', True

# BOTON-22
@app.callback([Output('boton-22', 'children'),
Output('boton-22', 'disabled')],
[Input('boton-22', 'n_clicks')])
def on_button_click(n):
    if n is None:
        return '_', False
    else:
        return 'X', True

# BOTON-23
@app.callback([Output('boton-23', 'children'),
Output('boton-23', 'disabled')],
[Input('boton-23', 'n_clicks')])
def on_button_click(n):
    if n is None:
        return '_', False
    else:
        return 'X', True

# BOTON-31
@app.callback([Output('boton-31', 'children'),
Output('boton-31', 'disabled')],
[Input('boton-31', 'n_clicks')])
def on_button_click(n):
    if n is None:
        return '_', False
    else:
        return 'X', True

# BOTON-32
@app.callback([Output('boton-32', 'children'),
Output('boton-32', 'disabled')],
[Input('boton-32', 'n_clicks')])
def on_button_click(n):
    if n is None:
        return '_', False
    else:
        return 'X', True

# BOTON-33
@app.callback([Output('boton-33', 'children'),
Output('boton-33', 'disabled')],
[Input('boton-33', 'n_clicks')])
def on_button_click(n):
    if n is None:
        return '_', False
    else:
        return 'X', True

@app.callback([Output('comp_status', 'children')
], [Input('boton-11', 'n_clicks'),
Input('boton-12', 'n_clicks'),
Input('boton-13', 'n_clicks'),
Input('boton-21', 'n_clicks'),
Input('boton-22', 'n_clicks'),
Input('boton-23', 'n_clicks'),
Input('boton-31', 'n_clicks'),
Input('boton-32', 'n_clicks'),
Input('boton-33', 'n_clicks')
])
def frase_final(a,b,c,d,e,f,g,h,i):
    if a is not None:
        return ['Computando Jugada...']
    elif b is not None:
        return ['Computando Jugada...']
    elif c is not None:
        return ['Computando Jugada...']
    elif d is not None:
        return ['Computando Jugada...']
    elif e is not None:
        return ['Computando Jugada...']
    elif f is not None:
        return ['Computando Jugada...']
    elif g is not None:
        return ['Computando Jugada...']
    elif h is not None:
        return ['Computando Jugada...']
    elif i is not None:
        return ['Computando Jugada...']
    else:
        return ['Computador en espera']

if __name__ == '__main__':
    app.run_server(debug=True)
