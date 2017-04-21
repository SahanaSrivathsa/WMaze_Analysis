import timeAtCenter as time
import plotly.plotly as py
py.sign_in('adelekap','p3GcPtLwHm5jSduhiguJ')
import plotly.graph_objs as go

youngincorrectTrace = time.createTimeTrace(time.accumulateData(time.youngRats,'i'))
oldincorrectTrace = time.createTimeTrace(time.accumulateData(time.oldRats,'i'))
youngincorrectError = time.errorBars(time.youngRats,'i')
oldincorrectError = time.errorBars(time.oldRats,'i')



youngIncorrect = go.Scatter(
    x = range(1,15),
    y = youngincorrectTrace,
    name = 'Young Incorrect',
    mode = 'lines+markers',
    line = dict(
        color = ('rgba(217, 0, 0, .9)'),
        width = 4),
    # error_y=dict(
    #         type='data',
    #         array=youngincorrectError,
    #         color=('rgba(217, 0, 0, .9)'),
    #         visible=True
    #     )
)

oldIncorrect = go.Scatter(
    x = range(1,15),
    y = oldincorrectTrace,
    name = 'Old Incorrect',
    mode = 'lines+markers',
    line = dict(
        color = ('rgba(217, 0, 0, .8)'),
        width = 4,
        dash='dot'),
    # error_y=dict(
    #         type='data',
    #         array=oldincorrectError,
    #         color=('rgba(217, 0, 0, .8)'),
    #         visible=True
    #     )
)

data = [youngIncorrect,oldIncorrect]

layout = go.Layout(
    title = 'Average Time Spent at Center Preceding Incorrect Decision',
    xaxis=dict(
            title = 'Session',
            range=[1, 14],
            autotick=False,
            dtick=1,
            ticks='outside'
        ),
    yaxis=dict(
        title = 'Time Spent at Center Feeder (sec)'
    )
)

fig = go.Figure(data=data, layout=layout)

plot_url = py.plot(fig, filename = 'TimeAtCenterIncorrect')