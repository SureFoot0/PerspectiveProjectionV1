# PerspectiveProjectionV1
Mapping 3D objects onto a 2D screen

3D objects can be plotted on 3 axes. But a computer screen only has 2 axes (obviously). So how can you draw a 3D object on a screen? The easiest way to do this is using "weak" perspective projection. 

You can create mathematically similar, right-angled triangles using this method by drawing a line from one of the corners of the object to the camera's "position". Then, you can make a right-angled triangle by adding two more lines perpendicular to each other. If you add a line in the middle, you can make 2 triangles (one stopping at the screen and the other at the point). These two triangles are mathematically similar with can give you a coordinate relative to the screen which can (somewhat) acurately plot a point.

Wikipedia link for 3D projection which includes "weak" perspective projection: https://en.wikipedia.org/wiki/3D_projection#:~:text=Perspective%20projection%20or%20perspective%20transformation,appear%20smaller%20than%20nearer%20objects.

Diagram of "weak" perspective projection: ![image](https://user-images.githubusercontent.com/63339089/205496310-9f3939dd-916a-4164-a78e-1e64f5938c4b.png)
