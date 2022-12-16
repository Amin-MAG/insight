# Basic Graphic Programming in C++

<aside>
💡 Introduction to C++ graphics: Graphics in C++ is defined to create a graphic model like creating different shapes and adding colors to it. It can be done in the C++ using your terminal or command prompt or you can download DevC++ compiler to create graphic programs. For terminal you need to add the graphics. h library to you GCC compiler. We can draw the circle, line, eclipse, and other geometric shapes too

</aside>

### What is graphics.h exactly?

**graphics.h** library is used to include and facilitate graphical operations in program. graphics.h functions can be used to draw different shapes, display text in different fonts, change colors and many more. Using functions of graphics.h you can make graphics programs, animations, projects and games. You can draw circles, lines, rectangles, bars and many other geometrical figures. You can change their colors using the available functions and fill them.

### **As mentioned earlier the header file “graphics.h” contains functions which some of them are described below:**

- `int initwindow (int width, int height, const char* title, int left, int top)`
    
    In order to generate a Viewport or a window for drawing graphics shapes, we should use a function called initwindow()
    
    - **int width:** width of the created window in pixels (integer type)
    - **int height:** height of the created window in pixels (integer type)
    - **const char* title: t**he title of the generated window which is a string type with dynamic and fixed memory allocation
    - **int left:** the horizontal (X) position of the window on the screen (integer type)
    - **int top:** the longitudinal (Y) position of the window on the screen (integer type)
        
        `initwindow (400 ,400, "Viewport" ,300 ,200);`
        
- `putpixel(int x, int y)`
    
    This function is used to draw a dot in (x, y) position.
    
- `line(int x1, int y1, int x2, int y2);`
    
    Line function is used to draw a line from a point (x1, y1) to point (x2, y2). (x1, y1) and (x2, y2) are end points of the line.
    
- `circle(int x, int y, int radius);`
    
    Circle function is used to draw a circle with center (x, y) and radius specified in the third parameter.
    
- `rectangle (int left, int top, int right, int bottom);`
    
    To create a rectangle, you have to pass the four parameters in this function. The two parameters represent the left and top upper left corner. Similarly, the right bottom parameter represents the lower right corner of the rectangle.
    
- `outtextxy(int x, int y, char *string);`
    
    This function displays the text or string at a specified point (x, y) on the screen.
    .
    
- `setcolor(int color);`
    
    setcolor sets the current drawing color to a new color. In graphics, each color is assigned a number. Total number of colors available are 16. Number of available colors depends on current graphics mode and driver. For example, setcolor(RED) or setcolor(4) changes the current drawing color to RED. (default drawing color is WHITE) The Colors table is given below:
    
    | Color | Int values |
    | --- | --- |
    | BLACK | 0 |
    | BLUE | 1 |
    | GREEN | 2 |
    | CYAN | 3 |
    | RED | 4 |
    | MAGENTA | 5 |
    | BROWN | 6 |
    | LIGHTGRAY | 7 |
    | DARKGRAY | 8 |
    | LIGHTBLUE | 9 |
    | LIGHTGREEN | 10 |
    | LIGHTCYAN | 11 |
    | LIGHRED | 12 |
    | LIGHTMAGENTA | 13 |
    | YELLOW | 14 |
    | WHITE | 15 |
- `setfillstyle(int pattern, int color);`
    
    This ****function sets the current fill pattern and fill color. The table of colors has already mentioned; below is the table showing INT VALUES corresponding to Patterns:
    
    | Pattern | Int values |
    | --- | --- |
    | EMPTY_FILL | 0 |
    | SOLID_FILL | 1 |
    | LINE_FILL | 2 |
    | LTSLASH_FILL | 3 |
    | SLASH_FILL | 4 |
    | BKSLASH_FILL | 5 |
    | LTBKSLASH_FILL | 6 |
    | HATCH_FILL | 7 |
    | XHATCH_FILL | 8 |
    | INTERLEAVE_FILL | 9 |
    | WIDE_DOT_FILL  | 10 |
    | CLOSE_DOT_FILL | 11 |
    | USER_FILL | 12 |