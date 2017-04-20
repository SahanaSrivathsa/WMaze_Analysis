"""
creates a population comparison for days
to reach learning criterion.
"""
import plotly.plotly as py
py.sign_in('adelekap','p3GcPtLwHm5jSduhiguJ')
import plotly.graph_objs as go

trial_inbound_old = {10281:345,10282:600,10351:375,10353:189,10354:340}
trial_inbound_young = {10279:212,10280:51,10348:41,10349:268}

session_inbound_old = {10281:8,10282:14,10351:9,10353:9,10354:14}
session_inbound_young = {10279:7,10280:2,10348:2,10349:10}

inboundOldVals = session_inbound_old.values()
inboundYoungVals = session_inbound_young.values()

def Ys(Xs,age):
    if age == 'Young':
        yBase = 0.5
    if age == 'Old':
        yBase = 0.25
    Ys = []
    values = {}
    for x in Xs:
        if x not in values.keys():
            Ys.append(yBase)
            values[x] = 1
        else:
            Ys.append(yBase + 0.05 * values[x])
            values[x] += 1

    return Ys

traceOld = go.Scatter(
    x = inboundOldVals,
    y = Ys(inboundOldVals,'Old'),
    name = 'Old',
    mode = 'markers',
    marker = dict(
            size = 16,
            color = 'rgba(152, 0, 0, .8)',
            line = dict(
                width = 2,
                color = 'rgb(0, 0, 0)'
            ))
)
traceYoung = go.Scatter(
    x = inboundYoungVals,
    y = Ys(inboundYoungVals,'Young'),
    name = 'Young',
    mode = 'markers',
    marker=dict(
        size=16,
        color='rgba(255, 182, 193, .9)',
        line=dict(
        width=2,
        )
    )
)

data = [traceOld,traceYoung]

layout = go.Layout(
    title = 'Inbound',
    xaxis=dict(
            title = 'Days to reach learning criterion',
            range=[1, 15],
            autotick=False,
            dtick=1,
            ticks='outside'
        ),
    yaxis=dict(
        title = 'AGE GROUP',
        range=[0.23,0.6],
        showgrid = False,
        showticklabels=False
    ),
   margin=go.Margin(
    l=50,
    r=50,
    b=100,
    t=100
    ),
    plot_bgcolor='rgb(214, 216, 219)'
)

fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename = 'testInboundPlot')






