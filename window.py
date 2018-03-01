from typing import Tuple

from constants import PYGAME_HACKS, WINDOW_SIZE2, Key
from util import simplegui, pygame


class Window(object):
    """
    The game window, only one may be created.
    """

    def __init__(self, title: str, size: Tuple[int, int], controls: bool = False, fullscreen: bool = False):
        """
        Creates a new game window.

        :param title: str
        :param size: (int, int)
        :param controls: bool
        """
        self.handler = WindowHandler(self)  # A noop window handler.

        self.controls = controls
        self._show_control_panel(controls)  # Set control panel visibility.
        self.fullscreen = self._set_fullscreen(fullscreen)  # Set fullscreen status.

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

        :return: None
        """
        self.frame.start()

    def destroy(self):
        """
        Destroys the window.

        :return: None
        """
        self.frame.stop()

    def _render(self, canvas: simplegui.Canvas):
        """
        Called by the window draw handler every game tick.
        Passes the render to the handler.

        :param canvas: Canvas
        :return: None
        """
        return self.handler.render(canvas)

    def _on_click(self, pos: Tuple[int, int]):
        """
        Called whenever the window receives a mouse click event.
        Passes the event to the handler.

        :param pos: (int, int)
        :return: None
        """
        return self.handler.on_click(pos)

    def _on_drag(self, pos: Tuple[int, int]):
        """
        Called whenever the window receives a mouse drag event.
        Passes the event to the handler.

        :param pos: (int, int)
        :return: None
        """
        return self.handler.on_drag(pos)

    def _on_key_down(self, key: int):
        """
        Called whenever the window receives a key down event.
        Passes the event to the handler.

        :param key: int
        :return: None
        """
        # Escape out of fullscreen mode
        if self.fullscreen and key == Key.ESCAPE:
            self.destroy()

        return self.handler.on_key_down(Key(key))

    def _on_key_up(self, key: int):
        """
        Called whenever the window receives a key up event.
        Passes the event to the handler.

        :param key: int
        :return: None
        """
        return self.handler.on_key_up(Key(key))

    # Pygame

    # noinspection PyMethodMayBeStatic
    def get_title(self) -> str:
        """
        Returns the title of the window.

        :return: str
        """
        if not PYGAME_HACKS:
            return self.title

        return pygame.display.get_caption()

    # noinspection PyMethodMayBeStatic
    def set_title(self, title: str):
        """
        Sets the title of the window.
        """
        if not PYGAME_HACKS:
            return

        return pygame.display.set_caption(title)

    # noinspection PyProtectedMember
    def _create_frame(self) -> simplegui.Frame:
        """
        Creates the window frame, magic may or may not come included.
        """
        frame = None

        if self.controls:
            frame = simplegui.create_frame(self.title, self.width, self.height)
        elif not PYGAME_HACKS:
            frame = simplegui.create_frame(self.title, self.width, self.height, control_width=0)

        if frame is not None:
            # Fix visual buffer issue in pygame implementation of simplegui (ignoring PYGAME_HACKS = False).
            if pygame is not None:
                pygame.display.flip()

            return frame

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
    def _show_control_panel(value: bool):
        """
        Attempts to hide the control panel.
        """
        if not PYGAME_HACKS:
            return

        simplegui.Frame._hide_controlpanel = not value

    @staticmethod
    def _set_fullscreen(value: bool) -> bool:
        """
        Attempts to set the fullscreen status.
        """
        if not PYGAME_HACKS:
            return False

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
        :param size: (int, int)
        :param fullscreen: bool
        :return: (int, int)
        """
        width, height = size[0], size[1]
        if not PYGAME_HACKS:
            if width == -1 or height == -1:
                width, height = WINDOW_SIZE2
            return int(round(width)), int(round(height))

        if fullscreen:
            # fullscreen should be truly fullscreen
            info = pygame.display.Info()
            width, height = info.current_w, info.current_h
        elif width == -1 or height == -1:
            # if either width or height are -1 use a ratio of the monitor dimensions
            info = pygame.display.Info()
            width, height = info.current_w, info.current_h

            width *= 0.66
            height *= 0.66

        # width and height should be ints
        return int(round(width)), int(round(height))


class WindowHandler(object):
    """
    A WindowHandler handles the rendering of the window and receives all events.
    """

    def __init__(self, window: Window):
        """
        Creates a window handler.

        :param window: Window
        """
        self.window = window

    def render(self, canvas: simplegui.Canvas):
        """
        Called by the window draw handler every game tick.

        :param canvas: Canvas
        :return: None
        """
        pass

    def on_click(self, pos: Tuple[int, int]):
        """
        Called whenever the window receives a mouse click event.

        :param pos: (int, int)
        :return: None
        """
        pass

    def on_drag(self, pos: Tuple[int, int]):
        """
        Called whenever the window receives a mouse drag event.

        :param pos: (int, int)
        :return: None
        """
        pass

    def on_key_down(self, key: Key):
        """
        Called whenever the window receives a key down event.

        :param key: int
        :return: None
        """
        pass

    def on_key_up(self, key: Key):
        """
        Called whenever the window receives a key up event.

        :param key: int
        :return: None
        """
        pass


class Renderable(object):
    """
    A renderable object to be drawn on the canvas.
    """

    def render(self, canvas: simplegui.Canvas):
        """
        Called to render the object.

        :param canvas: Canvas
        :return: None
        """
        pass
