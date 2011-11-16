/*
 * robot.h - for Windows
 * scan screen and control the mouse
 *
 * By WangLu
 */

#ifndef ROBOT_H__
#define ROBOT_H__

#include <windows.h>

void init_robot();

::COLORREF get_pixel(int x, int y);

void mouse_move(int x, int y);
void mouse_ldown();
void mouse_lup();
void mouse_rdown();
void mouse_rup();


#endif // ROBOT_H__
