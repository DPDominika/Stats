import dash
import dash_core_components as dcc
import dash_html_components as html
import helpers as helper

app = dash.Dash()

all_options = ['RUN_ID1', 'RUN_ID2', 'RUN_ID3']


vars_data = {
    'RUN_ID1': {'x': helper.extract('stats/single_run_stats/180317.tsv', 'SAMPLE'), 'y': helper.extract('stats/single_run_stats/180317.tsv', 'VARS')},
    'RUN_ID2': {'x': helper.extract('stats/single_run_stats/180319.tsv', 'SAMPLE'), 'y': helper.extract('stats/single_run_stats/180319.tsv', 'VARS')},
    'RUN_ID3': {'x': helper.extract('stats/single_run_stats/180331.tsv', 'SAMPLE'), 'y': helper.extract('stats/single_run_stats/180331.tsv', 'VARS')},
}

cvrg_data = {
    'RUN_ID1': {'x': helper.extract('stats/single_run_stats/180317.tsv', 'SAMPLE'), 'y': helper.extract('stats/single_run_stats/180317.tsv', 'CVRG')},
    'RUN_ID2': {'x': helper.extract('stats/single_run_stats/180319.tsv', 'SAMPLE'), 'y': helper.extract('stats/single_run_stats/180319.tsv', 'CVRG')},
    'RUN_ID3': {'x': helper.extract('stats/single_run_stats/180331.tsv', 'SAMPLE'), 'y': helper.extract('stats/single_run_stats/180331.tsv', 'CVRG')},
}


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
                        dcc.Checklist(
                                id ='Runs',
                                options=[{'label': k, 'value': k} for k in all_options],
                                values=all_options,
                                labelStyle={'display': 'inline-block'}
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
    [dash.dependencies.Input('Runs', 'values')])
def set_cities_options(selected_country):
    return [{'label': i, 'value': i} for i in all_options[selected_country]]


@app.callback(
    dash.dependencies.Output('graph', 'figure'),
    [dash.dependencies.Input('Runs', 'values')])
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
    [dash.dependencies.Input('Runs', 'values')])
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

