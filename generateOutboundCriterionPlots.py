"""
creates a population comparison for days
to reach learning criterion.
"""
import plotly.plotly as py
py.sign_in('adelekap','p3GcPtLwHm5jSduhiguJ')
import plotly.graph_objs as go
from plotly import tools


trial_outbound_old = {10282:358,10351:260}
trial_outbound_young = {10279:23,10280:38,10348:299,10349:355}

session_outbound_old = {10281:-1,10282:10,10351:9,10353:-1,10354:-1}
session_outbound_young = {10279:2,10280:2,10348:9,10349:12}
session_outbound_non = {10281:'Did not reach criterion',10353:'Did not reach criterion',10354:'Did not reach criterion'}

outboundOldVals = session_outbound_old.values()
outboundYoungVals = session_outbound_young.values()
outboundNonVals = session_outbound_non.values()
#
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
#
# traceOld = go.Scatter(
#     x = outboundOldVals,
#     y = Ys(outboundOldVals,'Old'),
#     name = 'Old Learners',
#     mode = 'markers',
#     marker = dict(
#             size = 16,
#             color = 'rgba(152, 0, 0, .8)',
#             line = dict(
#                 width = 2,
#                 color = 'rgb(0, 0, 0)'
#             ))
# )
# traceYoung = go.Scatter(
#     x = outboundYoungVals,
#     y = Ys(outboundYoungVals,'Young'),
#     name = 'Young',
#     mode = 'markers',
#     marker=dict(
#         size=16,
#         color='rgba(255, 182, 193, .9)',
#         line=dict(
#         width=2,
#         )
#     )
# )
# traceNonLearners = go.Scatter(
#     x = outboundNonVals,
#     y = Ys(outboundNonVals,'Old'),
#     name = 'Old Non-learners',
#     mode = 'markers',
#     marker = dict(
#             size = 16,
#             color = 'rgba(90, 0, 0, .8)',
#             line = dict(
#                 width = 2,
#                 color = 'rgb(0, 0, 0)'
#             ))
# )
#
# data = [traceOld,traceYoung,traceNonLearners]
#
#
# layout = go.Layout(
#     title = 'Outbound',
#     xaxis=dict(
#             title = 'Days to reach learning criterion',
#             range=[1, 15],
#             autotick=False,
#             dtick=1,
#             ticks='outside'
#         ),
#     yaxis=dict(
#         title = 'AGE GROUP',
#         range=[0.23,0.6],
#         showgrid = False,
#         showticklabels=False
#     ),
#    margin=go.Margin(
#     l=50,
#     r=50,
#     b=100,
#     t=100
#     ),
#     plot_bgcolor='rgb(214, 216, 219)'
# )
#
# fig = go.Figure(data=data, layout=layout)
# plot_url = py.plot(fig, filename = 'testOutboundPlot')


traceOldLearners = go.Scatter(
    x=outboundOldVals,
    y=Ys(outboundOldVals,'Old'),
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
    x=outboundYoungVals,
    y=Ys(outboundYoungVals,'Young'),
    name = 'Young',
    mode = 'markers',
    marker=dict(
        size=16,
        color='rgba(255, 182, 193, .9)',
        line=dict(
        width=2,
        ))
)
traceOldNonLearners = go.Scatter(
    x=outboundNonVals,
    y=Ys(outboundNonVals,'Old'),
    name = 'Old',
    mode = 'markers',
    marker = dict(
            size = 16,
            color = 'rgba(152, 0, 0, .8)',
            line = dict(
                width = 2,
                color = 'rgb(0, 0, 0)'
            )),
    showlegend = False
)

fig = tools.make_subplots(rows=1, cols=2,shared_yaxes=True,horizontal_spacing=0.001)

fig.append_trace(traceOldLearners, 1, 1)
fig.append_trace(traceYoung, 1, 1)
fig.append_trace(traceOldNonLearners, 1, 2)


fig['layout'].update(title='Outbound',
    plot_bgcolor='rgb(214, 216, 219)')
fig['layout']['xaxis1'].update(title='Days to reach learning criterion', range =[1,14],autotick=False,
            dtick=1,
            ticks='outside')
fig['layout']['yaxis1'].update(title = 'AGE GROUP',
        range=[0.23,0.6],
        showgrid = False,
        showticklabels=False)
plot_url = py.plot(fig, filename = 'testOutboundPlot')



