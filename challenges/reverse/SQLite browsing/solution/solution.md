# Solution

The solution of this challenge is fairly easy if you know where to look. You need to download
the sqlite browser.

The trickier part is to extract the sqlite database from the app. You can do this by using adb as such:
```
adb pull /data/data/ets.dci.ctf2022.c2/databases/coursedb.db ~/Documents/Application.db
```

to find the path to the db I used this link https://stackoverflow.com/questions/4847654/how-to-access-local-files-of-the-filesystem-in-the-android-emulator
which suggested using the command and navigating through directories to find `coursedb`:
```
adb shell
```

There may be easier way of pulling the app db but it's the way that was reliable for me.
 