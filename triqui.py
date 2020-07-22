# import plotly.graph_objects as go
import dash
from dash.dependencies import State, Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import numpy as np
from Logica import *

tablero = tablero_inicial()

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
        dbc.Col('', id='casillas'),
        dbc.Col('', id='tablero')
    ])
])


###############################################
# BOTON-11
# Pone una X en el boton-11
@app.callback([Output('boton-11', 'color'),
Output('boton-11', 'disabled'),#
#Output('comp_status', 'children')
], [Input('boton-11', 'n_clicks')])
def on_button_click(n):

    global tablero

    if n is None:
        return 'secondary', False#, 'Computador en espera'
    else:
        tablero[0, 0] = 2
        return 'primary', True#, 'Computando jugada...'
# BOTON-12
@app.callback([Output('boton-12', 'color'),
Output('boton-12', 'disabled')#,
#Output('comp_status', 'children')
], [Input('boton-12', 'n_clicks')])
def on_button_click(n):

    global tablero

    if n is None:
        return 'secondary', False#, 'Computador en espera'
    else:
        tablero[0, 1] = 2
        return 'primary', True#, 'Computando jugada...'

# BOTON-13
@app.callback([Output('boton-13', 'color'),
Output('boton-13', 'disabled')],
[Input('boton-13', 'n_clicks')])
def on_button_click(n):

    global tablero

    if n is None:
        return 'secondary', False#, 'Computador en espera'
    else:
        tablero[0, 2] = 2
        return 'primary', True#, 'Computando jugada...'

# BOTON-21
@app.callback([Output('boton-21', 'color'),
Output('boton-21', 'disabled')],
[Input('boton-21', 'n_clicks')])
def on_button_click(n):

    global tablero

    if n is None:
        return 'secondary', False#, 'Computador en espera'
    else:
        tablero[1, 0] = 2
        return 'primary', True#, 'Computando jugada...'

# BOTON-22
@app.callback([Output('boton-22', 'color'),
Output('boton-22', 'disabled')],
[Input('boton-22', 'n_clicks')])
def on_button_click(n):

    global tablero

    if n is None:
        return 'secondary', False#, 'Computador en espera'
    else:
        tablero[1, 1] = 2
        return 'primary', True#, 'Computando jugada...'

# BOTON-23
@app.callback([Output('boton-23', 'color'),
Output('boton-23', 'disabled')],
[Input('boton-23', 'n_clicks')])
def on_button_click(n):

    global tablero

    if n is None:
        return 'secondary', False#, 'Computador en espera'
    else:
        tablero[1, 2] = 2
        return 'primary', True#, 'Computando jugada...'

# BOTON-31
@app.callback([Output('boton-31', 'color'),
Output('boton-31', 'disabled')],
[Input('boton-31', 'n_clicks')])
def on_button_click(n):

    global tablero

    if n is None:
        return 'secondary', False#, 'Computador en espera'
    else:
        tablero[2, 0] = 2
        return 'primary', True#, 'Computando jugada...'

# BOTON-32
@app.callback([Output('boton-32', 'color'),
Output('boton-32', 'disabled')],
[Input('boton-32', 'n_clicks')])
def on_button_click(n):

    global tablero

    if n is None:
        return 'secondary', False#, 'Computador en espera'
    else:
        tablero[2, 1] = 2
        return 'primary', True#, 'Computando jugada...'

# BOTON-33
@app.callback([Output('boton-33', 'color'),
Output('boton-33', 'disabled')],
[Input('boton-33', 'n_clicks')])
def on_button_click(n):

    global tablero

    if n is None:
        return 'secondary', False#, 'Computador en espera'
    else:
        tablero[2, 2] = 2
        return 'primary', True#, 'Computando jugada...'

@app.callback(Output('comp_status', 'children'),
[Input('boton-11', 'n_clicks'),
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

@app.callback([Output('tablero', 'children'),
Output('boton-11', 'children'),
Output('boton-12', 'children'),
Output('boton-13', 'children'),
Output('boton-21', 'children'),
Output('boton-22', 'children'),
Output('boton-23', 'children'),
Output('boton-31', 'children'),
Output('boton-32', 'children'),
Output('boton-33', 'children'),
],
[Input('comp_status', 'children')])
def computa_jugada(estado):

    global tablero

    if estado == ['Computando Jugada...']:
        if triqui(tablero,0) == 0:
            antiguo_tablero = tablero
            tablero = jugar(tablero)
            if len(tablero) == 0:
                cambio = False
                for fila in range(3):
                    for columna in range(3):
                        if not cambio and antiguo_tablero[fila,columna]==0:
                            antiguo_tablero[fila,columna] = 1
                            cambio = True
                tablero = antiguo_tablero
            mensaje = 'Computador gana' if triqui(tablero,0)==1 else ''
            return mensaje, tablero[0,0], tablero[0,1], tablero[0,2],\
                tablero[1,0], tablero[1,1], tablero[1,2],\
                tablero[2,0], tablero[2,1], tablero[2,2]
        else:
            return "Humano gana", tablero[0,0], tablero[0,1], tablero[0,2],\
                tablero[1,0], tablero[1,1], tablero[1,2],\
                tablero[2,0], tablero[2,1], tablero[2,2]
    else:
        return '', tablero[0,0], tablero[0,1], tablero[0,2],\
               tablero[1,0], tablero[1,1], tablero[1,2],\
               tablero[2,0], tablero[2,1], tablero[2,2]


if __name__ == '__main__':
    app.run_server(debug=True)
