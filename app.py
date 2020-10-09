import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_table
import plotly.graph_objects as go 
import dash_daq as daq
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
    
date_format = "%d-%m-%Y"

"""graphs"""
df1 = pd.read_csv('https://raw.githubusercontent.com/uiy123/covData/master/covdata.csv')
df2 = pd.read_csv('https://raw.githubusercontent.com/uiy123/covData/master/rigions.csv')
tda = []
tee = []
tt = []
re = []
de = []
def enc(t, l):
    for i in t:
        if i == 0 or i == '' :
            l.append(None)
        else:
            l.append(i)

enc(df1.date, tda)
enc(df1.total_effected, tee)
enc(df1.recoveries, re)
enc(df1.death, de)
enc(df1.total_tests, tt)
ae = []
for i in df1.active:
    ae.append(i)
maxact = max(ae)
minact = min(ae)
fig= go.Figure()
fig.add_trace(go.Scatter(x= tda, y= ae, name= 'Actives'))
fig.add_trace(go.Scatter(x= tda, y= tee, name= 'Effected'))
fig.add_trace(go.Scatter(x= tda, y= re, name= 'Recoveries'))
fig.add_trace(go.Scatter(x= tda, y= de, name= 'Death'))
fig.add_trace(go.Scatter(x= tda, y= [4000]*len(tda), name= 'Out of control', fill='tozeroy', mode='none', opacity=0.5, line=dict(color='green', width=0.5)))
fig.update_layout({
                    "xaxis_title" :'Date',
                    "uirevision": True,
                    "margin": dict(l=0, r=0, t=4, b=4, pad=0),
                    "hovermode": "x",
                    "font": {"color": "white"},
                    "paper_bgcolor": "rgba(0,0,0,0)",
                    "plot_bgcolor": "rgba(0,0,0,0)",
                    "legend_orientation":"h",
                    "xaxis": dict(
                                showline=False,
                                showgrid=False,
                                zeroline=False,
                                showticklabels=False,)
                })
fig.update_traces(mode="lines")
sos = []
bni = []
dra = []
casa = []
da = []
fas =[]
gl = []
lay = []
mra = []
ori = []
rb = []
tan = []
def data(target, l):
    for i in target:
        l.append(i)
data(df2.BeniMellal_Khénifra, bni)
data(df2.souss_massa, sos)
data(df2.Casa_Settat, casa)
data(df2.Daraa_tafilalet, dra)
data(df2.Dakhla_Oued_EdDahab, da)
data(df2.Fès_meknes, fas)
data(df2.Guelmim_OuedNoun, gl)
data(df2.Laâyoune_Sakia_ElHamra, lay)
data(df2.Marrakech_Safi, mra)
data(df2.Oriental, ori)
data(df2.Rabat_SaléKenitra, rb)
data(df2.TangerTetouan_AlHoceima, tan)

def newCases(l): 
    if l[-1] == l[-2]:
        return f'0 {l.count(l[-1])} days'
    else:
        return f'(+{l[-1]-l[-2]})'
"""def cases(l):
    return f'(+{l[-1]-l[-2]})'"""

#labels1 = [f'BeniMellal_Khénifra {cases(bni)}', f'Casa_Settat {cases(casa)}', f'souss_massa {cases(sos)}', f'TangerTetouan_AlHoceima {cases(tan)}', f'Rabat_SaléKenitra {cases(rb)} ', f'Oriental {cases(ori)}', f'Daraa_tafilalet {cases(dra)}', f'Dakhla_Oued_EdDahab {cases(da)}', f'Fès_meknes {cases(fas)}', f'Guelmim_OuedNoun {cases(gl)}', f'Marrakech_Safi {cases(mra)}', f'Laâyoune_Sakia_ElHamra {cases(lay)}']       
labels = [f'BeniMellal_Khénifra {newCases(bni)}', f'Casa_Settat {newCases(casa)}', f'souss_massa {newCases(sos)}', f'TangerTetouan_AlHoceima {newCases(tan)}', f'Rabat_SaléKenitra {newCases(rb)} ', f'Oriental {newCases(ori)}', f'Daraa_tafilalet {newCases(dra)}', f'Dakhla_Oued_EdDahab {newCases(da)}', f'Fès_meknes {newCases(fas)}', f'Guelmim_OuedNoun {newCases(gl)}', f'Marrakech_Safi {newCases(mra)}', f'Laâyoune_Sakia_ElHamra {newCases(lay)}']       
values = [bni[-1], casa[-1], sos[-1], tan[-1], rb[-1], ori[-1], dra[-1], da[-1], fas[-1], gl[-1], mra[-1], lay[-1] ]
numbers = []
casesInRigions = []
zerocases = []
numdays = []
zcasesInRigion = []
for i, v in enumerate(labels):
    if int((''.join(filter(str.isdigit, v.split(' ')[1]) ))) == 0:
        zerocases.append(labels[i])
    else:
        numbers.append(int(''.join(filter(str.isdigit, v.split(' ')[1]) )))
numbers.sort(reverse=True)
numdays.sort(reverse=True)
for i in zerocases: numdays.append(i.split(' ')[2])
r = 0
while r < len(numdays):
    zcasesInRigion.append(''.join(str(i.split(' ')[0]) for i in zerocases if str(numdays[r]) in i))
    zcasesInRigion.append(''.join(str(i.split(' ')[2]) for i in zerocases if str(numdays[r]) in i))
    r +=1
n = 0
while n < len(numbers):
    casesInRigions.append(''.join(str(i) for i in labels if str(numbers[n])in i))   
    n += 1


fig2 = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='percent+label',insidetextorientation='radial', textposition='inside')])
fig2.update_layout(showlegend=False)
fig2.update_layout({
                    "uirevision": True,
                    "margin": dict(l=0, r=0, t=1, b=1, pad=0),
                    "font": {"color": "white"},
                    "paper_bgcolor": "rgba(0,0,0,0)",
                    "plot_bgcolor": "rgba(0,0,0,0)",
                })
fig3 = go.Figure(data=[go.Pie(labels=[i for i in df1.columns if i[0] == 'a'or i[0] == 'r' or i[0:2]=='de'], values=[ae[-1], re[-1], de[-1]], textinfo='percent+label',insidetextorientation='radial', textposition='inside', hole=.3)])
fig3.update_layout(showlegend=False)
fig3.update_layout({
                    "uirevision": True,
                    "margin": dict(l=0, r=0, t=1, b=1, pad=0),
                    "font": {"color": "white"},
                    "paper_bgcolor": "rgba(0,0,0,0)",
                    "plot_bgcolor": "rgba(0,0,0,0)",
                })

fig4 = go.Figure()
fig4.add_trace(go.Scatter(x= tda, y= ae, name= 'Actives'))
fig4.add_trace(go.Scatter(x= tda, y= [4000]*len(tda), name= 'Out of control', ))
fig4.add_trace(go.Scatter(
    x= [''.join(str(i) for i, e in zip(tda, ae) if e == max(ae))],
    y= [max(ae)],
    mode= 'markers',
    marker=dict(
        color='Red',
        size=20,
    ),
    showlegend=False,
    name='Maximum value'
))
fig4.update_layout({
                    "uirevision": True,
                    "margin": dict(l=0, r=2, t=0, b=0, pad=0),
                    "hovermode": "x",
                    "font": {"color": "white"},
                    "paper_bgcolor": "rgba(0,0,0,0)",
                    "plot_bgcolor": "rgba(0,0,0,0)",
                    "legend_orientation":"h",
                    "xaxis": dict(
                                showline=False,
                                showgrid=False,
                                zeroline=False,
                                showticklabels=False,),
                    
                    
                })
#animation
ys = [tee[0]]
xs = [tda[0]]
text = [tee[0]]
n = 1
f = []
for i in range(len(tee)):
    while n < len(tee):
        xs.append(tda[n])
        ys.append(tee[n])
        text.append(tee[n])
        f.append(go.Frame(data=[go.Scatter(x=xs, y=ys, mode='lines+markers' )])) 
        n += 1

fig5 = go.Figure(
            data=[go.Scatter(x=[tda[0]], y=[tee[0]] )],
            layout=go.Layout(
                xaxis=dict(autorange=False),
                yaxis=dict(range=[0, max(tee)+1], autorange=False),
                title="click",
                updatemenus=[dict(
                    type="buttons",
                    x=0.1,
                    y=1.23,
                    buttons=[dict(label="Play",
                                  method="animate",
                                  args=[None])])]
            ),
            frames=f,
        )
fig5.update_layout(
    xaxis_range=[0, len(tda)],
    paper_bgcolor= 'rgba(0,0,0,0)',
    font={'color':'white'},
    hovermode= 'x',
    plot_bgcolor= 'rgba(0,0,0,0)',
    uirevision= True,
    margin= dict(l=0, r=2, t=0, b=0, pad=0),

)


"""
fig5.update_layout({
                    "uirevision": True,
                    "margin": dict(l=0, r=2, t=0, b=0, pad=0),
                    "hovermode": "x",
                    "font": {"color": "white"},
                    "paper_bgcolor": "rgba(0,0,0,0)",
                    "plot_bgcolor": "rgba(0,0,0,0)",
                    "legend_orientation":"h",
                    "xaxis": dict(
                                showline=False,
                                showgrid=False,
                                zeroline=False,
                                showticklabels=False,),
                    
                    
                })
"""
"""end graphs"""
date_format = "%d-%m-%Y"
a = datetime.strptime(tda[0], date_format)
b = datetime.strptime(tda[-1] , date_format)
delta = b - a

count = (delta.days)+1

app = dash.Dash(meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ])
app.title = 'Covid-19'

#functions
def title(title):
    return html.Div(className="section-banner", children=title)
def value(v, d):
    c = ''
    if int(d) > 0:
        c = 'red'
    elif int(d) <= 0:
        c='green'
    
    return html.P(className='value-holder', children=[html.Div(className='value', children=v),html.Div(className=c, children=d)] )
def recov(v, d):
    c = ''
    if int(d) > 0:
        c = 'green'
    elif int(d) <= 0:
        c='red'
    
    return html.P(className='value-holder', children=[html.Div(className='value', children=v),html.Div(className=c, children=d)] )
    dcc.Graph(
        id='sparkline_graph_id',
        style={"width": "100%", "height": "95%"},
        config={
            "staticPlot": False,
            "editable": False,
            "displayModeBar": False,
        },
        figure=fig,
        
            
            
        
    ),


#banner
banner = html.Div(
        id="banner",
        className="banner",
        children=[
            html.Div(
                id="banner-text",
                children=[
                    html.H5("COVID-19 OVERVIEW"),
                    html.P("Data from official sources"),
                ],
            ),
            html.Div(
                id="banner-logo",
                children=[
                    html.A(
                        id="learn-more-button", children="Collab", href='#'
                    ),
                ],
            ),
        ],
    )


app.layout = html.Div(
    id="big-app-container",
    children=[
        banner,
        html.Div(
            id="app-container",
            children=[
                #cards
                title(f'Overview for today: {tda[-1]} ({count} days)'),
                html.Div(
                    className="row",
                    children=[
                        html.Div(
                            className='three columns flex',
                            children=[
                                title('Total Actives'),
                                value(ae[-1], ae[-1]-ae[-2]),

                            ]
                        ),
                        html.Div(
                            className='three columns',
                            children=[
                                title('Total effected'),
                                value(tee[-1], tee[-1]-tee[-2])
                            ]
                        ),
                        html.Div(
                            className='three columns',
                            children=[
                                title('Total recoveries'),
                                recov(re[-1], re[-1]-re[-2])
                            ]
                        ),
                        html.Div(
                            className='three columns',
                            children=[
                                title('Total death'),
                                value(de[-1], de[-1]-de[-2])
                            ]
                        ),
                    ]
                ),

                html.Div(
                    className="row",
                    children=[
                        #overview garph
                        html.Div(
                            className='twelve columns',
                            children=[
                                
                                dcc.Graph(
                                    id='sparkline_graph_id',
                                    style={"width": "100%", "height": "95%"},
                                    config={
                                        "staticPlot": False,
                                        "editable": False,
                                        "displayModeBar": False,
                                    },
                                    figure=fig,
                                ),
                                

                            ]
                        )
                    ]
                ),
                html.Br(),
                html.Div(
                    className='row',
                    children=[
                        html.Div(
                            className='six columns',
                            children=[
                                title('Rigions'),
                                dcc.Graph(
                                    id='rigions',
                                    style={"width": "100%", "height": "95%"},
                                    config={
                                        "staticPlot": False,
                                        "editable": False,
                                        "displayModeBar": False,
                                    },
                                    figure=fig2,
                                ),
                                title('Quick statsRigions cases:'),
                                html.Table(children=[
                                    html.Tr(children=[
                                        html.Td(children=[
                                            html.P([i.split()[0] for i in casesInRigions][0])
                                        ]),
                                        html.Td(children=[
                                            html.P([i.split()[1] for i in casesInRigions][0])
                                        ]),
                                        
                                    ]),
                                    html.Tr(children=[
                                        html.Td(children=[
                                            html.P([i.split()[0] for i in casesInRigions][1])
                                        ]),
                                        html.Td(children=[
                                            html.P([i.split()[1] for i in casesInRigions][1])
                                        ]),
                                        
                                    ]),
                                    html.Tr(children=[
                                        html.Td(children=[
                                            html.P([i.split()[0] for i in casesInRigions][2])
                                        ]),
                                        html.Td(children=[
                                            html.P([i.split()[1] for i in casesInRigions][2])
                                        ]),
                                        
                                    ]),
                                    html.Tr(children=[
                                        html.Td(children=[
                                            html.P([i.split()[0] for i in casesInRigions][3])
                                        ]),
                                        html.Td(children=[
                                            html.P([i.split()[1] for i in casesInRigions][3])
                                        ]),
                                        
                                    ]),
                                ]),
                                title('Rigions with Zero cases'),
                                
                            ]
                        ),
                        html.Div(
                            className='six columns flex',
                            children=[
                                title('Today'),
                                dcc.Graph(
                                    id='today',
                                    style={"width": "100%", "height": "95%"},
                                    config={
                                        "staticPlot": False,
                                        "editable": False,
                                        "displayModeBar": False,
                                    },
                                    figure=fig3,
                                ),
                                title('Quick stats:'),
                                html.Table(children=[
                                    html.Tr(children=[
                                        html.Td(children=[
                                            html.P('New cases')
                                        ]),
                                        html.Td(children=[
                                            html.P(tee[-1]-tee[-2])
                                        ]),
                                    ]),
                                    html.Tr(children=[
                                        html.Td(children=[
                                            html.P('Actives addes')
                                        ]),
                                        html.Td(children=[
                                            html.P(ae[-1]-ae[-2])
                                        ]),
                                    ]),
                                    html.Tr(children=[
                                        html.Td(children=[
                                            html.P('Recoveries today')
                                        ]),
                                        html.Td(children=[
                                            html.P(re[-1]-re[-2])
                                        ]),
                                    ]),
                                    html.Tr(children=[
                                        html.Td(children=[
                                            html.P('Deaths')
                                        ]),
                                        html.Td(children=[
                                            html.P(de[-1]-de[-2])
                                        ]),
                                    ]),
                                    
                                ])
                            ]
                        ),
                    ]   
                ),
                html.Div(
                    className='row',
                    children=[
                        html.Div(
                            className='twelve columns',
                            children=[
                                dcc.Graph(
                                    id='story',
                                    style={"width": "100%", "height": "95%"},
                                    config={
                                        "staticPlot": False,
                                        "editable": False,
                                        "displayModeBar": False,
                                    },
                                    figure=fig4
                                ),
                                dcc.Graph(
                                    id='story1',
                                    style={"width": "100%", "height": "95%"},
                                    config={
                                        "staticPlot": False,
                                        "editable": False,
                                        "displayModeBar": False,
                                    },
                                    figure=fig5
                                ),
                            
                            ]
                        )
                    ]
                )
            ]
            )
    ],
)
if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=True)
