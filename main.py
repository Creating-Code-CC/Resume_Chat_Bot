from load_db import load_db as load_db
import panel as pn
import param

class cbfs(param.Parameterized):
    chat_history=param.List([])
    answer=param.String("")
    db_query=param.String("")
    db_response=param.List([])
    