import plotly.plotly as py
py.sign_in('adelekap','p3GcPtLwHm5jSduhiguJ')
import plotly.graph_objs as go
import perseveration as p

young = p.youngRats
old = p.oldRats


trials = range(1,451)

z = [p.timeseries(rat) for rat in old]

oldTrace = [
    go.Heatmap(
        z=z,
        x=trials,
        y=['animal {0}'.format(rat) for rat in old],
        colorscale='Picnic'
    # colorscale=[['Correct', 'rgb(0,153,0)'], ['Revisit Error', 'rgb(255,204,204)'],
    #             ['Inbound Error', 'rgb(255,102,102)'], ['Outbound Error', 'rgb(204,0,0)']]
    )
]

layout = go.Layout(
    title='Performance across Trials',
    xaxis=dict(
        title='Session'
    )
)

fig = go.Figure(data=oldTrace, layout=layout)
plot_url = py.plot(fig, filename = 'perseverationOld')