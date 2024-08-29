# DOD Training Helper

A tool for finishing various dod training faster

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

Then you can just use the environment normally afterwords:
```
poetry install
```

LINUX X11 based DE:
```
xhost +local:
```

Install Tesseract OCR engine:
https://github.com/tesseract-ocr/tesseract/releases


# Workflow

Double click the icon, use the selector to outline your Region Of Interest, and then open up 
your favorite LLM. Add a short primer to the text that was extracted and added to your clipboard:

For example, for a multiple choice question you might type "help me answer: " then paste what is in your clipboard. 

# Future
1. Building out JSON/ intermeidate format with metadata for question/ query responses from LLM's
2. Automatic ROI extraction option
3. Selenium workflow integration to provide end to end answering.