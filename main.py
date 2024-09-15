import glfw
import glfw.GLFW as GLFW_CONSTANTS
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

def create_shader_program(vertex_filepath: str, fragment_filepath: str) -> int:
    vertex_module = create_shader_module(vertex_filepath, GL_VERTEX_SHADER)
    fragment_module = create_shader_module(fragment_filepath, GL_FRAGMENT_SHADER)
    
    shader = compileProgram(vertex_module, fragment_module)
    
    glDeleteShader(vertex_module)
    glDeleteShader(fragment_module)
    
    return shader

def create_shader_module(filepath: str, module_type: int) -> int:
    source_code = ""
    with open(filepath, "r") as file:
        source_code = file.readlines()
    
    return compileShader(source_code, module_type)
    
class App:
    
    def __init__(self):
        self.initialize_glfw()
        self.initialize_opengl()
        
    def initialize_glfw(self) -> None:
        glfw.init()
        glfw.window_hint(
            GLFW_CONSTANTS.GLFW_OPENGL_PROFILE,
            GLFW_CONSTANTS.GLFW_OPENGL_CORE_PROFILE)
        glfw.window_hint(GLFW_CONSTANTS.GLFW_CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(GLFW_CONSTANTS.GLFW_CONTEXT_VERSION_MINOR, 3)
        glfw.window_hint(GLFW_CONSTANTS.GLFW_OPENGL_FORWARD_COMPAT, GLFW_CONSTANTS.GLFW_TRUE)
        
        self.window = glfw.create_window(SCREEN_WIDTH, SCREEN_HEIGHT, "My OpenGL Context", None, None)
        glfw.make_context_current(self.window)
        
    def initialize_opengl(self) -> None:
        glClearColor(0.1, 0.2, 0.4, 1.0)
        self.shader = create_shader_program("shaders/vertex.glsl", "shaders/fragment.glsl")
        
        
    def run(self):
        
        while(not glfw.window_should_close(self.window)):
            
            if glfw.get_key(self.window, GLFW_CONSTANTS.GLFW_KEY_ESCAPE) == GLFW_CONSTANTS.GLFW_PRESS:
                break
            glfw.poll_events()
            
            glClear(GL_COLOR_BUFFER_BIT)
            glfw.swap_buffers(self.window)
    
    def quit(self):
        
        glfw.destroy_window(self.window)
        glfw.terminate()
    
my_app = App()
my_app.run()
my_app.quit()