import flet as ft
import requests
import json


def main(page: ft.Page):
	# === main page settings =========================================================================================================;
	page.title = "To Do App"
	page.window.width = 450
	page.window.height = 400

	# - top labels ---
	label1 = ft.Text( "Kelly's To do App",size = 20 ,weight=ft.FontWeight.BOLD)

	# --- Load firebas ----
	#Read database

	def load_data():
		global message
		url = 'https://flettodo-default-rtdb.europe-west1.firebasedatabase.app/.json'
		auth_key = 'AIzaSyBUSl3Wfe_VE584QjzgCN5U-cSkfD3Awh4'
		request = requests.get(url+'?auth='+auth_key)
		data_list = request.json()
		message = data_list["Item2"]
		message = message["Message"]
	load_data()

	label2 = ft.Text( f"{message}",size = 14 ,weight=ft.FontWeight.BOLD)


	#---change item in Database---
	# function to change it
	def change_item(e):
		
		#get what is inside
		changed_item = input_box.value
		#write to database
		url = 'https://flettodo-default-rtdb.europe-west1.firebasedatabase.app/.json'
		JSON = {'Item2':{"Message":changed_item}}
		JSON = json.dumps(JSON)
		to_database = json.loads(JSON)
		requests.patch(url = url, json= to_database)
		label2.value = changed_item
		page.update()


	#inputbox en button
	input_box = ft.TextField(label="Change item")
	submit_btn =ft.ElevatedButton(text="Change item", on_click=change_item)


	# === Add the widgets to the page =================================================================================================
	page.add(
		ft.Column(
			controls=[
				ft.Row([label1]),
				ft.Row([label2]),
				ft.Row([input_box]),
				ft.Row([submit_btn]),
			],
			#alignment="center",
			spacing=10
		)
	)

ft.app(main)
