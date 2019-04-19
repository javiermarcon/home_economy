# -*- coding: utf-8 -*-

"""
These options allow to show a different value than the value to handle
id and text pairs.

This code was a merge from kniteditor’s SettingOptionMapping
(https://github.com/fossasia/kniteditor)
and kivy SettingScrollOptions
(https://github.com/kivy/kivy/wiki/Scollable-Options-in-Settings-panel)
"""

from kivy.properties import DictProperty, ObjectProperty
from kivy.uix.settings import SettingItem
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.togglebutton import ToggleButton
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.settings import SettingSpacer


class SettingOptionMapping(SettingItem):
    '''Implementation of an option list on top of a :class:`SettingItem`.
    It is visualized with a :class:`~kivy.uix.label.Label` widget that, when
    clicked, will open a :class:`~kivy.uix.popup.Popup` with a
    list of options from which the user can select.
    '''

    options = DictProperty({})
    '''A mapping of key strings to value strings.
    The values are displayed to the user.
    The keys can be found in the value attribute.

    :attr:`options` is a :class:`~kivy.properties.DictProperty` and defaults
    to ``{}``.
    '''

    popup = ObjectProperty(None, allownone=True)
    '''(internal) Used to store the current popup when it is shown.

    :attr:`popup` is an :class:`~kivy.properties.ObjectProperty` and defaults
    to None.
    '''

    def on_panel(self, instance, value):
        """The panel is set. Bind to open a popup when it is clicked."""
        if value is None:
            return
        self.fbind('on_release', self._create_popup)


    def _set_option(self, value):
        self.value = value
        self.popup.dismiss()

    def _create_popup(self, instance):
        # create the popup
        content = GridLayout(cols=1, spacing='5dp')
        scrollview = ScrollView(do_scroll_x=False)
        scrollcontent = GridLayout(cols=1, spacing='5dp', size_hint=(None, None))
        scrollcontent.bind(minimum_height=scrollcontent.setter('height'))
        self.popup = popup = Popup(content=content, title=self.title, size_hint=(0.5, 0.9), auto_dismiss=False)

        # we need to open the popup first to get the metrics
        popup.open()
        # Add some space on top
        content.add_widget(Widget(size_hint_y=None, height=dp(2)))
        # add all the options
        uid = str(self.uid)
        for option, text in self.options.items():
            state = 'down' if option == self.value else 'normal'
            btn = ToggleButton(text=text, state=state, group=uid, size=(popup.width, dp(55)), size_hint=(None, None))
            btn.bind(on_release=lambda instance,
                     option=option: self._set_option(option))
            scrollcontent.add_widget(btn)

        # finally, add a cancel button to return on the previous panel
        scrollview.add_widget(scrollcontent)
        content.add_widget(scrollview)
        content.add_widget(SettingSpacer())
        # btn = Button(text='Cancel', size=((oORCA.iAppWidth/2)-sp(25), dp(50)),size_hint=(None, None))
        btn = Button(text='Cancel', size=(popup.width, dp(50)), size_hint=(0.9, None))
        btn.bind(on_release=popup.dismiss)
        content.add_widget(btn)


