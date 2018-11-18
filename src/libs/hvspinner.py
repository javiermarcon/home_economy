# -*- coding: utf-8 -*-

# Downloaded from https://gist.github.com/zeeMonkeez/5d7492479c72e55a6600
# More info in https://stackoverflow.com/questions/36264293/getting-index-of-kivy-spinner

import itertools
from kivy.factory import Factory

from kivy.compat import string_types
from kivy.uix.spinner import Spinner, SpinnerOption
from kivy.properties import ListProperty, ObjectProperty, StringProperty
from kivy.logger import Logger

class HVSpinnerOption(SpinnerOption):
    """Represents an option in HVSpinner. It adds :attr:`value` to represent a hidden value not shown to user."""
    value = ObjectProperty(None)

class HVSpinner(Spinner):
    """Implements a spinner that keeps hidden values associated with
    options and displays a human readable text.
    """

    hidden_values = ListProperty()
    """Values associated with every item generated from :attr:`values`.
    :attr:`hidden_values`: is a :class:`~kivy.properties.ListProperty` and defaults to `range(len(self.values))`.
    The list may contain any kind of object.
    """

    selected_text = StringProperty()
    """Text representation of the selected item. By default, this is `None`. Upon selection of an item,
    it will be the corresponding element of :attr:`values`.
    """

    selected_value = ObjectProperty(None)
    """Representation of the selected item. Defaults to `None`. Upon selection of an item,
    it will be the corresponding element of :attr:`hidden_values`.
    """

    option_cls = ObjectProperty(HVSpinnerOption)
    '''Extension of class to display options. It must conform to requirements laid out for :attr:`~kivy.uix.spinner.option_cls`. In addition, the class must have a `value` property (should be :class:`~kivy.properties.ObjectProperty`).

    Additional :parameter:
    `text_transformer`: `None` or `callable`. Function that is used to set the :attr:`text` of :class:`HVSpinner` once
    an item has been selected. It should return a string and it should take 3 arguments:

    - :attr:`caller`: instance of :class:`HVSpinner` making the call
    - :attr:`text`: same as :attr:`selected_text`
    - :attr:`value`: same as :attr:`selected_value`

    Example::

        from kivy.base import runTouchApp
        from kivy.uix.gridlayout import GridLayout
        from kivy.uix.boxlayout import BoxLayout
        def print_current_val(obj, *largs):
            print("Spinner {} has text [{}], selected_text [{}] and hidden value [{}]".format(obj, obj.text, obj.selected_text, obj.selected_value))

        def transformator(caller, text, value):
            return "Now at >{}< ({})".format(text, value)

        vals = ["item {}".format(i) for i in range(8)]
        hvals  = ["<{}>".format(i + 17) for i in range(len(vals)) ]
        gl = GridLayout(rows=1)

        hvs1 = HVSpinner(values=vals, hidden_values=hvals, text='Select Me',
             size_hint=(.3, None), height="30dp")
        hvs2 = HVSpinner(values=vals, text='No, Me', size_hint=(.3, None), height="40dp")
        hvs3 = HVSpinner(values=vals, hidden_values=range(len(vals)), text='Please, me!', size_hint=(.3, None), height="30dp",
            text_transformer=transformator)
        hvs1.bind(selected_value=print_current_val)
        hvs2.bind(selected_value=print_current_val)
        hvs3.bind(selected_value=print_current_val)
        gl.add_widget(hvs1)
        gl.add_widget(hvs2)
        gl.add_widget(hvs3)
        runTouchApp(gl)

    '''

    def __init__(self, *args, **kwargs):
        self.text_transformer = kwargs.pop('text_transformer', None)
        super(HVSpinner, self).__init__(*args, **kwargs)

    def _update_dropdown(self, *largs):
        dp = self._dropdown
        cls = self.option_cls
        if isinstance(cls, string_types):
            cls = Factory.get(cls)
        dp.clear_widgets()
        if len(self.hidden_values) == 0:
            self.hidden_values = range(len(self.values))
        if len(self.values) != len(self.hidden_values):
            Logger.warning("HVSpinner: 'values' and 'hidden_values' have different lengths.")
        for tv, hv in itertools.izip(self.values, self.hidden_values):
            item = cls(text=tv, value=hv)
            item.bind(on_release=lambda option: dp.select((option.text, option.value)))
            dp.add_widget(item)

    def _on_dropdown_select(self, instance, data, *largs):
        if callable(self.text_transformer):
            self.text = self.text_transformer(self, data[0], data[1])
        else:
            self.text = data[0]
        self.selected_text = data[0]
        self.selected_value = data[1]
        self.is_open = False

    def select_by_id(self, id):
        """Selects an item from a spinner by its id"""
        for tv, hv in itertools.izip(self.values, self.hidden_values):
            if hv == id:
                self._dropdown.select((tv, hv))

Factory.register('HVSpinner', cls=HVSpinner)

if __name__ == '__main__':
    from kivy.base import runTouchApp
    from kivy.uix.gridlayout import GridLayout
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.button import Button
    
    def print_current_val(obj, *largs):
        print("Spinner {} has text [{}], selected_text [{}] and hidden value [{}]".format(obj, obj.text, obj.selected_text, obj.selected_value))

    def transformator(caller, text, value):
        return "Now at >{}< ({})".format(text, value)

    vals = ["item {}".format(i) for i in range(8)]
    hvals  = ["<{}>".format(i + 17) for i in range(len(vals)) ]
    gl = GridLayout(rows=3)

    hvs1 = HVSpinner(values=vals, hidden_values=hvals, text='Select Me',
         size_hint=(.3, None), height="30dp")
    hvs2 = HVSpinner(values=vals, text='No, Me', size_hint=(.3, None), height="40dp")
    hvs3 = HVSpinner(values=vals, hidden_values=range(len(vals)), text='Please, me!', size_hint=(.3, None), height="30dp",
        text_transformer=transformator)
    hvs1.bind(selected_value=print_current_val)
    hvs2.bind(selected_value=print_current_val)
    hvs3.bind(selected_value=print_current_val)
    gl.add_widget(hvs1)
    gl.add_widget(hvs2)
    gl.add_widget(hvs3)
    def change_values(sender):
        hvs3.values = ["new item {}".format(i) for i in range(8)]
    b1 = Button(text='Change values', on_press=change_values)
    gl.add_widget(b1)
    
    runTouchApp(gl)


