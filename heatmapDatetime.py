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
        colorscale='Picnic',
        colorbar=dict(
            tickmode='array',
            tickvals=[1,2,3,4],
            ticktext=['Correct','Revisit Error','Inbound Error','Outbound Error']
        )
    )
]

layout = go.Layout(
    title='Performance across Trials - Old animals',
    xaxis=dict(
        title='Session'
    )

)

fig = go.Figure(data=oldTrace, layout=layout)
plot_url = py.plot(fig, filename = 'perseverationOld')