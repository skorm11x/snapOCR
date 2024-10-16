# snapOCR

A tool for snapping a capture of a region of interest and extracting the text

#


## TODO

Somehow fix pyinstaller broken setuptools on windows box.

Would only add:
```
poetry add --dev pyinstaller
```

Also needs fixes for PyQt5 in poetry
```
poetry add PyQt5
```



For now you need pyinstaller locally to generate releases:
```
pip install pyinstaller
```

Pyinstaller currently tested working on linux!
Run pyinstaller against the spec file:

inside the project source snapOCR/snapOCR
'''
pyinstaller main.spec
'''

This will output the standalone binaries into a dist folder.

Then you can just use the environment normally afterwords:
```
poetry install
```

LINUX X11 based DE:
```
xhost +local:
```
Also install/ ensure xclip is on system or you will get:

Debian:
```
Error: Cannot find '.setClipboardContents' in object /klipper at org.kde.klipper
```
Solve with:
```
sudo apt-get install xclip
```

Install Tesseract OCR engine:
https://github.com/tesseract-ocr/tesseract/releases

Ensure you are using the latest versions for good results! Don't rely on package manager. I build it from source included on tesseract instructions.


# Workflow

Double click the icon, use the selector to outline your Region Of Interest, and then open up 
your favorite LLM. Add a short primer to the text that was extracted and added to your clipboard:

For example, for a multiple choice question you might type "help me answer: " then paste what is in your clipboard. 

# Lint
```
poetry run pylint --rcfile=.pylintrc snapOCR/
```

# Build binary
from within snapOCR folder, 
```
poetry run pyinstaller main.spec
```

## Windows fix

```
Open the Run dialog:

Press Win + R.
Open Registry Editor:

Type regedit and hit Enter.
Navigate to the following path:

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem
Find or create LongPathsEnabled:

Look for a key named LongPathsEnabled.
If it exists, double-click it and set its value to 1.
If it doesn’t exist, right-click in the right pane, select New > DWORD (32-bit) Value, name it LongPathsEnabled, and set the value to 1.
Reboot your computer:

The changes will take effect after restarting the system.

```

Also,

afterwords run poetry install will result in a failure to install pyqt5.
Install it manually:
```
poetry run pip install PyQt5
```

make sure you run the script with the environment python e.gg
```
poetry run python main.py
```
or within poetry shell
```
poetry shell
python main.py
```

# Future
<del>1. Change the QT application flow so "main" is responsible and modules just leverage off it.</del>

2. Bundle tesseract with builds
3. linux distribution
4. add certs to exe generation for windows
5. Add modules for tesseract / OCR magik stuff
6. Automatic ROI extraction option
7. Template/ memory for specific functions/ forms that is useful over time (think dod standard forms etc.)
9. Selenium automation 