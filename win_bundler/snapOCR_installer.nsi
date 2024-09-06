!include "MUI2.nsh"


requestexecutionlevel admin

InstallDir "$PROGRAMFILES\snapOCR"

Icon "..\assets\snapOCR.ico"

; Define custom text for various pages
; 1033 is English

Name "snapOCR"
!define MUI_PRODUCT "snapOCR Setup"
LangString MUI_TEXT_WELCOME_INFO_TEXT ${1033} "Welcome to the snapOCR Setup Wizard."
LangString MUI_TEXT_DIRECTORY_TITLE ${1033} "Select Installation Directory"
LangString MUI_TEXT_DIRECTORY_SUBTITLE ${1033} "Choose where to install the application."
LangString MUI_TEXT_INSTALLING_TITLE ${1033} "Installing Files"
LangString MUI_TEXT_INSTALLING_SUBTITLE ${1033} "Please wait while the files are being installed."
LangString MUI_TEXT_FINISH_TITLE ${1033} "Installation Complete"
LangString MUI_TEXT_FINISH_SUBTITLE ${1033} "The installation was successful."
LangString MUI_TEXT_ABORT_TITLE ${1033} "Setup Aborted"
LangString MUI_TEXT_ABORT_SUBTITLE ${1033} "The setup has been aborted."
LangString MUI_BUTTONTEXT_FINISH ${1033} "Finish"
LangString MUI_TEXT_FINISH_INFO_REBOOT ${1033} "You need to restart your computer to complete the installation."
LangString MUI_TEXT_FINISH_REBOOTNOW ${1033} "Restart Now"
LangString MUI_TEXT_FINISH_REBOOTLATER ${1033} "Restart Later"

!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_LANGUAGE "English"


Section "MainSection" SEC01

    SetOutPath "$INSTDIR"
    CreateDirectory "$INSTDIR\dist"
    CreateDirectory "$INSTDIR\tessdata"

    SetOutPath "$INSTDIR\dist"
    File /r "..\snapOCR\dist\*.*"

    SetOutPath "$INSTDIR\tessdata"
    File /r "..\snapOCR\tessdata\*.*"

    File "..\assets\snapOCR.ico"


    CreateShortCut "$DESKTOP\snapOCR.lnk" "$INSTDIR\dist\snapOCR.exe" "" "$INSTDIR\tessdata\snapOCR.ico"
SectionEnd

; Uninstaller section
Section "Uninstall"
    Delete "$INSTDIR\*.*"
    RMDir /r "$INSTDIR"

    Delete "$DESKTOP\snapOCR.lnk"
    Delete "$STARTMENU\snapOCR\Uninstall.lnk"
    RMDir "$STARTMENU\snapOCR"

SectionEnd