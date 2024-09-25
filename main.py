import glfw
import glfw.GLFW as GLFW_CONSTANTS
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np


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
    
def build_triangle_mesh() -> tuple[tuple[int], int]:
    position_data = np.array(
        (-0.75, -0.75, 0.0,
         0.75, -0.75, 0.0,
         0.0, 0.75, 0.0), dtype = np.float32)
    
    color_data = np.array(
        (0, 1, 2), dtype = np.uint)
    
    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)
    
    #position buffer
    position_buffer = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, position_buffer)
    glBufferData(GL_ARRAY_BUFFER, position_data.nbytes, position_data, GL_STATIC_DRAW)
    attribute_index = 0
    size = 3
    stride = 12
    offset = 0
    glVertexAttribPointer(attribute_index, size, GL_FLOAT, GL_FALSE, stride, ctypes.c_void_p(offset))
    glEnableVertexAttribArray(attribute_index) 
    
    #Color buffer
    color_buffer = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, color_buffer)
    glBufferData(GL_ARRAY_BUFFER, color_data.nbytes, color_data, GL_STATIC_DRAW)
    attribute_index = 1
    size = 1
    stride = 4
    offset = 0
    glVertexAttribIPointer(attribute_index, size, GL_UNSIGNED_INT, stride, ctypes.c_void_p(offset))
    glEnableVertexAttribArray(attribute_index) 
    
    return ((position_buffer, color_buffer), vao)
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
        self.triangle_buffers, self.triangle_vao = build_triangle_mesh()
        self.shader = create_shader_program("shaders/vertex.glsl", "shaders/fragment.glsl")
        
        
    def run(self):
        
        while(not glfw.window_should_close(self.window)):
            
            if glfw.get_key(self.window, GLFW_CONSTANTS.GLFW_KEY_ESCAPE) == GLFW_CONSTANTS.GLFW_PRESS:
                break
            glfw.poll_events()
            
            glClear(GL_COLOR_BUFFER_BIT)
            glUseProgram(self.shader)
            glBindVertexArray(self.triangle_vao)
            glDrawArrays(GL_TRIANGLES, 0, 3)
            glfw.swap_buffers(self.window)
    
    def quit(self):
        glDeleteBuffers(len(self.triangle_buffers), self.triangle_buffers)
        glDeleteVertexArrays(1, (self.triangle_vao,))
        glDeleteProgram(self.shader)
        glfw.destroy_window(self.window)
        glfw.terminate()
    
my_app = App()
my_app.run()
my_app.quit()