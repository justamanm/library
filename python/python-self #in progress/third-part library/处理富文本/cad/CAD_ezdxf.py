# pip install ezdxf
import ezdxf

# 画出的结果：https://pic4.zhimg.com/80/v2-8e81fdd12feda880c045f23ac9ea5f43_720w.jpg
dwg = ezdxf.new('R2007')
msp = dwg.modelspace()
d = 40.
n = int(40 / 1.5)

delta = d / n

start = (100, 100)

msp.add_circle(start, 20)

for x in range(-n, n):
    for y in range(-n, n):
        if y & 1:
            offset = 0.5
        else:
            offset = 0
        rx = ((x + offset)**2 + y**2)**0.5
        if rx <= (n/2 + 0.1):
            r = 0.35 # (0.25 * delta * (n/2 - rx) / (n/2) + 0.15 * delta)
            msp.add_circle((start[0] + (x + offset) * delta, start[1] + y * delta), r)

dwg.saveas('speaker_hole.dxf')