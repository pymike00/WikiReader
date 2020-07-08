# WikiReader
Multi platform application to browse Wikipedia's summaries. Can be built to run standalone on Android and iOS. Written using Kivy and KivyMD, as a project for my YouTube Series "How to Build Smartphone Apps With Python".


### To run the app locally:
Using Python 3.8+, create a virtual environment using [venv](https://docs.python.org/3/library/venv.html) and install the dependencies with pip install -r requirements.txt. Then, run the main.py script. Please note that Kivy 1.11 does not support Python 3.8. You can use 2.0 (rc if final not yet available) instead.


### To to build the App for Smartphone:
You can use [Buildozer](https://github.com/kivy/buildozer). A buildozer.spec file is provided with the repo. The procedure is explained in lesson 2 of the series.


### To to build the App for Desktop:
You can use [PyInstaller](https://github.com/pyinstaller/pyinstaller). Feel free to watch my related [italian](https://youtu.be/BYtSNfEacSo) or [english](https://youtu.be/vg24wionhFg) video tutorials  to learn how to use it.


### Questions

Q: Where can I find the series? \
A: The series is in Italian and can be found, free of charge, [at this link](https://www.youtube.com/playlist?list=PLHUQL6-_n9ZdPfFls4HJIQ1biWOxPI1rG) 

Q: Will you publish this same series on your international channel as well? \
A: I am not planning to release the series on my International YouTube channel at the moment, but I might definitely do so in the future. If you follow my international channel and are interested in the series, please get in touch on [twitter](https://www.twitter.com/pymike00)

Q: The endpoints you are connecting to look very weird: why are you doing so? \
A: I agree! Unfortunately the REST endpoints offered by Wikimedia only provide a one line string as "summary" of single voices. Therefore, I opted for using the endpoints provided by the Action API. I will however also attach a version of this app that uses the REST Endpoints. Feel free to get in touch on [twitter](https://www.twitter.com/pymike00) or send a pull request if you have a better alternative. Thanks.

Q: Why do you pack so much code into a single commit? \
A: It's just one way to make it easier for people watching the series to access the code written for a specific lesson. 





#### MD DOC UNDER DEVELOPMENT.