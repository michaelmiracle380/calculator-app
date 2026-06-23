[app]

title = Calculator
package.name = calculatorapp
package.domain = org.yourname

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3,kivy==2.5.0

orientation = portrait
fullscreen = 0

icon.filename = %(source.dir)s/icon.png

[buildozer]

log_level = 2
warn_on_root = 1

[app:android]

python_version = 3.11
android.permissions =
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True
