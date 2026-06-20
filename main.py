"""
Calculator App - built with Kivy
Supports: + - * / ^ (power) sqrt % parentheses decimals
"""

import math
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

# Safe namespace for eval - only math functions we allow
SAFE_NAMES = {
    "sqrt": math.sqrt,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "log": math.log10,
    "ln": math.log,
    "pi": math.pi,
    "e": math.e,
    "abs": abs,
}


def safe_eval(expression: str):
    """Evaluate a math expression safely (no builtins, only whitelisted names)."""
    # Replace calculator-friendly symbols with Python equivalents
    expr = expression.replace("^", "**")
    expr = expr.replace("√", "sqrt")
    expr = expr.replace("÷", "/")
    expr = expr.replace("×", "*")
    expr = expr.replace("%", "/100")

    try:
        result = eval(expr, {"__builtins__": {}}, SAFE_NAMES)
        return format_result(result)
    except ZeroDivisionError:
        return "Error: Div by 0"
    except Exception:
        return "Error"


def format_result(value):
    if isinstance(value, float):
        if value.is_integer():
            return str(int(value))
        return str(round(value, 10))
    return str(value)


class CalculatorLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=10, spacing=10, **kwargs)

        self.expression = ""

        # Display
        self.display = TextInput(
            text="",
            font_size=40,
            size_hint=(1, 0.25),
            halign="right",
            readonly=False,
            multiline=False,
            background_color=(0.1, 0.1, 0.1, 1),
            foreground_color=(1, 1, 1, 1),
            cursor_color=(1, 1, 1, 1),
        )
        self.add_widget(self.display)

        # Buttons grid
        grid = GridLayout(cols=5, spacing=6, size_hint=(1, 0.75))

        buttons = [
            "C", "(", ")", "⌫", "/",
            "sqrt(", "7", "8", "9", "*",
            "^", "4", "5", "6", "-",
            "%", "1", "2", "3", "+",
            ".", "0", "pi", "=", "ANS",
        ]

        self.last_answer = "0"

        for label in buttons:
            btn = Button(
                text=label,
                font_size=24,
                on_press=self.on_button_press,
            )
            grid.add_widget(btn)

        self.add_widget(grid)

    def on_button_press(self, instance):
        label = instance.text

        if label == "C":
            self.expression = ""
        elif label == "⌫":
            self.expression = self.expression[:-1]
        elif label == "=":
            result = safe_eval(self.expression if self.expression else "0")
            self.last_answer = result
            self.expression = result
        elif label == "ANS":
            self.expression += self.last_answer
        else:
            self.expression += label

        self.display.text = self.expression


class CalculatorApp(App):
    def build(self):
        self.title = "Calculator"
        Window.clearcolor = (0.05, 0.05, 0.05, 1)
        return CalculatorLayout()


if __name__ == "__main__":
    CalculatorApp().run()
