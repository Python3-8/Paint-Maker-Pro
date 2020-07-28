from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Ellipse, Color, Rectangle
from kivy.uix.label import Label
from android.permissions import request_permissions, Permission
from datetime import datetime
from kivy.utils import platform
from os import getcwd, mkdir
from os.path import join, isdir
from kivy.uix.button import Button
from random import uniform
from kivy.uix.colorpicker import ColorPicker
from kivy.core.window import Window
from kivy.uix.popup import Popup

Window.clearcolor = (1, 1, 1, 1)
Window.set_system_cursor('crosshair')


class clr_pkr:
	def __init__(self, can, **kwargs):
		super(clr_pkr, self).__init__(**kwargs)
		self.pkr = ColorPicker(
			pos_hint={'center_x': 0.5, 'center_y': 0.5}, size_hint=(1, 1))
		self.pkr.bind(color=lambda instance, value: can.add(
			Color(value[0], value[1], value[2], value[3])))
		self.pk()

	def pk(self):
		return self.pkr


class PaintWindow(Widget):
	shape_size = (20, 20)
	shape = 'cir'

	def on_touch_down(self, touch):
		Window.set_system_cursor('crosshair')
		with self.canvas:
			Ellipse(pos=(touch.pos[0] - self.shape_size[0] / 2,
						 touch.pos[1] - self.shape_size[1] / 2), size=self.shape_size) if self.shape == 'cir' else Rectangle(pos=(touch.pos[0] - self.shape_size[0] / 2,
																																  touch.pos[1] - self.shape_size[1] / 2), size=self.shape_size)

	def on_touch_move(self, touch):
		self.canvas.add(Ellipse(pos=(touch.pos[0] - self.shape_size[0] / 2,
									 touch.pos[1] - self.shape_size[1] / 2), size=self.shape_size) if self.shape == 'cir' else Rectangle(pos=(touch.pos[0] - self.shape_size[0] / 2,
																																			  touch.pos[1] - self.shape_size[1] / 2), size=self.shape_size))

	def set_shape_size(self, b, l):
		self.shape_size = (b, l)

	def set_shape(self, shape):
		self.shape = shape


class popup(Popup):
	@staticmethod
	def pop(tit, con):
		Window.set_system_cursor('arrow')
		window = Popup(title=tit, content=con,
					   size_hint=(None, None), size=pop_size)
		window.open()


class PaintApp(App):
	title = 'Paint Maker Pro'
	icon = 'Icon.png'

	def build(self):
		global pop_size
		pop_size = (Window.width / 1.6, Window.height / 1.2)
		print(pop_size)
		self.root = Widget()
		self.paint = PaintWindow()
		btn_col = (uniform(0, 1), uniform(0, 1), uniform(0, 1), 1)
		self._100 = Window.width / 8
		self._50 = Window.width / 16
		self._150 = Window.width / (5 + 1 / 3)
		self._100_100 = (Window.width / 8, Window.height / 6)
		self._150_100 = (Window.width / (5 + 1 / 3), Window.height / 6)
		self._50_100 = (Window.width / 16, Window.height / 6)
		self.font_15 = self._100 / (6 + 2 / 3)
		self.clear_btn = Button(text='Clear', background_color=btn_col,
								on_release=self.clear_canvas, pos=(0, 0), size=self._100_100, font_size=self.font_15)
		self.save_btn_jpg = Button(text='Save as JPG', background_color=btn_col,
								   on_release=self.save_canvas, pos=(self._100, 0), size=self._150_100, font_size=self.font_15)
		self.select_col_btn = Button(text='Select a Color', background_color=btn_col,
									 on_release=lambda for_kivy: popup.pop('Select a Color', clr_pkr(self.paint.canvas).pk()), pos=(self._100 + (self._150 or 250), 0), size=self._150_100, font_size=self.font_15)
		self.erase_btn = Button(text='Erase', background_color=btn_col,
								on_release=lambda for_kivy: self.paint.canvas.add(Color(1, 1, 1, 1)), pos=(self._100 + (self._150 or 250) + self._150, 0), size=self._100_100, font_size=self.font_15)
		self.pt_10 = Button(text='10 PX', background_color=btn_col,
							on_release=lambda for_kivy: self.paint.set_shape_size(10, 10), pos=(self._100 + (self._150 or 250) + self._150 + self._100, 0), size=self._50_100, font_size=self.font_15)
		self.pt_20 = Button(text='20 PX', background_color=btn_col,
							on_release=lambda for_kivy: self.paint.set_shape_size(20, 20), pos=(self._100 + (self._150 or 250) + self._150 + self._100 + self._50, 0), size=self._50_100, font_size=self.font_15)
		self.pt_30 = Button(text='30 PX', background_color=btn_col,
							on_release=lambda for_kivy: self.paint.set_shape_size(30, 30), pos=(self._100 + (self._150 or 250) + self._150 + self._100 + self._50 * 2, 0), size=self._50_100, font_size=self.font_15)
		self.pt_40 = Button(text='40 PX', background_color=btn_col,
							on_release=lambda for_kivy: self.paint.set_shape_size(40, 40), pos=(self._100 + (self._150 or 250) + self._150 + self._100 + self._50 * 3, 0), size=self._50_100, font_size=self.font_15)
		self.pt_50 = Button(text='50 PX', background_color=btn_col,
							on_release=lambda for_kivy: self.paint.set_shape_size(50, 50), pos=(self._100 + (self._150 or 250) + self._150 + self._100 + self._50 * 4, 0), size=self._50_100, font_size=self.font_15)
		self.pt_60 = Button(text='60 PX', background_color=btn_col,
							on_release=lambda for_kivy: self.paint.set_shape_size(60, 60), pos=(self._100 + (self._150 or 250) + self._150 + self._100 + self._50 * 5, 0), size=self._50_100, font_size=self.font_15)
		self.cir_btn = Button(text='Circle', background_color=btn_col,
							  on_release=lambda for_kivy: self.paint.set_shape('cir'), pos=(self._100 + (self._150 or 250) + self._150 +
																							self._100 + self._50 * 5 + 5, Window.height - Window.height / 6), size=(Window.width - (self._100 + (self._150 or 250) + self._150 +
																																													self._100 + self._50 * 5 + 5), Window.height / 6), font_size=self.font_15)
		self.rec_btn = Button(text='Square', background_color=btn_col,
							  on_release=lambda for_kivy: self.paint.set_shape('rec'), pos=(self._100 + (self._150 or 250) + self._150 +
																							self._100 + self._50 * 5 + 5, Window.height - Window.height / 6 - Window.height / 6), size=(Window.width - (self._100 + (self._150 or 250) + self._150 +
																																																		self._100 + self._50 * 5 + 5), Window.height / 6), font_size=self.font_15 / 1.07)
		self.paint.canvas.add(
			Rectangle(pos=(0, 0), size=(Window.width, Window.height)))
		self.paint.canvas.add(Rectangle(source='Icon.png', pos=(
			0, Window.height / 6 + 5), size=(self._100 + (self._150 or 250) + self._150 +
											 self._100 + self._50 * 5, Window.height - Window.height / 6 + 5)))
		self.root.add_widget(self.paint)
		self.root.add_widget(self.clear_btn)
		self.root.add_widget(self.save_btn_jpg)
		self.root.add_widget(self.select_col_btn)
		self.root.add_widget(self.erase_btn)
		self.root.add_widget(self.pt_10)
		self.root.add_widget(self.pt_20)
		self.root.add_widget(self.pt_30)
		self.root.add_widget(self.pt_40)
		self.root.add_widget(self.pt_50)
		self.root.add_widget(self.pt_60)
		self.root.add_widget(self.cir_btn)
		self.root.add_widget(self.rec_btn)
		self.root.canvas.add(Color(1, 1, 0, 1))
		self.root.canvas.add(
			Rectangle(pos=(0, Window.height / 6), size=(Window.width, 5)))
		self.root.canvas.add(Rectangle(pos=(self._100 + (self._150 or 250) + self._150 +
											self._100 + self._50 * 5, Window.height / 6 + 5), size=(5, Window.height - Window.height / 6)))
		self.paint.canvas.add(Color(0, 0, 0, 1))
		return self.root

	def clear_canvas(self, for_kivy):
		children = self.paint.canvas.children
		children.reverse()
		for col, child in enumerate(children):
			if type(child) == Color:
				break
		last_col = children[col]
		self.paint.canvas.clear()
		self.paint.canvas.add(
			Rectangle(pos=(0, 0), size=(Window.width, Window.height)))
		self.paint.canvas.add(last_col)
		self.btn_col = (uniform(0, 1), uniform(0, 1), uniform(0, 1), 1)
		self.clear_btn.background_color = self.btn_col
		self.save_btn_jpg.background_color = self.btn_col
		self.select_col_btn.background_color = self.btn_col
		self.erase_btn.background_color = self.btn_col
		self.pt_10.background_color = self.btn_col
		self.pt_20.background_color = self.btn_col
		self.pt_30.background_color = self.btn_col
		self.pt_40.background_color = self.btn_col
		self.pt_50.background_color = self.btn_col
		self.pt_60.background_color = self.btn_col
		self.rec_btn.background_color = self.btn_col
		self.cir_btn.background_color = self.btn_col

	def save_canvas(self, for_kivy):
		filename = datetime.now().strftime('PMP_Drawing_at_%a_%b_%d_%I:%M:%S:%f_%p_%Y.jpg')
		if platform == 'android':
			if not isdir('/storage/emulated/0/DCIM/Paint Maker Pro/'):
				mkdir('/storage/emulated/0/DCIM/Paint Maker Pro/')
			self.root.export_as_image().save(join('/storage/emulated/0/DCIM/Paint Maker Pro/', filename))
		else:
			self.root.export_as_image().save(filename)
		self.btn_col = (uniform(0, 1), uniform(0, 1), uniform(0, 1), 1)
		self.save_btn_jpg.background_color = self.btn_col
		self.clear_btn.background_color = self.btn_col
		self.select_col_btn.background_color = self.btn_col
		self.erase_btn.background_color = self.btn_col
		self.pt_10.background_color = self.btn_col
		self.pt_20.background_color = self.btn_col
		self.pt_30.background_color = self.btn_col
		self.pt_40.background_color = self.btn_col
		self.pt_50.background_color = self.btn_col
		self.pt_60.background_color = self.btn_col
		self.rec_btn.background_color = self.btn_col
		self.cir_btn.background_color = self.btn_col
		if platform == 'android':
			text = 'Drawing saved at:\n/DCIM/Paint Maker Pro/'
		else:
			text = 'Drawing saved.'
		popup.pop(filename, Label(text=text, font_size=self.font_15))


if __name__ in ['__android__', '__main__']:
	if platform == 'android':
		request_permissions([Permission.WRITE_EXTERNAL_STORAGE])
	PaintApp().run()
