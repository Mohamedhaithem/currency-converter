from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner  # القائمة المنسدلة
import requests

API_KEY = "b578caee327c93545664abfd"  

class CurrencyConverter(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        # إدخال المبلغ
        self.amount_input = TextInput(hint_text="أدخل المبلغ", multiline=False)
        self.add_widget(self.amount_input)

        # قائمة اختيار العملة الأصلية
        self.from_currency = Spinner(
            text="USD",
            values=("USD", "EUR", "DZD", "GBP", "JPY", "SAR")
        )
        self.add_widget(self.from_currency)

        # قائمة اختيار العملة الهدف
        self.to_currency = Spinner(
            text="DZD",
            values=("USD", "EUR", "DZD", "GBP", "JPY", "SAR")
        )
        self.add_widget(self.to_currency)

        # زر التحويل
        self.convert_button = Button(text="حوّل", on_press=self.convert_currency)
        self.add_widget(self.convert_button)

        # عرض النتيجة
        self.result_label = Label(text="النتيجة ستظهر هنا")
        self.add_widget(self.result_label)

    def convert_currency(self, instance):
        try:
            amount = float(self.amount_input.text)
            from_curr = self.from_currency.text
            to_curr = self.to_currency.text

            url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_curr}"
            response = requests.get(url).json()
            rate = response["conversion_rates"][to_curr]
            result = amount * rate

            self.result_label.text = f"{amount} {from_curr} = {result:.2f} {to_curr}"
        except Exception as e:
            self.result_label.text = f"خطأ: {e}"

class MyApp(App):
    def build(self):
        return CurrencyConverter()

if __name__ == "__main__":
    MyApp().run()
