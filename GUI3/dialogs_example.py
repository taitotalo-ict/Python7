from PySide6 import QtWidgets, QtCore
from PySide6.QtGui import (
    QAction,
    QKeySequence,
    QIcon,
)
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QStatusBar,
    QDialog,
    QDialogButtonBox,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox,
    QInputDialog,
    QFileDialog,
    QScrollArea,
)

class ActionRow(QWidget):
    clicked = QtCore.Signal(object) # Custom signal

    def __init__(self, text:str, slot):
        super().__init__()

        layout = QHBoxLayout()
        self.setLayout(layout)

        self.button = QtWidgets.QPushButton(text)
        self.button.clicked.connect(self.emit_signal)
        self.clicked.connect(slot)
        layout.addWidget(self.button)
        self.input = QtWidgets.QLabel()
        self.input.setStyleSheet('background-color:White; border: 1px solid black;')
        layout.addWidget(self.input)
    
    def emit_signal(self):
        self.clicked.emit(self.input)


class CustomDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)

        self.setWindowTitle('Are you ok today?')

        buttonBox = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel, self)
        buttonBox.setCenterButtons(True)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()
        layout.addWidget(buttonBox)
        self.setLayout(layout)
        self.resize(self.minimumSizeHint())


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.TEXT_MESSAGES = {
            QMessageBox.StandardButton.Ok: 'Ok',
            QMessageBox.StandardButton.Open: 'Open',
            QMessageBox.StandardButton.Save: 'Save',
            QMessageBox.StandardButton.Cancel: 'Cancel',
            QMessageBox.StandardButton.Close: 'Close',
            QMessageBox.StandardButton.Discard: 'Discard',
            QMessageBox.StandardButton.Apply: 'Apply',
            QMessageBox.StandardButton.Reset: 'Reset',
            QMessageBox.StandardButton.RestoreDefaults: 'RestoreDefaults',
            QMessageBox.StandardButton.Help: 'Help',
            QMessageBox.StandardButton.SaveAll: 'SaveAll',
            QMessageBox.StandardButton.Yes: 'Yes',
            QMessageBox.StandardButton.YesToAll: 'YesToAll',
            QMessageBox.StandardButton.No: 'No',
            QMessageBox.StandardButton.NoToAll: 'NoToAll',
            QMessageBox.StandardButton.Abort: 'Abort',
            QMessageBox.StandardButton.Retry: 'Retry',
            QMessageBox.StandardButton.Ignore: 'Ignore',
            QMessageBox.StandardButton.NoButton: '',
        }

        self.FILE_FILTERS = [
            'All files (*)',
            'Python files (*.py)',
        ]
        self.selected_filter = self.FILE_FILTERS[0]

        # Toolbar
        toolbar = QtWidgets.QToolBar('Main toolbar')
        self.addToolBar(toolbar)

        # Some icons by [Yusuke Kamiyamane](http://p.yusukekamiyamane.com/).
        # Licensed under a [Creative Commons Attribution 3.0 License](http://creativecommons.org/licenses/by/3.0/).
        exit_action = QAction(QIcon("home--arrow.png"), "Exit", self)
        exit_action.setStatusTip("Exit the application")
        exit_action.triggered.connect(self.close)
        exit_action.setShortcut(QKeySequence("Ctrl+Q"))
        toolbar.addAction(exit_action)

        toolbar.addSeparator()

        # Toinen toolbar
        toolbar2 = QtWidgets.QToolBar('Second toolbar')
        self.addToolBar(toolbar2)


        # Status bar
        self.setStatusBar(QStatusBar(self))

        # Menu
        menu = self.menuBar()
        file_menu = menu.addMenu('&File')
        file_menu.addAction(exit_action)
        file_menu.addSeparator()
        # file_menu.add

        # button2 = QtWidgets.QPushButton('QMessageBox')
        # button2.clicked.connect(self.open_message_box)


        ## Create layout and place elements in the layout
        layout = QtWidgets.QVBoxLayout()

        layout.addWidget(ActionRow('Open custom dialog', self.open_dialog))
        layout.addWidget(ActionRow('Open default QMessageBox', self.default_message_box))
        layout.addWidget(ActionRow('Open custom QMessageBox', self.custom_message_box))
        layout.addWidget(ActionRow('Open about QMessageBox', self.about_message_box))
        layout.addWidget(ActionRow('Open critical QMessageBox', self.critical_message_box))
        layout.addWidget(ActionRow('Open information QMessageBox', self.information_message_box))
        layout.addWidget(ActionRow('Open question QMessageBox', self.question_message_box))
        layout.addWidget(ActionRow('Open warning QMessageBox', self.warning_message_box))
        layout.addWidget(ActionRow('Ask for an integer', self.int_input_dialog))
        layout.addWidget(ActionRow('Ask for a float', self.float_input_dialog))
        layout.addWidget(ActionRow('Ask for a string from a list', self.strlist_input_dialog))
        layout.addWidget(ActionRow('Ask for a string', self.str_input_dialog))
        layout.addWidget(ActionRow('Ask for a text', self.text_input_dialog))
        layout.addWidget(ActionRow('Select a file', self.file_dialog))
        layout.addWidget(ActionRow('Select a folder', self.folder_dialog))
        layout.addWidget(ActionRow('Save to a file', self.save_file_dialog))


       ## Create main widget and set its layout
        widget = QWidget(self)
        widget.setLayout(layout)

        # The main widget should go in a scroll area
        scrollArea = QScrollArea()
        scrollArea.setWidget(widget)
        widget.resize(600, widget.height())

        #
        # Set main widget as the central widget of the QMainWindow
        #
        self.setCentralWidget(scrollArea)

        # Show the window
        self.show()


    def open_dialog(self, output):
        dlg = CustomDialog(self)
        # dlg.setWindowTitle('Everything ok?')
        result = dlg.exec() # True tai False
        output.setText('Nice!' if result else "Let's hope it gets better")

    def default_message_box(self, output):
        dlg = QMessageBox(self)
        dlg.setWindowTitle('Informative box')
        dlg.setText('This is a simple message box')
        result = dlg.exec()  # QMessageBox.xxx (Ok, Cancel, ...)
        output.setText(self.TEXT_MESSAGES[result])

    def custom_message_box(self, output):
        dlg = QMessageBox(self)
        dlg.setWindowTitle('Custom message box')
        dlg.setText('Are you liking Qt framework?')
        dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        dlg.setIcon(QMessageBox.Icon.Question)
        result = dlg.exec()  # QMessageBox.xxx (Ok, Cancel, ...)
        output.setText(self.TEXT_MESSAGES[result])

    def about_message_box(self, output):
        result = QMessageBox.about(self, 'About message box', 'This is just an about message')
        output.setText(self.TEXT_MESSAGES[result] if result else 'None')

    def critical_message_box(self, output):
        result = QMessageBox.critical(self, 'Critical message box', 'Something went very wrong')
        output.setText(self.TEXT_MESSAGES[result])

    def information_message_box(self, output):
        result = QMessageBox.information(self, 'Informational message box', 'This informs you of something')
        output.setText(self.TEXT_MESSAGES[result])

    def question_message_box(self, output):
        result = QMessageBox.question(self, 'Question message box', 'Is Python the best programming language?')
        output.setText(self.TEXT_MESSAGES[result])

    def warning_message_box(self, output):
        result = QMessageBox.warning(self, 'Warning message box', 'You have to be very careful')
        output.setText(self.TEXT_MESSAGES[result])

    def int_input_dialog(self, output):
        value, result = QInputDialog.getInt(self, "Integer", "Enter an integer number")
        # Result: True tai False
        output.setText(f'{result}: {value}')

    def float_input_dialog(self, output):
        value, result = QInputDialog.getDouble(self, "Float", "Enter an decimal number")
        # Result: True tai False
        output.setText(f'{result}: {value}')

    def strlist_input_dialog(self, output):
        value, result = QInputDialog.getItem(self, "String from list", "Select one of the strings", ['A', 'B', 'C'])
        # Result: True tai False
        output.setText(f'{result}: {value}')

    def str_input_dialog(self, output):
        value, result = QInputDialog.getText(self, "Integer", "Enter a string")
        # Result: True tai False
        output.setText(f'{result}: {value}')

    def text_input_dialog(self, output):
        value, result = QInputDialog.getMultiLineText(self, "Integer", "Write a text")
        # Result: True tai False
        output.setText(f'{result}: {value}')

    def file_dialog(self, output):
        filename, self.selected_filter = QFileDialog.getOpenFileName(self, 'Select a file', filter=';;'.join(self.FILE_FILTERS), selectedFilter=self.selected_filter)
        output.setText(f'{filename} - {self.selected_filter}')

    def folder_dialog(self, output):
        folder = QFileDialog.getExistingDirectory(self, 'Select a folder')
        output.setText(folder)

    def save_file_dialog(self, output):
        dlg = QFileDialog(self)
        dlg.setWindowTitle('Select file to save to')
        dlg.setDirectory('')
        dlg.setNameFilters(self.FILE_FILTERS)
        dlg.selectNameFilter(self.FILE_FILTERS[0])
        dlg.setFileMode(QFileDialog.FileMode.AnyFile)
        result = dlg.exec()  # 0 tai 1
        output.setText(f'{result}: {dlg.selectedFiles()} - {dlg.selectedNameFilter()}')


        # QFileDialog.setWindowTitle()
        # QFileDialog.setDirectory()
        # QFileDialog.setNameFilter(str)
        # QFileDialog.setNameFilters([])
        # QFileDialog.selectNameFilter(selected_filter)
        # QFileDialog.setFileMode(mode)
        #       QFileDialog.FileMode.ExistingFile
        #       QFileDialog.FileMode.AnyFile
        #       QFileDialog.FileMode.Directory
        #       QFileDialog.FileMode.ExistingFiles
        # QFileDialog.setOptions(option | option | ...)
        #       QFileDialog.Option.ShowDirsOnly
        #       QFileDialog.Option.DontResolveSymlinks
        #       QFileDialog.Option.DontConfirmOverwrite
        #       QFileDialog.Option.DontUseNativeDialog
        #       QFileDialog.Option.ReadOnly
        #       QFileDialog.Option.HideNameFilterDetails
        #       QFileDialog.Option.DontUseCustomDirectoryIcons
        #
        # QFileDialog shortcuts:
        # - QFileDialog.getFileName()
        # - QFileDialog.getFileNames()
        # - QFileDialog.getSaveFileName()
        # - QFileDialog.getExistingDirectory()


def main():
    # Create a Qt Application
    app = QApplication([])
    
    # Create a main window using our custom class
    main_window = MainWindow()
    main_window.resize(650, main_window.height())

    # Start the main loop
    app.exec()


if __name__ == '__main__':
    main()



### Button types:
# https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QDialogButtonBox.html#PySide6.QtWidgets.QDialogButtonBox.StandardButton
# QDialogButtonBox.StandardButton.Ok
# QDialogButtonBox.StandardButton.Open
# QDialogButtonBox.StandardButton.Save
# QDialogButtonBox.StandardButton.Cancel
# QDialogButtonBox.StandardButton.Close
# QDialogButtonBox.StandardButton.Discard
# QDialogButtonBox.StandardButton.Apply
# QDialogButtonBox.StandardButton.Reset
# QDialogButtonBox.StandardButton.RestoreDefaults
# QDialogButtonBox.StandardButton.Help
# QDialogButtonBox.StandardButton.SaveAll
# QDialogButtonBox.StandardButton.Yes
# QDialogButtonBox.StandardButton.YesToAll
# QDialogButtonBox.StandardButton.No
# QDialogButtonBox.StandardButton.NoToAll
# QDialogButtonBox.StandardButton.Abort
# QDialogButtonBox.StandardButton.Retry
# QDialogButtonBox.StandardButton.Ignore
# QDialogButtonBox.StandardButton.NoButton


### QMessageBox button types:
# QMessageBox.StandardButton offers exactly the same buttons than QDialogButtonBox.StandardButton
# https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QMessageBox.html#PySide6.QtWidgets.QMessageBox.StandardButton


# QMessageBox icons:
# https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QMessageBox.html#PySide6.QtWidgets.QMessageBox.Icon
# QMessageBox.Icon.NoIcon:      The message box does not have an icon.
# QMessageBox.Icon.Question:    The message is asking a question.
# QMessageBox.Icon.Information: The message is informational only.
# QMessageBox.Icon.Warning:     The message is warning.
# QMessageBox.Icon.Critical:    The message indicates a critical problem.


# QMessageBox "syntactic sugars":
# QMessageBox.about(parent, title, message)
# QMessageBox.critical(parent, title, message[, buttons=QMessageBox.StandardButton.Ok[, defaultButton=QMessageBox.StandardButton.NoButton]])
# QMessageBox.information(parent, title, message[, buttons=QMessageBox.StandardButton.Ok[, defaultButton=QMessageBox.StandardButton.NoButton]])
# QMessageBox.question(parent, title, message[, buttons=QMessageBox.StandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)[, defaultButton=QMessageBox.StandardButton.NoButton]])
# QMessageBox.warning(parent, title, message[, buttons=QMessageBox.StandardButton.Ok[, defaultButton=QMessageBox.StandardButton.NoButton]])
