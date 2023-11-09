import pyautogui
import time

def run_flow(flow):
	# Add check to see if OS is Windows

    # Open power automate
	pyautogui.press('win')
	pyautogui.write('power automate', interval=0.15)
	pyautogui.press('enter')

	# Check if power automate opened
	open_image = 'power_automate_check_open.png'
	check_load_page(open_image)

	# Maximixe power automate
	with pyautogui.hold('win'):
		pyautogui.press('up')

	# Search flow
	my_flows_image = 'power_automate_my_flows.png'
	search_image = 'power_automate_flow_search.png'
	# Enter my flows
	check_load_page(my_flows_image)
	pyautogui.click(my_flows_image)
	# Search engine
	check_load_page(search_image)
	pyautogui.click(search_image)
	pyautogui.write(flow, interval=0.25)
	pyautogui.press('enter')

	# Run flow
	flow_run_image = 'power_automate_flow_run.png'
	check_load_page(flow_run_image)
	pyautogui.click(flow_run_image)

def check_load_page(picture):
	location = None
	picture_path = f'pythomate/pictures/{picture}'

	while location == None:
		try:
			location = pyautogui.locateOnScreen(picture_path)
			print(f'Looking for {picture}.')
		except Exception as e:
			print(e)

	return None

def run_flow_2(flow):
	from pywinauto.application import Application
	# Este stackoverflow responde aonde está o executável do power automate
	# Mostra também que é possível realizar a chamada via linha de comando, mas ao tentar ele ainda pede alguns cliques antes de iniciar o fluxo
	# https://stackoverflow.com/questions/75714376/cant-find-pad-console-host-exe-on-my-pc-to-run-flows-through-powershell
	
	# vídeo que ajudou https://www.youtube.com/watch?v=R4E4IOIC63s
	power_automate_exe_path = 'C:/Program Files (x86)/Power Automate Desktop/PAD.Console.Host.exe'
	app = Application(backend="uia").start(power_automate_exe_path).connect(
																			title='Power Automate',
																			timeout=100,
																			)
	dlg_spec = app.PowerAutomate
	
	# Clica linha do fluxo
	flow_line = dlg_spec.child_window(
									  title=flow, 
									  control_type='DataItem',
									  ).wrapper_object()
	flow_line.click_input()
	# Clica na execução do fluxo	
	flow_button = dlg_spec.child_window(
										title="Executar", 
										auto_id="StartFlowButton", 
										control_type="Button"
										).wrapper_object()
	flow_button.click_input()


	ok_button = dlg_spec.child_window(
									  title="OK",
									  auto_id="Button",
									  control_type="Button"
									  )
	
	# import ipdb; ipdb.set_trace(context=10)
	# dlg_spec.print_control_identifiers()
	ok_button.click_input()

if __name__ == '__main__':
	# run_flow('ffak')
	run_flow_2('conectarh')
