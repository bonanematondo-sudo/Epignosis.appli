[app]

# (str) Title of your application
title = Application de gestion Epignosis

# (str) Package name
package.name = epignosis

# (str) Package domain
package.domain = org.epignosis

# (str) Source code where main.py/app.py is located
source.dir = .

# (str) Application version
version = 1.0

# (str) Python file to run
entrypoint = app.py

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientation
orientation = portrait

# (bool) Fullscreen
fullscreen = 0

# (str) Presplash
presplash.filename = %(source.dir)s

# (str) Icon
icon.filename = %(source.dir)s

# (str) Android API
android.api = 35

# (str) Android minimum API
android.minapi = 21

# (str) Android architecture
android.arch = arm64-v8a

# (bool) Copy libraries
android.copy_libs = 1

# (list) Python files to include
source.include_exts = py,png,jpg,jpeg,kv,json

# (str) Android application name
android.entrypoint = org.kivy.android.PythonActivity

# (bool) Accept SDK license
android.accept_sdk_license = True


[buildozer]

# (str) Log level
log_level = 2

# (bool) Warn if buildozer is run as root
warn_on_root = 1