from load_db import load_db as load_db
import panel as pn
import param

class cbfs(param.Parameterized):
    chat_history=param.List([])
    answer=param.String("")
    db_query=param.String("")
    db_response=param.List([])
    
    def __init__(self, **params):
        super(cbfs, self).__init__(**params)
        self.panels=[]
        self.loaded_file="file/dir.pdf"
        self.qa=load_db(self.loaded_file,"stuff",4)