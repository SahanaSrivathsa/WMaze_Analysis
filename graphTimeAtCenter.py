import timeAtCenter as time

youngcorrectTrace = time.createTimeTrace(time.accumulateData(time.youngRats,'c'))
oldcorrectTrace = time.createTimeTrace(time.accumulateDate(time.oldRats,'c'))
youngcorrectError = time.errorBars(time.youngRats,'c')
oldcorrectError = time.errorBars(time.oldRats,'c')

youngincorrectTrace = time.createTimeTrace(time.accumulateData(time.youngRats,'i'))
oldincorrectTrace = time.createTimeTrace(time.accumulateData(time.oldRats,'i'))
youngincorrectError = time.errorBars(time.youngRats,'i')
oldincorrectError = time.errorBars(time.oldRats,'i')


youngTrace = go.Scatter(
    x = range(1,15),
    y = youngTimeTrace,
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
    y = oldTimeTrace,
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