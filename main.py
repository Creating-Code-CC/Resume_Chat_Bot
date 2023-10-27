from load_db import load_db as load_db
import panel as pn
import param

class cbfs(param.Parameterized):
    chat_history = param.List([])

    