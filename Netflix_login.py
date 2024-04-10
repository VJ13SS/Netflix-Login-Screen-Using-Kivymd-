#All the adjustments made here are for my mobile since the code is made on my mobile.
#Adjust it as per your screen 


from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.uix.image import Image
from kivy.lang import Builder
from kivymd.uix.label import MDLabel,MDIcon
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFlatButton,MDIconButton
from kivymd.uix.selectioncontrol import MDCheckbox
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView

class MYApp(MDApp):
	
	def build(self):
		
		#Setting Theme
		
		self.theme_cls.theme_style = 'Dark'
		self.theme_cls.primary_hue = '50'
		
		self.screen = Screen()
		
		#Adding Image (Ensure that The image and your code are in the same directory)
		self.screen.add_widget(Image(source = 'Netflix logo.jpg',pos_hint = {'center_x' : 0.3,'center_y':0.9}))
		
		
		#Labels
		self.label1 = MDLabel(text = 'Sign In',bold = True,pos_hint = {'center_x' : 0.27,'center_y': 0.78},halign = 'center',theme_text_color = 'Primary',font_style = 'H3',size_hint_y = None)
		
		self.label2 = MDLabel(text = 'OR',bold = False,pos_hint = {'center_x' : 0.5,'center_y': 0.38},halign = 'center',theme_text_color = 'Secondary',size_hint_y = None)
		self.label3 = MDLabel(text = 'Forgot password?',pos_hint = {'center_x': 0.5,'center_y' : 0.26},halign = 'center',size_hint_y = None)
		
		self.label4 = MDLabel(text = 'Remember me',pos_hint = {'center_x': 0.29,'center_y' : 0.21},halign = 'center',size_hint_y = None)
		
		self.label5 = MDLabel(text = 'New to Netflix?',pos_hint = {'center_x': 0.215,'center_y' : 0.165},halign = 'center',theme_text_color = 'Secondary',size_hint_y = None)
		
		self.label6 = MDLabel(text = 'Sign up now.',bold = True,pos_hint = {'center_x': 0.48,'center_y' : 0.165},halign = 'center',theme_text_color = 'Primary',size_hint_y = None)
		
		self.label7 = MDLabel(text = '''This page is protected by Google reCAPTCHA to ensure
you're not a bot.''',pos_hint = {'center_x': 0.575,'center_y' : 0.10},theme_text_color = 'Hint',font_style = 'Subtitle2',size_hint_y =None)

		self.label8 = MDLabel(text = 'Learn more',pos_hint = {'center_x': 0.426,'center_y' : 0.09},halign = 'center',theme_text_color = 'Custom',text_color = (0,0.4,1,1),font_style = 'Subtitle2',)
		
		
		self.screen.add_widget(self.label1)
		self.screen.add_widget(self.label2)
		self.screen.add_widget(self.label3)
		self.screen.add_widget(self.label4)
		self.screen.add_widget(self.label5)
		self.screen.add_widget(self.label6)
		self.screen.add_widget(self.label7)
		self.screen.add_widget(self.label8)
		
		#Adding text fields
		self.textfield1 = MDTextField(hint_text = 'Email or phone number',pos_hint = {'center_x':0.5,'center_y':0.65},size_hint_x = 0.8,helper_text = '× Please enter a valid email address or phone number',helper_text_mode = 'on_focus',mode = 'rectangle',line_color_normal = (0.9,1,1,1),line_color_focus = (1,0,0,1),helper_text_color_focus = (1,0,0,1),size_hint_y = None)
		
		self.textfield2 = MDTextField(hint_text = 'Password',pos_hint = {'center_x':0.5,'center_y':0.55},size_hint_x = 0.8,helper_text = '× Your password must contain between 4 and 60 characters',password = True,helper_text_mode = 'on_focus',mode = 'rectangle',line_color_focus = (1,0,0,1),line_color_normal = (1,1,1,1),max_text_length =  60,line_anim = True,helper_text_color_focus = (1,0,0,1),size_hint_y = None)
		
						
		self.screen.add_widget(self.textfield1)
		self.screen.add_widget(self.textfield2)
		
		
		#Adding buttons
		self.button1 = MDFlatButton(text = 'Sign In',font_style = 'H6',pos_hint = {'center_x':0.5,'center_y':0.45},size_hint = (0.88,0.060),md_bg_color = (1,0,0,1),on_press = self.sign_in,size_hint_y = None)
		
		self.button2 = MDFlatButton(text = 'Use a sign-in code',font_style = 'Subtitle1',pos_hint = {'center_x':0.5,'center_y':0.32},size_hint = (0.88,0.060),md_bg_color = (0.22,0.22,0.22,1))
		
		
		self.button3 = MDIconButton(icon = 'eye-off',font_style = 'Subtitle1',pos_hint = {'center_x':0.845,'center_y':0.545},size_hint = (0.10,0.05),md_bg_color = (0.07,0.07,0.07,1),on_release = self.toggle_eye)
			
		
		self.screen.add_widget(self.button1)
		self.screen.add_widget(self.button2)
		self.screen.add_widget(self.button3)
		
		
		#to add checkbox
		self.checkbox = MDCheckbox(pos_hint = {'center_x': 0.10,'center_y':0.21},size_hint = (0.06,0.035),background_hue= '500',ripple_color=(1,1,1,1))
		self.screen.add_widget(self.checkbox)
		
		return self.screen
				
	#to toggle the icon 
	def toggle_eye(self,obj):
		if self.button3.icon == 'eye-off':
			self.button3.icon = 'eye'
			self.textfield2.password = False
		else:
			self.button3.icon = 'eye-off'
			self.textfield2.password = True
			
	#sign in function
	def sign_in(self,obj):
		if self.textfield1.text != '' and self.textfield2.text != '' and 4<= len(self.textfield2.text) <= 60:
			
			#to check if email or the phone number entered is valid or not
			if '@' in self.textfield1.text and '.com'  in self.textfield1.text or (len(self.textfield1.text) == 10 and self.textfield1.text.isdigit()):			
				self.textfield1.text = ''			
				self.textfield2.text = ''

			
if __name__ == '__main__':
	MYApp().run()
