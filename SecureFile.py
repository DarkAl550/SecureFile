""" SecureFile v1.0 """

import os, shutil, time

"""Login in app """
class Login(object):
	""" Constructor """
	def __init__(self, login, password, key):
		self.login = input("\nLOGIN: ")
		self.password = input("PASSWORD: ")
		
	def Log(self):
		if self.login == "admin" and self.password == "admin":
			print("**Success!**")
			time.sleep(2)
			self.key = input("\nKEY: ")
			if self.key == "Q13":
				secure = CreateSecure("","Q13")
				n = input("Choose any:\na) Lock folder\nb) Unlock folder \nc) Show/Hide secret folder\n")
				if n == "a" or n == "A":
					print(secure.Path())
					
					time.sleep(3)
					print("\n***SUCCESS!***")

				elif n == "b" or n == "B":
					print(secure.UnlockPath())
					time.sleep(3)
					print("**Success!**")

				elif n == "c" or n == "C":
					print(secure.Lock())

				else:
					print("Wrong!")
			else:
				return "Wrong!"

		elif self.login == "guest" and self.password == "":
			print("**Success!**")
			time.sleep(2)
			secure = CreateSecure("","Q13")
			n = input("Choose any:\na) Lock folder\nb) Unlock folder \n")
			if n == "a" or n == "A":
				print(secure.Path())
					
				time.sleep(3)
				print("\n***SUCCESS!***")

			elif n == "b" or n == "B":
				print(secure.UnlockPath())
				time.sleep(3)
				print("**Success!**")

				
			else:
				print("Wrong!")

		else:
			return "Wrong!"
			

""" Add password for catalog and reserve this catalog """
class CreateSecure(object):

	def __init__(self, path, key):
		""" Constructor """
		self.path = path
		self.key = key

	def Path(self):
		""" Found file or catalog """
		self.path = input("\nInput path to catalog >> ")
		name = input("Input name this catalog >> ")
		defpath = "userdata/" + name

		shutil.move(self.path, defpath)

		return "Your real files in catalog < "+defpath+" >"

	def UnlockPath(self):
		""" Return file or catalog """
		self.path = input("\nInput path to back file >> ")
		name = input("Name this catalog >> ")
		defpath = "userdata/" + name
		shutil.move(defpath, self.path)

		return "Your file or catalog was return < %s >" % self.path

	def Lock(self):
		""" Lock file """
		os.startfile("lock.bat")
		
		return "Key for this catalog %s" % self.key


		



""" MAIN """
if __name__ == "__main__":
	
	print("\n\nThis SecureFile v." + str(1.0) + ". Please input your login and password")
	
	l = Login("","","")
	print(l.Log())
