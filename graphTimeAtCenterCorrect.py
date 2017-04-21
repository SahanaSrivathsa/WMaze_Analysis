import timeAtCenter as time
import plotly.plotly as py
py.sign_in('adelekap','p3GcPtLwHm5jSduhiguJ')
import plotly.graph_objs as go


youngcorrectTrace = time.createTimeTrace(time.accumulateData(time.youngRats,'c'))
oldcorrectTrace = time.createTimeTrace(time.accumulateData(time.oldRats,'c'))
youngcorrectError = time.errorBars(time.youngRats,'c')
oldcorrectError = time.errorBars(time.oldRats,'c')

youngCorrect = go.Scatter(
    x = range(1,15),
    y = youngcorrectTrace,
    name = 'Young Correct',
    mode = 'lines+markers',
    line = dict(
        color = ('rgba(12,0, 88, .9)'),
        width = 4,),
    # error_y=dict(
    #         type='data',
    #         array=youngcorrectError,
    #         color=('rgba(12, 0, 88, .9)'),
    #         visible=True
    #     )
)

oldCorrect = go.Scatter(
    x = range(1,15),
    y = oldcorrectTrace,
    name = 'Old Correct',
    mode = 'lines+markers',
    line = dict(
        color = ('rgba(12, 0, 88, .8)'),
        width = 4,
        dash='dot'),
    # error_y=dict(
    #         type='data',
    #         array=oldcorrectError,
    #         color=('rgba(12, 0, 88, .8)'),
    #         visible=True
    #     )
)

data =[youngCorrect,oldCorrect]

layout = go.Layout(
    title = 'Average Time Spent at Center Preceding Correct Decision',
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

plot_url = py.plot(fig, filename = 'TimeAtCenterCorrect')