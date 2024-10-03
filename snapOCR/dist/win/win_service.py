import win32serviceutil
import win32service
import win32event
import servicemanager
import os
import sys

class snapOCRService(win32serviceutil.ServiceFramework):
    _svc_name_ = "snapOCR"
    _svc_display_name_ = "snapOCR Service"
    _svc_description_ = "Runs the OCR keyboard listener."

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.stop_event = win32event.CreateEvent(None, 0, 0, None)
        self.running = True

        self.start_process()

    def start_process(self):
        python_executable = sys.executable
        current_script = os.path.abspath(__file__)
        self.process = win32event.CreateProcess(
            python_executable, f'"{current_script}"',
            None, None, 0, win32process.CREATE_NO_WINDOW,
            None, None
        )

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.stop_event)
        self.running = False

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                               servicemanager.PYS_SERVICE_STARTED,
                               (self._svc_name_, ''))
        self.main()

    def main(self):
        while self.running:
            win32event.WaitForSingleObject(self.stop_event, win32event.INFINITE)

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(snapOCRService)