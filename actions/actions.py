from rasa_sdk import Action


class ActionEmail(Action):
	def name(self):
		return 'action_email'
		
	def run(self, dispatcher, tracker, domain):
		mail = tracker.get_slot('email')
		if mail is None:
			response = """Lo siento, no reconozco tu dirección como un email válido. Prueba de nuevo."""
		else:
			email = ' '.join(map(str, mail))
			response = """Perfecto. Se ha registrado {} como tu email""".format(email)
		dispatcher.utter_message(response)
		return []	