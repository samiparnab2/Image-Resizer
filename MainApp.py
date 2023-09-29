from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from plyer import filechooser




import cv2
import numpy as np
import math
import matplotlib.pyplot as plt 


import os
import logging


class MainApp(App):

    img_file_name : str= ''
    img_file_path : str = ''
    img_file_unit : list = ['B' , 'KB' , 'MB']
    img = None

    def open_image(self , path):
        self.img = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)

    def choose_image(self):
        self.img_file_path = filechooser.open_file(multiple=False, filters = ["*.jpeg", "*.jpg" , "*.png"])[0]
        print(self.img_file_path)


    def load_image(self , *args):
        self.choose_image()
        self.img_file_name = os.path.basename(self.img_file_path)
        print(self.img_file_name)
        self.open_image(self.img_file_path)

    def build(self):
        
        #declaring layouts---------------------------------------------------------------------------------
        main_layout = BoxLayout(orientation="vertical")
        top_layout = BoxLayout(orientation = 'horizontal' , size_hint = (1 , .9))
        bottom_layout = BoxLayout(orientation = 'horizontal' ,size_hint = (1, .1))
        left_layout = BoxLayout(orientation = 'vertical', size_hint = (.7, 1))
        right_layout = BoxLayout(orientation = 'vertical' , size_hint = (.3 , 1))
        #--------------------------------------------------------------------------------------------------
        # top layout
        #right layout widgets-------------------------------------------------------------------------------

        #minimm resolution 
        min_resolutiuon_label = Label(text = "Minimum Resolution")
        right_layout.add_widget(min_resolutiuon_label)
        temp_layout = BoxLayout(orientation="horizontal")
        min_width_text = TextInput(text = '200')
        min_height_text = TextInput(text = '500')
        temp_layout.add_widget(Label(text = 'Width'))
        temp_layout.add_widget(min_width_text)
        temp_layout.add_widget(Label(text = 'Length'))
        temp_layout.add_widget(min_height_text)
        right_layout.add_widget(temp_layout)


        #maximum resolution 
        max_resolutiuon_text = Label(text = "Maximum Resolution")
        right_layout.add_widget(max_resolutiuon_text)
        temp_layout = BoxLayout(orientation="horizontal")
        max_width_text = TextInput(text = '200')
        max_height_text = TextInput(text = '500')
        temp_layout.add_widget(Label(text = 'Width'))
        temp_layout.add_widget(max_width_text)
        temp_layout.add_widget(Label(text = 'Length'))
        temp_layout.add_widget(max_height_text)
        right_layout.add_widget(temp_layout)


        #min aspect ration 
        min_aspect_ratio_text = Label(text = "Minimum Aspect Ratio")
        right_layout.add_widget(min_aspect_ratio_text)
        temp_layout = BoxLayout(orientation="horizontal")
        min_ar = TextInput(text = '0.45')
        temp_layout.add_widget(min_ar)
        right_layout.add_widget(temp_layout)


        #max aspect ration 
        max_aspect_ratio_text = Label(text = "Maximum Aspect Ratio")
        right_layout.add_widget(max_aspect_ratio_text)
        temp_layout = BoxLayout(orientation="horizontal")
        max_ar = TextInput(text = '0.67')
        temp_layout.add_widget(max_ar)
        right_layout.add_widget(temp_layout)


        #min file size 
        min_file_size_text = Label(text = "Minimum File Size")
        right_layout.add_widget(min_file_size_text)
        temp_layout = BoxLayout(orientation="horizontal")
        min_fsize_text = TextInput(text = '5')
        min_fsize_unit_dropdown = DropDown()
        for unit in self.img_file_unit:
            btn = Button(text=unit , size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: min_fsize_unit_dropdown.select(btn.text))
            min_fsize_unit_dropdown.add_widget(btn)
        
        min_fsize_unit_dropdown_button = Button(text ='KB')
        min_fsize_unit_dropdown_button.bind(on_release = min_fsize_unit_dropdown.open)
        min_fsize_unit_dropdown.bind(on_select = lambda instance, x: setattr(min_fsize_unit_dropdown_button, 'text', x))


        temp_layout.add_widget(min_fsize_text)
        temp_layout.add_widget(min_fsize_unit_dropdown_button)
        right_layout.add_widget(temp_layout)

        #max file size 
        max_file_size_text = Label(text = "Maximum File Size")
        right_layout.add_widget(max_file_size_text)
        temp_layout = BoxLayout(orientation="horizontal")
        max_fsize_text = TextInput(text = '5')

        max_fsize_unit_dropdown = DropDown()
        for unit in self.img_file_unit:
            btn = Button(text=unit , size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: max_fsize_unit_dropdown.select(btn.text))
            max_fsize_unit_dropdown.add_widget(btn)
        
        max_fsize_unit_dropdown_button = Button(text ='KB')
        max_fsize_unit_dropdown_button.bind(on_release = max_fsize_unit_dropdown.open)
        max_fsize_unit_dropdown.bind(on_select = lambda instance, x: setattr(max_fsize_unit_dropdown_button, 'text', x))

     
        temp_layout.add_widget(max_fsize_text)
        temp_layout.add_widget(max_fsize_unit_dropdown_button)
        right_layout.add_widget(temp_layout)


        #left layout widgets---------------------------------------------------------------------------------

        # #image box
        img_open_button = Button(text = 'Open Image' , size_hint = (1,1))
        img_open_button.bind(on_release = self.load_image)
        image_box = Image(source = self.img_file_path , size_hint = (1 , .8))
        image_box.add_widget(img_open_button)
        left_layout.add_widget(image_box)

        
        #main layout widgets---------------------------------------------------------------------------------
        top_layout.add_widget(left_layout)
        top_layout.add_widget(right_layout)

        output_path_text = TextInput(text=self.img_file_name, multiline=False , size_hint = (.7 , 1))
        save_button = Button(text = "Save" , size_hint = (.3 , 1))
        bottom_layout.add_widget(output_path_text)
        bottom_layout.add_widget(save_button)

        main_layout.add_widget(top_layout)
        main_layout.add_widget(bottom_layout)
        # ---------------------------------------------------------------------------------------------------
        return main_layout
	
    # def on_button_press(self, instance):
    #     current = self.solution.text
    #     button_text = instance.text

    #     if button_text == "C":
    #         # Clear the solution widget
    #         self.solution.text = ""
    #     else:
    #         if current and (
    #             self.last_was_operator and button_text in self.operators):
    #             # Don't add two operators right after each other
    #             return
    #         elif current == "" and button_text in self.operators:
    #             # First character cannot be an operator
    #             return
    #         else:
    #             new_text = current + button_text
    #             self.solution.text = new_text
    #     self.last_button = button_text
    #     self.last_was_operator = self.last_button in self.operators
		
    # def on_solution(self, instance):
    #     text = self.solution.text
    #     if text:
    #         solution = str(eval(self.solution.text))
    #         self.solution.text = solution

if __name__ == '__main__':
    app = MainApp()
    app.run()