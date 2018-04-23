import dash
import dash_core_components as dcc
import dash_html_components as html
import helpers as helper

app = dash.Dash()

id_list = helper.prepare_resources()
all_options = helper.create_all_options(id_list)

vars_data = helper.create_data(all_options, id_list, 'VARS')
cvrg_data = helper.create_data(all_options, id_list, 'CVRG')


app.css.append_css({'external_url': 'https://cdn.rawgit.com/plotly/dash-app-stylesheets/2d266c578d2a6e8850ebce48fdb52759b2aef506/stylesheet-oil-and-gas.css'})

app.layout = html.Div(
    html.Div([
        html.Div(
            [
                html.H1(children='STATS',
                        className='nine columns'),
            ], className="row"
        ),

        html.Div(
            [
                html.Div(
                    [
                        html.P('Choose runs:'),
                        dcc.Dropdown(
                                id ='Runs',
                                options=[{'label': k, 'value': k} for k in all_options],
                                value=all_options,
                                multi=True

                        ),
                    ],
                    className='six columns',
                    style={'margin-top': '10'}
                ),
            ], className="row"
        ),

        html.Div(
            [
                html.Div([
                    dcc.Graph(
                        id='graph'
                    )
                ], className='six columns'
                ),

                html.Div([
                    dcc.Graph(
                        id='graph-2'
                    )
                ], className='six columns'
                )
            ], className="row"
        )
    ], className='ten columns offset-by-one')
)


@app.callback(
    dash.dependencies.Output('Runs', 'options'),
    [dash.dependencies.Input('Runs', 'value')])


@app.callback(
    dash.dependencies.Output('graph', 'figure'),
    [dash.dependencies.Input('Runs', 'value')])
def update_image_src(selector):
    data = []
    for cvrg in selector:
        data.append({'x': cvrg_data[cvrg]['x'], 'y': cvrg_data[cvrg]['y'],
                    'type': 'bar', 'name': cvrg})
    figure = {
        'data': data,
        'layout': {
            'title': 'CVRG Stats',
            'xaxis' : dict(
                title='SAMPLE_ID',
                titlefont=dict(
                family='Helvetica, monospace',
                size=20,
                color='#7f7f7f'
            )),
            'yaxis' : dict(
                title='CVRG',
                titlefont=dict(
                family='Helvetica, monospace',
                size=20,
                color='#7f7f7f'
            ))
        }
    }
    return figure


@app.callback(
    dash.dependencies.Output('graph-2', 'figure'),
    [dash.dependencies.Input('Runs', 'value')])
def update_image_src(selector):
    data = []
    for vars in selector:
        data.append({'x': vars_data[vars]['x'], 'y': vars_data[vars]['y'],
                    'type': 'bar', 'name': vars})
    figure = {
        'data': data,
        'layout': {
            'title': 'VARS Stats',
            'xaxis' : dict(
                title='SAMPLE_ID',
                titlefont=dict(
                family='Helvetica, monospace',
                size=20,
                color='#7f7f7f'
            )),
            'yaxis' : dict(
                title='VARS',
                titlefont=dict(
                family='Helvetica, monospace',
                size=20,
                color='#7f7f7f'
            ))
        }
    }
    return figure


if __name__ == '__main__':
    app.run_server(debug=True)

