from requests import get

class YesNo:
	def __init__(self) -> None:
		self.api = "https://yesno.wtf"
		self.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
		}

	def get_answer(self) -> dict:
		return get(
			f"{Self.api}/api", headers=self.headers).json()
