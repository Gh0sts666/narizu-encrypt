#!/usr/bin/python3
import os,sys
import re
import base64


class Narizu():
	def encrypt(self, txt, key):
		if key is not type(key) == int:
			print()
		else:
			result = ""
			data = txt.encode("utf8")
			base = base64.b64encode(data).decode("utf8")
			print(f"Base64 : {base}")
			ress = re.split("", base)
			ress.pop(0)
			ress.pop(-1)
			for i in ress:
				narizu = chr(ord(i) + int(key))
				result += narizu
			haha = f"$n${key}${result}"
			return haha
