from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

def create_context_menu(instance, color_scheme):
    """Create a right-click context menu for the URL input field."""
    menu = Popup(size_hint=(0.3, 0.2), background_color=color_scheme["background"])

    # Create buttons for Copy, Paste, and Cut
    content = BoxLayout(orientation="vertical", spacing=5)
    copy_button = Button(text="Copy", size_hint_y=None, height=40, background_color=color_scheme["button"])
    paste_button = Button(text="Paste", size_hint_y=None, height=40, background_color=color_scheme["button"])
    cut_button = Button(text="Cut", size_hint_y=None, height=40, background_color=color_scheme["button"])

    # Bind buttons to their respective actions
    copy_button.bind(on_press=lambda x: instance.copy())
    paste_button.bind(on_press=lambda x: instance.paste())
    cut_button.bind(on_press=lambda x: instance.cut())

    # Add buttons to the menu
    content.add_widget(copy_button)
    content.add_widget(paste_button)
    content.add_widget(cut_button)
    menu.content = content

    # Open the menu
    menu.open()