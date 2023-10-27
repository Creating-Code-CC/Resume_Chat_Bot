import load_db as db
import panel as pn
import param

class cbfs(param.Parameterized):
    chat_history = param.List([])

    