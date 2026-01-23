from BattleShipv2.resources import Map, Fleet

from PySide6 import QtWidgets
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QPushButton,
    QHBoxLayout,
)
import random

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from BattleShipv2.resources import Square

class SquareWidget(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.row = 0
        # self.column = 0
        # self.coordinates = coordinates
        self.square: None|Square = None  # Will be linked to a Square instance
        self.clicked.connect(self.on_click)
    
    def on_click(self):
        # print(f"Square {self.coordinates} clicked.")
        assert self.square is not None
        self.square.hit()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.BOARD_SIZE = 10
        self.setup_ui()
        self.initialize_game()


    def initialize_game(self):
        self.player_map = Map(self.BOARD_SIZE, self.player_board)
        self.computer_map = Map(self.BOARD_SIZE, self.computer_board)
        self.player_fleet = Fleet(self.player_map)
        self.computer_fleet = Fleet(self.computer_map, hidden=True)

    def setup_ui(self):
        self.setWindowTitle("BattleShip GUI")

        main_layout = QHBoxLayout()
        main_layout.setSpacing(50)
        ## Create layout and place elements in the layout

        WIDGETS_PER_ROW = self.BOARD_SIZE
        self.computer_board = {}
        board_layout = QtWidgets.QGridLayout()
        board_layout.setSpacing(5)
        for index in range(self.BOARD_SIZE * self.BOARD_SIZE):
            row = index // WIDGETS_PER_ROW
            column = index % WIDGETS_PER_ROW
            widget = SquareWidget()
            widget.setFixedWidth(50)
            widget.setFixedHeight(50)
            widget.clicked.connect(self.check_fleet_status)
            self.computer_board[(column, row)] = widget
            board_layout.addWidget(widget, row, column)
        main_layout.addLayout(board_layout)

        self.player_board = {}
        board_layout = QtWidgets.QGridLayout()
        board_layout.setSpacing(5)
        for index in range(self.BOARD_SIZE * self.BOARD_SIZE):
            row = index // WIDGETS_PER_ROW
            column = index % WIDGETS_PER_ROW
            widget = SquareWidget()
            widget.setFixedWidth(50)
            widget.setFixedHeight(50)
            widget.setEnabled(False)
            self.player_board[(column, row)] = widget
            board_layout.addWidget(widget, row, column)
        main_layout.addLayout(board_layout)

        ## Create main widget and set its layout
        widget = QWidget()
        widget.setLayout(main_layout)

        #
        # Set main widget as the central widget of the QMainWindow
        #
        self.setCentralWidget(widget)

        # Window size
        self.resize(widget.width(), 480)

        # Show the window
        self.show()

    def check_fleet_status(self):
        while True:
            coordinates = (random.randint(0,self.BOARD_SIZE-1), random.randint(0,self.BOARD_SIZE-1))
            if self.player_board[coordinates].square.is_hit:
                continue
            self.player_board[coordinates].square.hit()
            break

        if self.computer_fleet.is_destroyed:
            print("You have destroyed the computer's fleet! You win!")
            for square in self.computer_board.values():
                square.setEnabled(False)
        elif self.player_fleet.is_destroyed:
            print("Your fleet has been destroyed! You lose!")

# Create a Qt Application
app = QApplication([])

# Create a main window using our custom class
main_window = MainWindow()

# Start the main loop
app.exec()
