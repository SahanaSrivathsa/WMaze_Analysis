import timeAtCenter as time
import plotly.plotly as py
py.sign_in('adelekap','p3GcPtLwHm5jSduhiguJ')
import plotly.graph_objs as go

oldcorrectTrace = time.createTimeTrace(time.accumulateData(time.oldRats,'c'))
oldcorrectError = time.errorBars(time.oldRats,'c')
oldincorrectTrace = time.createTimeTrace(time.accumulateData(time.oldRats,'i'))
oldincorrectError = time.errorBars(time.oldRats,'i')


oldCorrect = go.Scatter(
    x = range(1,15),
    y = oldcorrectTrace,
    name = 'Old Correct',
    mode = 'lines+markers',
    line = dict(
        color = ('rgba(12,0, 88, .9)'),
        width = 4,
        dash='dot'),
    # error_y=dict(
    #         type='data',
    #         array=youngcorrectError,
    #         color=('rgba(12, 0, 88, .9)'),
    #         visible=True
    #     )
)

oldIncorrect = go.Scatter(
    x = range(1,15),
    y = oldincorrectTrace,
    name = 'Old Incorrect',
    mode = 'lines+markers',
    line = dict(
        color = ('rgba(217, 0, 0, .9)'),
        width = 4,
        dash='dot'),
    # error_y=dict(
    #         type='data',
    #         array=youngincorrectError,
    #         color=('rgba(217, 0, 0, .9)'),
    #         visible=True
    #     )
)

data =[oldCorrect,oldIncorrect]

layout = go.Layout(
    title = 'Average Time Spent at Center Preceding Decision',
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

plot_url = py.plot(fig, filename = 'TimeAtCenterOLD')