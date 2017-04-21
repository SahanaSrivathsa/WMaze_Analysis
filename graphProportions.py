
import plotly.plotly as py
py.sign_in('adelekap','p3GcPtLwHm5jSduhiguJ')
import plotly.graph_objs as go
import ProportionCorrect as p


youngInboundErrorTrace = p.createProportionTrace(p.accumulateData(p.youngRats))
oldInboundErrorTrace = p.createProportionTrace(p.accumulateData(p.oldRats))
youngOutboundErrorTrace = p.createProportionTrace(p.accumulateData(p.youngRats))
oldOutboundErrorTrace = p.createProportionTrace(p.accumulateData(p.oldRats))

youngInTrace = go.Scatter(
    x = range(1,15),
    y = youngInboundErrorTrace,
    name = 'Young % Inbound Errors',
    mode = 'lines',
    line = dict(
        color = ('rgba(255, 182, 193, .9)'),
        width = 4,)
)

youngOutTrace = go.Scatter(
    x = range(1,15),
    y = youngOutboundErrorTrace,
    name = 'Young % Outbound Errors',
    mode = 'lines',
    line = dict(
        color = ('rgba(255, 182, 193, .9)'),
        width = 4,
        dash = 'dot')
)

oldInTrace = go.Scatter(
    x = range(1,15),
    y = oldInboundErrorTrace,
    name = 'Old % Inbound Errors',
    mode = 'lines',
    line = dict(
        color = ('rgba(152, 0, 0, .8)'),
        width = 4,)
)

oldOutTrace = go.Scatter(
    x = range(1,15),
    y = oldOutboundErrorTrace,
    name = 'Old % Outbound Errors',
    mode = 'lines',
    line = dict(
        color = ('rgba(152, 0, 0, .8)'),
        width = 4,
        dash = 'dot')
)

data = [youngInTrace,youngOutTrace,oldInTrace,oldOutTrace]

layout = go.Layout(
    title = 'Error Types Made Across Sessions',
    xaxis=dict(
            title = 'Session',
            range=[1, 14],
            autotick=False,
            dtick=1,
            ticks='outside'
        ),
    yaxis=dict(
        title = 'Percent of Total Errors',
        range=[0,1],
    )
)

fig = go.Figure(data=data, layout=layout)

plot_url = py.plot(fig, filename = 'Errors')


