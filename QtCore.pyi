from typing import Callable


class Qt:

    class Alignment(int):
        ...

    class DockWidgetArea(int):
        ...

    BottomDockWidgetArea: DockWidgetArea

class QObject:

    def tr(self, sourceText: str) -> str: ...
    def setObjectName(self, objectname: str) -> None: ...

class pyqtSignal:

    def connect(self, slot: Callable) -> None: ...
