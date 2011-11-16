#include <windows.h>

// Globals
HDC hDC = NULL; // screen hdc
int screenX, screenY;
INPUT input;

COLORREF get_pixel(int x, int y)
{
	return ::GetPixel(hDC, x, y);
}

void send_mouse_event(DWORD flag, int x=0, int y=0)
{
	input.type = INPUT_MOUSE;
	input.mi.dwFlags = flag;
	input.mi.dx = x;
	input.mi.dy = y;
	input.mi.time = 0;

	::SendInput(1, &input, sizeof(input));
}

void mouse_move(int x, int y)
{
	::POINT p;
	::GetCursorPos(&p);
	send_mouse_event(MOUSEEVENTF_MOVE | MOUSEEVENTF_ABSOLUTE, x*65536/screenX, y*65536/screenY);
}

void mouse_ldown()
{
	send_mouse_event(MOUSEEVENTF_LEFTDOWN);
}

void mouse_lup()
{
	send_mouse_event(MOUSEEVENTF_LEFTUP);
}

void mouse_rdown()
{
	send_mouse_event(MOUSEEVENTF_RIGHTDOWN);
}

void mouse_rup()
{
	send_mouse_event(MOUSEEVENTF_RIGHTUP);
}

void init_robot()
{
	hDC = ::GetDC(NULL);
	screenX = ::GetSystemMetrics(SM_CXSCREEN);
	screenY = ::GetSystemMetrics(SM_CYSCREEN);
}
