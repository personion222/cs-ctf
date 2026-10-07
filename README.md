# cs-ctf
CTF made for CS club senior room
```
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
(don't be afraid to dos attack this endpoint, it's running on my home laptop lmao)
```
