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
    def call_load_db(self, count):
        if count==0 or file_input.value is None:#init or no file specified
            return pn.pane.Markdown(f"Loaded File: {self.loaded_file}")
        else:
            file_input.save("temp.pdf") #local copy
            self.loaded_file=file_input.file_name
            button_load.button_style="outline"
            self.qa=load_db("temp.pdf", "stuff", 4)
            button_load.button_style="solid"
            
        self.clr_history()

        return pn.pane.Markdown(f"Loaded File: {self.loaded_file}")
    
