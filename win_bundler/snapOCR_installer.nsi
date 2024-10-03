!include "MUI2.nsh"
Unicode True

requestexecutionlevel admin
InstallDir "$PROGRAMFILES\snapOCR"

Icon "..\assets\snapOCR.ico"
Name "snapOCR"
!define MUI_PRODUCT "snapOCR Setup"

!insertmacro MUI_LANGUAGE "English"
!insertmacro MUI_LANGUAGE "SimpChinese"


; Define language strings for English (1033)
LangString MUI_TEXT_WELCOME_INFO_TITLE ${LANG_ENGLISH} "Welcome"
LangString MUI_TEXT_WELCOME_INFO_TEXT ${LANG_ENGLISH} "This will install snapOCR on your computer."
LangString MUI_TEXT_DIRECTORY_TITLE ${LANG_ENGLISH} "Select Destination Location"
LangString MUI_TEXT_DIRECTORY_SUBTITLE ${LANG_ENGLISH} "Please select the folder where snapOCR will be installed."
LangString MUI_TEXT_INSTALLING_TITLE ${LANG_ENGLISH} "Installing"
LangString MUI_TEXT_INSTALLING_SUBTITLE ${LANG_ENGLISH} "Please wait while the files are being installed."
LangString MUI_TEXT_FINISH_TITLE ${LANG_ENGLISH} "Installation Complete"
LangString MUI_TEXT_FINISH_SUBTITLE ${LANG_ENGLISH} "Thank you for installing snapOCR."
LangString MUI_TEXT_ABORT_TITLE ${LANG_ENGLISH} "Installation Aborted"
LangString MUI_TEXT_ABORT_SUBTITLE ${LANG_ENGLISH} "The installation has been aborted."
LangString MUI_BUTTONTEXT_FINISH ${LANG_ENGLISH} "Finish"
LangString MUI_TEXT_FINISH_INFO_TITLE ${LANG_ENGLISH} "Finished"
LangString MUI_TEXT_FINISH_INFO_TEXT ${LANG_ENGLISH} "You can now run snapOCR."
LangString MUI_TEXT_FINISH_REBOOT ${LANG_ENGLISH} "Please Reboot Now."
LangString MUI_TEXT_FINISH_REBOOTNOW ${LANG_ENGLISH} "Please reboot now" ;add reboot now trigger
LangString MUI_TEXT_FINISH_REBOOTLATER ${LANG_ENGLISH} "reboot later or now" ;add reboot now/later dialogue trigger
LangString MUI_UNTEXT_CONFIRM_TITLE ${LANG_ENGLISH} "Confirmation Required"
LangString MUI_UNTEXT_CONFIRM_SUBTITLE ${LANG_ENGLISH} "Please confirm your action"
LangString MUI_UNTEXT_UNINSTALLING_TITLE ${LANG_ENGLISH} "Uninstallation Confirmation"
LangString MUI_UNTEXT_UNINSTALLING_SUBTITLE ${LANG_ENGLISH} "Are you sure you want to uninstall?"
LangString MUI_UNTEXT_FINISH_TITLE ${LANG_ENGLISH} "Installation Complete"
LangString MUI_UNTEXT_FINISH_SUBTITLE ${LANG_ENGLISH} "The installation has finished successfully"
LangString MUI_UNTEXT_ABORT_TITLE ${LANG_ENGLISH} "Action Aborted"
LangString MUI_UNTEXT_ABORT_SUBTITLE ${LANG_ENGLISH} "The process has been aborted"
LangString MUI_UNTEXT_FINISH_INFO_TITLE ${LANG_ENGLISH} "Completion Information"
LangString MUI_UNTEXT_FINISH_INFO_REBOOT ${LANG_ENGLISH} "A reboot is required due to"
LangString MUI_UNTEXT_FINISH_INFO_TEXT ${LANG_ENGLISH} "Thank you for using my application!"
LangString MUI_TEXT_FINISH_INFO_REBOOT ${LANG_ENGLISH} "A reboot is required in the future"
LangString MUI_TEXT_FINISH_INFO_REBOOTNOW ${LANG_ENGLISH} "A reboot is required now" ;add reboot option in future


; Define language strings for Simplified Chinese (2052)
LangString MUI_TEXT_WELCOME_INFO_TITLE ${LANG_SIMPCHINESE} "欢迎"
LangString MUI_TEXT_WELCOME_INFO_TEXT ${LANG_SIMPCHINESE} "这将会在您的计算机上安装 snapOCR。"
LangString MUI_TEXT_DIRECTORY_TITLE ${LANG_SIMPCHINESE} "选择目标位置"
LangString MUI_TEXT_DIRECTORY_SUBTITLE ${LANG_SIMPCHINESE} "请选择要安装 snapOCR 的文件夹。"
LangString MUI_TEXT_INSTALLING_TITLE ${LANG_SIMPCHINESE} "正在安装"
LangString MUI_TEXT_INSTALLING_SUBTITLE ${LANG_SIMPCHINESE} "请等待文件安装。"
LangString MUI_TEXT_FINISH_TITLE ${LANG_SIMPCHINESE} "安装完成"
LangString MUI_TEXT_FINISH_SUBTITLE ${LANG_SIMPCHINESE} "感谢您安装 snapOCR。"
LangString MUI_TEXT_ABORT_TITLE ${LANG_SIMPCHINESE} "安装中止"
LangString MUI_TEXT_ABORT_SUBTITLE ${LANG_SIMPCHINESE} "安装已中止。"
LangString MUI_BUTTONTEXT_FINISH ${LANG_SIMPCHINESE} "完成"
LangString MUI_TEXT_FINISH_INFO_TITLE ${LANG_SIMPCHINESE} "完成"
LangString MUI_TEXT_FINISH_INFO_TEXT ${LANG_SIMPCHINESE} "您现在可以运行 snapOCR。"
LangString MUI_TEXT_FINISH_REBOOT ${LANG_SIMPCHINESE} "现在重启"
LangString MUI_TEXT_FINISH_REBOOTNOW ${LANG_SIMPCHINESE} "现在重启"
LangString MUI_TEXT_FINISH_REBOOTLATER ${LANG_SIMPCHINESE} "稍后重启"
LangString MUI_UNTEXT_CONFIRM_TITLE ${LANG_SIMPCHINESE} "确认"
LangString MUI_UNTEXT_CONFIRM_SUBTITLE ${LANG_SIMPCHINESE} "确认子标题"
LangString MUI_UNTEXT_UNINSTALLING_TITLE ${LANG_SIMPCHINESE} "卸载确认"
LangString MUI_UNTEXT_UNINSTALLING_SUBTITLE ${LANG_SIMPCHINESE} "卸载信息"
LangString MUI_UNTEXT_FINISH_TITLE ${LANG_SIMPCHINESE} "完成确认"
LangString MUI_UNTEXT_FINISH_SUBTITLE ${LANG_SIMPCHINESE} "完成副标题"
LangString MUI_UNTEXT_ABORT_TITLE ${LANG_SIMPCHINESE} "中止标题"
LangString MUI_UNTEXT_ABORT_SUBTITLE ${LANG_SIMPCHINESE} "中止副标题"
LangString MUI_UNTEXT_FINISH_INFO_TITLE ${LANG_SIMPCHINESE} "完成信息"
LangString MUI_UNTEXT_FINISH_INFO_REBOOT ${LANG_SIMPCHINESE} "需要重启，因为"
LangString MUI_UNTEXT_FINISH_INFO_TEXT ${LANG_SIMPCHINESE} "英语"
LangString MUI_TEXT_FINISH_INFO_REBOOT ${LANG_SIMPCHINESE} "需要重启以应用更改"
LangString MUI_TEXT_FINISH_INFO_REBOOTNOW ${LANG_SIMPCHINESE} "立即重启"

!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES
!insertmacro MUI_UNPAGE_FINISH


Section "MainSection" SEC01
    ; Create proper directories, Copy with File keyword, and setup uninstaller registry files
    SetOutPath "$INSTDIR"
    CreateDirectory "$INSTDIR\dist"
    CreateDirectory "$INSTDIR\tessdata"
    CreateDirectory "$SMPROGRAMS\snapOCR"

    CreateShortcut "$SMPROGRAMS\snapOCR\snapOCR.lnk" "$INSTDIR\dist\snapOCR.exe" "" "$INSTDIR\tessdata\snapOCR.ico"
    CreateShortCut "$DESKTOP\snapOCR.lnk" "$INSTDIR\dist\snapOCR.exe" "" "$INSTDIR\tessdata\snapOCR.ico"

    SetOutPath "$INSTDIR\dist"
    File /r "..\snapOCR\dist\*.*"

    SetOutPath "$INSTDIR\tessdata"
    File /r "..\snapOCR\tessdata\*.*"
    File "..\assets\snapOCR.ico"

    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\snapOCR" "DisplayName" "snapOCR"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\snapOCR" "UninstallString" "$INSTDIR\uninstall.exe"
    WriteUninstaller "$INSTDIR\uninstall.exe"


SectionEnd

Section "Uninstall"
    ; Delete files and directories
    Delete "$INSTDIR\dist\*.*"
    Delete "$INSTDIR\tessdata\*.*"
    Delete "$INSTDIR\snapOCR.ico"
    RMDir /r "$INSTDIR\dist"
    RMDir /r "$INSTDIR\tessdata"
    RMDir "$INSTDIR"

    ; Remove shortcuts
    Delete "$DESKTOP\snapOCR.lnk"
    Delete "$SMPROGRAMS\snapOCR\snapOCR.lnk"
    RMDir "$SMPROGRAMS\snapOCR"

    ; Remove from registry
    DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\snapOCR"
SectionEnd

UninstallIcon "..\assets\snapOCR.ico"