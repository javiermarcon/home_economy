# -*- coding: utf-8 -*-

from kivy.factory import Factory
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.properties import StringProperty

class ConfirmPopup(GridLayout):
    text = StringProperty()

    def __init__(self, **kwargs):
        self.register_event_type('on_answer')
        super(ConfirmPopup, self).__init__(**kwargs)

    def on_answer(self, *args):
        pass


class PopupBox(Popup):
    pop_up_text = ObjectProperty()
    def update_pop_up_text(self, p_message):
        self.pop_up_text.text = p_message


class PopupActions():
    # response of a popup
    confirm_popup_actions = None

    def open_confirm_popup(self, message, title='Confirmar', action_yes=None,
                   action_no=None, size=(480, 400), size_hint=(None, None)):
        self.confirm_popup_actions = {'action_yes': action_yes,
                              'action_no': action_no}
        content = ConfirmPopup(text=message)
        content.bind(on_answer=self._on_popup_answer)
        self.confirm_popup = Popup(title=title,
                           content=content,
                           size_hint=size_hint,
                           size=size,
                           auto_dismiss=False)
        self.confirm_popup.open()

    def show_popup(self, message='...'):
        self.pop_up = Factory.PopupBox()
        self.pop_up.update_pop_up_text(message)
        self.pop_up.open()

    def close_popup(self):
        self.pop_up.dismiss()

    def _on_popup_answer(self, instance, answer):
        self.confirm_popup.dismiss()
        if answer:
            self.confirm_popup_actions['action_yes']()
        else:
            self.confirm_popup_actions['action_no']()