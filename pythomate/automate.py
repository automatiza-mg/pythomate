import pyautogui
import time

def run_flow(flow):
	# Add check to see if OS is Windows

    # Open power automate
	pyautogui.press('win')
	pyautogui.write('power automate', interval=0.15)
	pyautogui.press('enter')

	# Check if power automate opened
	import ipdb; ipdb.set_trace(context=10)
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

if __name__ == '__main__':
	run_flow('test-pythomate')
