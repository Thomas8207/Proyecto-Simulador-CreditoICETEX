import sys
import os

# Agrega la carpeta 'src' al path para poder importar 'model.logica_credito'
# sin importar desde dónde se ejecute este archivo.
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from model import logica_credito


class CreditoICETEXApp(App):

    def build(self):
        self.title = 'Simulador de Credito Educativo'
        contenedor = GridLayout(rows=5, cols=2, padding=20, spacing=10)

        contenedor.add_widget(Label(text='Monto del credito'))
        self.monto_credito = TextInput()
        contenedor.add_widget(self.monto_credito)

        contenedor.add_widget(Label(text='Tasa de interes mensual (%)'))
        self.tasa_interes = TextInput()
        contenedor.add_widget(self.tasa_interes)

        contenedor.add_widget(Label(text='Numero de cuotas'))
        self.cantidad_cuotas = TextInput()
        contenedor.add_widget(self.cantidad_cuotas)

        boton_calcular = Button(text='Calcular')
        boton_calcular.bind(on_press=self.calcular)
        contenedor.add_widget(boton_calcular)

        self.resultado = Label(text='Aqui apareceran los resultados')
        contenedor.add_widget(self.resultado)

        return contenedor

    def calcular(self, sender):
        try:
            monto_credito = float(self.monto_credito.text)
            tasa_interes_mensual = float(self.tasa_interes.text) / 100
            cantidad_cuotas = int(self.cantidad_cuotas.text)

            cuota = round(logica_credito.calcular_cuota(monto_credito, tasa_interes_mensual, cantidad_cuotas), 2)
            total_pagado = round(logica_credito.calcular_total_pagado(monto_credito, tasa_interes_mensual, cantidad_cuotas), 2)
            total_intereses = round(logica_credito.calcular_total_intereses(monto_credito, tasa_interes_mensual, cantidad_cuotas), 2)

            self.resultado.text = (
                f'Cuota mensual: {cuota}\n'
                f'Total pagado: {total_pagado}\n'
                f'Total intereses: {total_intereses}'
            )
        except ValueError:
            self.resultado.text = 'Ingrese solo valores numericos validos'
        except Exception as err:
            self.resultado.text = str(err)


if __name__ == '__main__':
    CreditoICETEXApp().run()