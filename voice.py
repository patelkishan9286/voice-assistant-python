import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>=0 and hour<12:
		speak('Good Morning')
	elif hour>=12 and hour<16:
		speak("Good Afternoon")
	else:
		speak("Good Evening!")

	speak("Python Assistnt here! Please tell me how may I help you?")

def takeCommand():
	r=sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.pause_thresold=1
		audio=r.listen(source)
	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language='en-in')
		print(f"User said: {query}\n")

	except Exception as e:
		print("Say that again please...")
		return "None"
	return query 
	
def sendEmail(to,content):
	server=smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.login('your-mail','your-password')
	server.sendmail('your-mail',to,content)
	server.close()

if __name__=="__main__":
	wishMe()
	while True:
		query=takeCommand().lower()

		if 'wikipedia' in query:
			speak("Searching Wikipedia...")
			query=query.replace("wikipedia","")
			results=wikipedia.summary(query,sentences=1)
			speak("According to wikipedia")
			print(results)
			speak(results)
			break

		elif 'open youtube' in query:
			webbrowser.open("youtube.com")
			break

		elif 'open google' in query:
			webbrowser.open("google.com")
			break

		elif 'open stackoverflow' in query:
			webbrowser.open("stackoverflow.com")
			break

		elif 'open gmail' in query:
			webbrowser.open("gmail.com")
			break

		elif 'open google classroom' in query:
			webbrowser.open("classroom.google.com")
			break

		elif 'play music' in query:
			music_dir="E:\\Songs"
			songs=os.listdir(music_dir)
			print(songs)
			os.startfile(os.path.join(music_dir,songs[0]))

		elif 'the time' in query:
			strTime=datetime.datetime.now().strftime("%H:%M:%S")
			speak("Its",strTime)

		elif 'open code' in query:
			codePath="C:\\Users\\inspiron\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.exe"
			os.startfile(codePath)
			break

		# elif 'email to me' in query:
		# 	try:
		# 		speak("What should I say?")
		# 		content=takeCommand()
		# 		to="jeetrshah99@gmail.com"
		# 		sendEmail(to,content)
		# 		speak("Email has been sent")
		# 	except Exception as e:
		# 		print(e)
		# 		speak("Sorry! Seems like error occured during sending this email")
		#	break