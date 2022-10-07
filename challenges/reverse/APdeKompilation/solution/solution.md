# Solution

In order to do this challenge you first need to install [`apktool2`](https://ibotpeaches.github.io/Apktool/install/). 
Then using this tool you can decompile the APK.
```
java -jar apktool-2.6.1.jar d APdeKompilation.apk
```

Once it's done, it's time to explore decompiled classes found in the folder `APdeKompilation/`.
In the `smali_classes3\ets\dci\ctf2022\c3\MainActivity$OnCreate$1.smali`, it's possible to find the check for the correct flag.
It can be copied directly! 