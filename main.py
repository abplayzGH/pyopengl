from config import *
import mesh_factory
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
        # self.triangle_buffers, self.triangle_vao = mesh_factory.build_triangle_mesh()
        self.triangle_vbo, self.triangle_vao = mesh_factory.build_triangle_mesh2()
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
        # glDeleteBuffers(len(self.triangle_buffers), self.triangle_buffers)
        glDeleteBuffers(1, self.triangle_vbo)
        glDeleteVertexArrays(1, (self.triangle_vao,))
        glDeleteProgram(self.shader)
        glfw.destroy_window(self.window)
        glfw.terminate()
    
my_app = App()
my_app.run()
my_app.quit()