'''
'''
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

import pandas as pd


KV = '''
Label:
    text: app.result
    text_size: self.width, None
    halign: 'center'
'''
data = [['a1', 'b1', 'c1'],
        ['a2', 'b2', 'c2'],
        ['a3', 'b3', 'c3']]

df = pd.DataFrame(data)

class Application(App):
    result = StringProperty('')
    def build(self):
        self.result = format(df)
        return Builder.load_string(KV)


if __name__ == "__main__":
    Application().run()
