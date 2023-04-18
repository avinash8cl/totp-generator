import pyotp
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock

class TOTPApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.secret_key_input = TextInput(hint_text='Enter secret key')
        self.generate_button = Button(text='Generate TOTP')
        self.generate_button.bind(on_press=self.generate_totp)
        self.totp_label = Label(text='')
        self.layout.add_widget(self.secret_key_input)
        self.layout.add_widget(self.generate_button)
        self.layout.add_widget(self.totp_label)
        return self.layout

    def generate_totp(self, instance):
        secret_key = self.secret_key_input.text
        totp = pyotp.TOTP(secret_key)
        totp_pin = str(totp.now())
        self.totp_label.text = 'TOTP is: ' + totp_pin

if __name__ == '__main__':
    TOTPApp().run()
