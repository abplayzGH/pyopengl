#version 330 core

const vec3[3] colors = vec3[](
    vec3(1.0, 0.0, 0.0),
    vec3(0.0, 1.0, 0.0),
    vec3(0.0, 0.0, 1.0)
);

layout (location = 0) in vec3 vertexPosition;
layout (location = 1) in uint vertexColor;

out vec3 fragmentColor;

void main()
{
    gl_Position = vec4(vertexPosition, 1.0);
    fragmentColor = colors[vertexColor];
}