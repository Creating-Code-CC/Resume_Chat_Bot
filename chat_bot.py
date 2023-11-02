"""""openai"""
import sys
import panel as pn
from cbfs import cbfs
pn.extension()
cb = cbfs()

file_input=pn.widgets.FileInput(accept='.pdf')
button_load=pn.widgets.Button(name="Load DB", button_type='primary')
button_clearhistory=pn.widgets.Button(name="Clear History", button_type='warning')
button_clearhistory.on_click(cb.clr_history)
inp=pn.widgets.TextInput(placeholder='Enter text here...')

bound_button_load=pn.bind(cb.call_load_db, button_load.param.clicks)
conversation=pn.bind(cb.convchain,inp)

png_pane=pn.pane.Image( './img/social_media_github.png')

tab1=pn.Column(
    pn.Row(inp),
    pn.layout.Divider(),
    pn.panel(conversation, loading_indicator=True,height=300),
    pn.layout.Divider(),
)
tab2=pn.Column(
    pn.panel(cb.get_lquest),
    pn.layout.Divider(),
    pn.panel(cb.get_sources),
)
tab3=pn.Column(
    pn.panel(cb.get_chats),
    pn.layout.Divider(),
)
tab4=pn.Column(
    pn.Row(file_input, button_load, bound_button_load),
    pn.Row(button_clearhistory, pn.pane.Markdown("Clears chat history. Can use to start a new topic")),
    pn.layout.Divider(),
    pn.Row(png_pane.clone(width=400))
)
dashboard=pn.Column(
    pn.Row(pn.pane.Markdown('# SmittyChatBot_IYAOYAS')),
    pn.Tabs(('Conversation', tab1), ('Database', tab2), ('Chat History', tab3), ('Configure', tab4))
)


if __name__.startswith('bokeh'):
    dashboard.servable()
else:
    dashboard.show()
    # dashboard.save('dashboard.html', embed=True)
    # pn.serve(dashboard, port=5006, show=True, websocket_origin='localhost:5006')
    # bokeh serve --show

# EOF