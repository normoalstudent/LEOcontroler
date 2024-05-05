from gradio_client import Client

client = Client("https://embodied-generalist-leo-demo.hf.space/--replicas/8mtig/")
result = client.predict(
		"3RScan-Bedroom",	# Literal['3RScan-Bedroom', '3RScan-Hotel', '3RScan-Livingroom', '3RScan-Nursery', '3RScan-Office', 'ScanNet-Bathroom', 'ScanNet-Bedroom', 'ScanNet-Hotel', 'ScanNet-Office', 'ScanNet-Study']  in 'Select a 3D scene' Dropdown component
		api_name="/change_scene"
)
print(result)