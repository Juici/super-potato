from typing import List, Tuple

from constants import HIDPI_FACTOR, Key
from modules import pygame, simplegui
from util import Polygon
from vector import Vector


class Window(object):
    """
    The game window, only one may be created.
    """

    def __init__(self, title: str, size: Tuple[int, int], fullscreen: bool = False):
        """
        Creates a new game window.
        """
        self.hidpi_factor = HIDPI_FACTOR  # HiDPI scale factor.

        self.handler = WindowHandler(self)  # A noop window handler.

        self._hide_control_panel()  # Hide control panel.
#        self.fullscreen = self._set_fullscreen(fullscreen)  # Set fullscreen state.

        # Get appropriate window size.
        self.width, self.height = self._get_window_size(size, fullscreen)
        self.title = title

        # Create the frame.
        self.frame = self._create_frame()

        # Set the frame event handlers.
        self.frame.set_draw_handler(self._render)
        self.frame.set_mouseclick_handler(self._on_click)
        self.frame.set_mousedrag_handler(self._on_drag)
        self.frame.set_keydown_handler(self._on_key_down)
        self.frame.set_keyup_handler(self._on_key_up)

    def show(self):
        """
        Shows the window.
        """
        self.frame.start()

    def destroy(self):
        """
        Destroys the window.
        """
        self.frame.stop()

    # noinspection PyMethodMayBeStatic
    def get_title(self) -> str:
        """
        Returns the title of the window.
        """
        return pygame.display.get_caption()

    # noinspection PyMethodMayBeStatic
    def set_title(self, title: str):
        """
        Sets the title of the window.
        """
        return pygame.display.set_caption(title)

    # noinspection PyMethodMayBeStatic
    def get_cursor_pos(self) -> Vector:
        x, y = pygame.mouse.get_pos()
        return Vector(x, y)

    # noinspection PyMethodMayBeStatic
    def set_cursor_pos(self, pos: Vector):
        return pygame.mouse.set_pos((pos.x, pos.y))

    def get_size(self) -> Tuple[int, int]:
        return self.width, self.height

    # Event handlers

    def _render(self, canvas: simplegui.Canvas):
        """
        Called by the window draw handler every game tick.
        Passes the render to the handler.
        """
        if self.handler is not None:
            self.handler.render(canvas)

    def _on_click(self, pos: Tuple[int, int]):
        """
        Called whenever the window receives a mouse click event.
        Passes the event to the handler.
        """
        if self.handler is not None:
            self.handler.on_click(Vector(pos[0], pos[1]))

    def _on_drag(self, pos: Tuple[int, int]):
        """
        Called whenever the window receives a mouse drag event.
        Passes the event to the handler.
        """
        if self.handler is not None:
            self.handler.on_drag(Vector(pos[0], pos[1]))

    def _on_key_down(self, key: int):
        """
        Called whenever the window receives a key down event.
        Passes the event to the handler.
        """
        if self.handler is not None:
            self.handler.on_key_down(Key(key))

    def _on_key_up(self, key: int):
        """
        Called whenever the window receives a key up event.
        Passes the event to the handler.
        """
        if self.handler is not None:
            self.handler.on_key_up(Key(key))

    # Internal

    # noinspection PyProtectedMember
    def _create_frame(self) -> simplegui.Frame:
        """
        Creates the window frame, magic may or may not come included.
        """
        offset = 4
        fake_width = self.width - offset
        fake_height = self.height - offset

        frame: simplegui.Frame = simplegui.create_frame(self.title, fake_width, fake_height)
        frame._canvas._frame_parent = None
        frame._canvas._pygame_surface = None
        frame._canvas = simplegui.Canvas(frame, self.width, self.height)

        # Magical fixes in the pygame implementation.
        frame._control_width = 0
        frame._border_size = 0
        frame._canvas_border_size = 0
        frame._canvas_x_offset = 0
        frame._canvas_y_offset = 0
        frame._statusmouse_x_offset = 0
        frame._statusmouse_y_offset = 0
        frame._statuskey_x_offset = 0
        frame._statuskey_y_offset = 0
        simplegui.Frame._statuskey_height = 0
        simplegui.Frame._statusmouse_height = 0

        # redraw frame to correct size
        frame._pygame_surface: pygame.Surface = pygame.display.set_mode((self.width, self.height),
                                                                        simplegui.Frame._pygame_mode_flags,
                                                                        simplegui.Frame._pygame_mode_depth)
        frame._pygame_surface.fill(simplegui.Frame._background_pygame_color)

        # update display
        pygame.display.update()
        pygame.display.flip()

        return frame

    @staticmethod
    def _hide_control_panel():
        """
        Attempts to hide the control panel.
        """
        simplegui.Frame._hide_controlpanel = True

    @staticmethod
    def _set_fullscreen(value: bool) -> bool:
        """
        Attempts to set the fullscreen status.
        """
        # noinspection PyProtectedMember
        flags = simplegui.Frame._pygame_mode_flags
        enable = pygame.FULLSCREEN | pygame.HWSURFACE
        if value:
            flags |= enable
        else:
            flags &= ~enable
        simplegui.Frame._pygame_mode_flags = flags

        return value

    @staticmethod
    def _get_window_size(size: Tuple[int, int], fullscreen: bool) -> Tuple[int, int]:
        """
        Returns the appropriate window size.
        """
        width = size[0]
        height = size[1]

        if fullscreen:
            # fullscreen should be truly fullscreen
            info = pygame.display.Info()
            width = info.current_w
            height = info.current_h

        width *= HIDPI_FACTOR
        height *= HIDPI_FACTOR

        # width and height should be ints
        return int(round(width)), int(round(height))


class Renderable(object):
    """
    A renderable object to be drawn on the canvas.
    """

    def __init__(self, window: Window):
        self.window = window
        self.parent: 'Renderable' = None

    def render(self, canvas: simplegui.Canvas):
        """
        Called to render the object.
        """
        pass

    def get_bounds(self) -> Polygon:
        """
        The bounds of the rendered object.
        Used to handle click events.
        """
        raise NotImplementedError

    def is_mouse_over(self) -> bool:
        """
        Returns `true` if the mouse is over the object.
        """
        return self.get_bounds().is_inside(self.window.get_cursor_pos())

    def on_click(self, pos: Vector):
        """
        Called when object receives a click event.
        """
        pass


class RenderableParent(Renderable):
    """
    A renderable object to be drawn on the canvas, that can have children.
    """

    def __init__(self, window: Window):
        super().__init__(window)
        self.children: List[Renderable] = []

    def render(self, canvas: simplegui.Canvas):
        """
        Called to render the object and render it's children.
        """
        for child in self.children:
            child.render(canvas)

    def get_bounds(self) -> Polygon:
        raise NotImplementedError

    def on_click(self, pos: Vector):
        """
        Called when object receives a click event.
        Also checks and passes event to children.
        """
        for child in self.children:
            if child.get_bounds().is_inside(pos):
                child.on_click(pos)


class WindowHandler(RenderableParent):
    """
    A WindowHandler handles the rendering of the window and receives all events.
    """

    def __init__(self, window: Window):
        """
        Creates a window handler.
        """
        super().__init__(window)

    def render(self, canvas: simplegui.Canvas):
        """
        Called by the window draw handler every game tick.
        """
        super().render(canvas)

    def get_bounds(self) -> Polygon:
        size = self.window.get_size()
        return Polygon(
            Vector(0, 0),
            Vector(size[0], 0),
            Vector(size[0], size[1]),
            Vector(0, size[1]),
        )

    def on_click(self, pos: Vector):
        """
        Called whenever the window receives a mouse click event.
        """
        super().on_click(pos)

    def on_drag(self, pos: Vector):
        """
        Called whenever the window receives a mouse drag event.
        """
        pass

    def on_key_down(self, key: Key):
        """
        Called whenever the window receives a key down event.
        """
        pass

    def on_key_up(self, key: Key):
        """
        Called whenever the window receives a key up event.
        """
        pass