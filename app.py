from flask import Flask, send_file, request

app = Flask(__name__)

leaderboard_dict = {"sammy": 2, "ananth": -15}


@app.get("/ctf")
def lander():
	return '''\
welcome to the cs club ctf!
unfortunately we cant afford CSS (or even HTML for that matter) so you're gonna have to put up with this :3
check out /ctf/intro for an introduction to the challenge''', 200, {"Content-Type": "text/plain"}

@app.get("/ctf/intro")
def intro():
	return '''\
backstory:
every club needs some form of attendance tracking. however, cs club is too sigma for a paltry google form.

as such, the ever hardworking club execs finally finished their magnum opus: a functioning attendance-tracking website!

however, they must have forgot that this is, indeed, the cs club.
as a mischevious club member, it is now your goal to take over the website and get the attendance HIGH SCORE!

(this is why we can't have nice things)

the leaderboard is available at /ctf/leaderboard


your goal:
you must find all 5 numerical digits of the secret testing attendance code that lacks duplicate submission checking.
it will be obvious when a number received is a digit of the code.


digits:
0. logging in @ /ctf/login
1. access control @ /ctf/access
2. console.log in prod :( @ /ctf/logs
3. hidden secrets @ /ctf/secrets
4. cheating!? @ /ctf/cheating


finally, submit by sending a POST request to /ctf/submit with query parameters in the following format:
/ctf/submit?username=<whatever you want>&code=<attendance code>
(don't be afraid to dos attack this endpoint, it's running on my home laptop lmao)''', 200, {"Content-Type": "text/plain"}

@app.get("/ctf/login")
def login():
	if request.args.get("password") == "VerySecurePassword":
		return "The 0th (0-indexed) digit is: 9 (nine)!", 200, {"Content-Type": "text/plain"}
	return '''\
test login: (REMOVE BEFORE PUSHING TO PROD)
password: YhubVhfxuhSdvvzrug (caesar cipher key: -3)

login by sending a GET request to this endpoint with query parameters in the following format:
/ctf/login?password=<password>''', 200, {"Content-Type": "text/plain"}

@app.get("/ctf/access")
def access():
	if request.headers.get("admin", '0') == '1':
		return "The 1st (0-indexed) digit is 9 (nine)!", 200, {"Content-Type": "text/plain"}
	return "invalid credentials! is the 'admin' request header set to '1'?", 401, {"Content-Type": "text/plain"}

@app.get("/ctf/logs")
def logs():
	return '''\
<script>console.log("The 2nd (0-indexed) digit is 1 (one)!")</script>
wow, finally a proper HTML page! i'm sure this could have no repercussions :3
''', 200

@app.get("/ctf/secrets")
def secrets():
	return send_file("jamjam.png", mimetype="image/png")

@app.get("/ctf/cheating")
def cheating():
	return '''\
looks like you got bored and ended up asking someone for help with the last question.
however, in fear of the benevolent cs club execs discovering this vile treachery, they have encoded their response:
VGhlIDR0aCAoMC1pbmRleGVkKSBkaWdpdCBpcyA1IChmaXZlKSE=''', 200, {"Content-Type": "text/plain"}

@app.post("/ctf/submit")
def submit():
	if not request.args.get("username"):
		return "missing username", 400, {"Content-Type": "text/plain"}
	global leaderboard_dict
	if request.args.get("code") == "99115":
		if request.args.get("username") in leaderboard_dict:
			leaderboard_dict[request.args.get("username")] += 1
		else:
			leaderboard_dict[request.args.get("username")] = 1
		return "submission successful!", 200, {"Content-Type": "text/plain"}
	return "submission unsuccessful :(", 401, {"Content-Type": "text/plain"}

@app.get("/ctf/leaderboard")
def leaderboard():
	return f"LEADERBOARD:\n\n{'\n'.join([f'{idx}. {pair[0]} with {pair[1]} point(s)' for idx, pair in enumerate(sorted(leaderboard_dict.items(), key=lambda item: item[1], reverse=True))])}", 200, {"Content-Type": "text/plain"}


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8080)
