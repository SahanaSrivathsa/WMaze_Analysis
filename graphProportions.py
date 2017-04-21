
import plotly.plotly as py
py.sign_in('adelekap','p3GcPtLwHm5jSduhiguJ')
import plotly.graph_objs as go
import ProportionCorrect as p


youngErrorTrace = p.createProportionTrace(p.accumulateData(p.youngRats))
oldErrorTrace = p.createProportionTrace(p.accumulateData(p.oldRats))

youngError = p.errorBars(p.youngRats)
oldError = p.errorBars(p.oldRats)


youngTrace = go.Scatter(
    x = range(1,15),
    y = youngErrorTrace,
    name = 'Young',
    mode = 'lines+markers',
    line = dict(
        color = ('rgba(255, 182, 193, .9)'),
        width = 4,),
    error_y=dict(
            type='data',
            array=youngError,
            color=('rgba(255, 182, 193, .9)'),
            visible=True
        )
)

oldTrace = go.Scatter(
    x = range(1,15),
    y = oldErrorTrace,
    name = 'Old',
    mode = 'lines+markers',
    line = dict(
        color = ('rgba(152, 0, 0, .8)'),
        width = 4,),
    error_y=dict(
            type='data',
            array=oldError,
            color=('rgba(152, 0, 0, .8)'),
            visible=True
        )
)


data = [youngTrace,oldTrace]

layout = go.Layout(
    title = 'Alternation Task Performance',
    xaxis=dict(
            title = 'Exposure',
            range=[1, 14],
            autotick=False,
            dtick=1,
            ticks='outside'
        ),
    yaxis=dict(
        title = 'Proportion Correct',
        range=[0,1],
    )
)

fig = go.Figure(data=data, layout=layout)

plot_url = py.plot(fig, filename = 'Proportion Correct')


