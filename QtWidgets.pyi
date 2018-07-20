from typing import List, Optional, overload, Callable
from .QtCore import QObject, pyqtSignal, Qt
from .QtGui import QPaintDevice, QIcon, QKeySequence


class QApplication():

    @staticmethod
    def applicationName() -> str: ...
    @staticmethod
    def organizationName() -> str: ...
    @staticmethod
    def applicationVersion() -> str: ...


class QWidget(QObject):

    def __init__(self, parent: Optional[QWidget]=..., flags: Optional[int]=...) -> None: ...
    def setLayout(self, layout: QLayout) -> None: ...
    def close(self) -> bool: ...
    def setVisible(self, visible: bool) -> None: ...


class QDialog(QWidget, QPaintDevice):

    def accept(self) -> None: ...


class QDialogButtonBox(QWidget):

    class StandardButton(int):
        ...

    Ok: StandardButton

    accepted: pyqtSignal

    @overload
    def __init__(self, parent: Optional[QWidget]=..., flags: Optional[int]=...) -> None: ...
    @overload
    def __init__(self, buttons: StandardButton, parent: Optional[QWidget]=..., flags: Optional[int]=...) -> None: ...


class QDockWidget(QWidget):

    @overload
    def __init__(self, title: str, parent: QWidget=..., flags: int=...) -> None: ...
    @overload
    def __init__(self, parent: QWidget=..., flags:int=...) -> None: ...
    def setWidget(self, widget: QWidget) -> None: ...
    def toggleViewAction(self) -> QAction: ...


class QLabel(QWidget):

    @overload
    def __init__(self, parent: Optional[QWidget]=..., flags: Optional[int]=...) -> None: ...
    @overload
    def __init__(self, text: str, parent: Optional[QWidget]=..., flags: Optional[int]=...) -> None: ...


class QMainWindow(QWidget):

    def setMenuBar(self, menuBar: QMenuBar) -> None: ...
    def setStatusBar(self, statusbar: QStatusBar) -> None: ...
    def addDockWidget(self, area: Qt.DockWidgetArea, dockwidget: QDockWidget) -> None: ...


class QMenuBar(QWidget):

    @overload
    def addMenu(self, menu: QMenu) -> QAction: ...
    @overload
    def addMenu(self, title: str) -> QMenu: ...
    @overload
    def addMenu(self, icon: QIcon, title: str) -> QMenu: ...


class QStatusBar(QWidget):

    def addWidget(self, widget: QWidget, stretch: int=...) -> None: ...


class QTabWidget(QWidget):

    @overload
    def addTab(self, page: QWidget, label: str) -> int: ...
    @overload
    def addTab(self, page: QWidget, icon: QIcon, label: str) -> int: ...


class QLayoutItem:
    ...


class QLayout(QObject, QLayoutItem):
    ...


class QBoxLayout(QLayout):

    def addWidget(self, widget: QWidget, stretch: int=..., alignment: Qt.Alignment=...) -> None: ...


class QVBoxLayout(QBoxLayout):
    ...


class QMenu(QWidget):

    @overload
    def addAction(str, text: str) -> QAction: ...
    @overload
    def addAction(self, icon: QIcon, text: str) -> QAction: ...
    @overload
    def addAction(self, text: str, receiver: QObject, member: str, shortcut: QKeySequence=...) -> QAction: ...
    @overload
    def addAction(self, icon: QIcon, text: str, receiver: QObject, member: str, shortcut: QKeySequence=...) -> QAction: ...
    @overload
    def addAction(self, text:str, receiver: QObject, method: Callable, shortcut: QKeySequence) -> QAction: ...
    @overload
    def addAction(self, action: QAction) -> QAction: ...
    def addSeparator(self) -> None: ...


class QAction(QObject):

    def setVisible(self, visible: bool) -> None: ...
