import plotly.graph_objects as go

title = '2020/W9: Sleep Hours Needed and Averaged'
xLabel = 'Grades'
yLabel = 'Sleep Hours'


grade = ['Kindergarten','First grade','Second grade','Third grade','Fourth grade','Fifth grade','Sixth grade','Seventh grade','Eighth grade','Ninth grade','10th grade','11th grade','12th grade']
hours_needed = [9.5,9.1,9.3,8.6,8.9,8.9,8.6,8.5,8.5,8.3,8.4,8.4,8.0]
hours_averaged =[8.5,8.4,8.3,8.1,7.9,7.8,7.6,7.3,7.4,7.1,6.8,6.9,6.6]

fig = go.Figure(data=[
    go.Bar(name='Hours Needed', x=grade, y=hours_needed),
    go.Bar(name='Hours Averaged', x=grade, y=hours_averaged)
])
# Change the bar mode
fig.update_layout(barmode='overlay',title=title,
    xaxis_title=xLabel,
    yaxis_title=yLabel,)
fig.show()



# fig.update_layout(title=title,
#                 xaxis_title="Grades",
#                 yaxis_title="Hours")




# data = [
#     go.Bar(x=x, y=need, name='Hours Needed'),
#     # go.Bar(x=x, y=avg, name='Hours Averaged')
#     ]

# layout = go.Layout(
#     barmode='overlay',
# )

# fig = dict(data = data, layout = layout)
# pio.show(fig)

