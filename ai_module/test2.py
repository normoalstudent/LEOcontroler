from gradio_client import Client

client = Client("https://embodied-generalist-leo-demo.hf.space/--replicas/8mtig/")
result = client.predict(
		[["Hello!",None]],	# Tuple[str | Dict(file: filepath, alt_text: str | None) | None, str | Dict(file: filepath, alt_text: str | None) | None]  in 'Chat with LEO' Chatbot component
		"Hello!!",	# str  in 'parameter_16' Textbox component
		api_name="/receive_instruction"
)
print(result)