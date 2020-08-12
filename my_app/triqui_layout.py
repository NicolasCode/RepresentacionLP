import dash_html_components as html
import dash_bootstrap_components as dbc

triqui_layout = dbc.Container(children=[
    dbc.Row([
        dbc.Col(dbc.Button(#ficha['11'],
                            id="boton-11",
                            style={'font-size':'30px'}
                            )
                ),
        dbc.Col(dbc.Button(#ficha['12'],
                            id="boton-12",
                            style = {'font-size':'30px'}
                            )
                ),
        dbc.Col(dbc.Button(#ficha['13'],
                            id="boton-13",
                            style = {'font-size':'30px'}
                            ))
    ]),
    dbc.Row([
        dbc.Col(dbc.Button(#ficha['21'],
                            id="boton-21",
                            style = {'font-size':'30px'}
                            )),
        dbc.Col(dbc.Button(#ficha['22'],
                            id="boton-22",
                            style = {'font-size':'30px'}
                            )),
        dbc.Col(dbc.Button(#ficha['23'],
                            id="boton-23",
                            style = {'font-size':'30px'}
                            ))
    ]),
    dbc.Row([
        dbc.Col(dbc.Button(#ficha['31'],
                            id="boton-31",
                            style = {'font-size':'30px'}
                            )),
        dbc.Col(dbc.Button(#ficha['32'],
                            id="boton-32",
                            style = {'font-size':'30px'}
                            )),
        dbc.Col(dbc.Button(#ficha['33'],
                            id="boton-33",
                            style = {'font-size':'30px'}
                            ))
    ])
])

root_layout = dbc.Container(children=[
    html.H6(children = 'Haga su jugada con las \'X\''+\
                       ' dando click en alguna de las casillas libres:'),
    html.Br(),
    html.Br(),
    dbc.Row([
        dbc.Col(''),
        dbc.Col(children=[triqui_layout],
                id="Panel_central"),
        dbc.Col('')
    ]),
    html.Br(),
    html.Br(),
    dbc.Row([
        dbc.Col('Computador en espera', id='comp_status'),
        dbc.Col('', id='casillas'),
        dbc.Col('', id='tablero')
    ]),
    html.Br(),
    dbc.Row(children=[
        dbc.Col(html.A(html.Button('Reiniciar'),href='/')),
        dbc.Col(
            dbc.DropdownMenu(
                label="Seleccione el engine del computador",
                children=[
                    dbc.DropdownMenuItem("DPLL", id="dpll", active=False),
                    dbc.DropdownMenuItem("MinMax", id="minmax", active=True),
                ],
                id="engine"
            )
        ),
        dbc.Col()
    ])
])
