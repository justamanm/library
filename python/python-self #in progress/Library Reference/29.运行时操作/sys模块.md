### sys.exit()

- 仅仅抛出一个异常

- 即如果对异常进行捕获，则程序不会退出

```python
import sys

try:
    sys.exit(1)
    # a = 1
except:
    # 注：如果是except Exception as e，则except中的语句不会被执行
    # print(str(e))
    print('Program is dead.')
finally:
    print('clean-up')
    
a = 1
print(a)

------输出-----
Program is dead.
clean-up
1
```

在导包时，子模块中调用了sys.exit()

- 主程序就会结束
- 因为其实sys.exit()是被导入到主程序中的，所以主程序结束执行



如果不主动调用sys.exit()

- 0：正常结束
- 负数：程序报错导致执行失败
- 正数：exe本身错误返回正数，如路径不正确

sys.exit(num)  num取[0,255]

> import sys
> sys.exit(n)          // n is the value returned to shell
>
> Response to your response:
> The range of return value is [0, 255] in shell, and any number that exceeds this range will be converted as                 n%256
> Negative values are reserved for errors of program running.
>
> [python脚本如何 返回值给调用它的shell？ - 大周的回答 - 知乎](https://www.zhihu.com/question/22859506/answer/22883534)



### sys.frozen和sys._MEIPASS

- 在python脚本中时，没有frozen和_MEIPASS属性
- 在打包exe中，二者均为True
- 所以，可以用来判断是否在打包程序中

示例：

```python
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    print('running in a PyInstaller bundle')
else:
    print('running in a normal Python process')
```



### sys.argv[0]

脚本执行

- 主程序：所执行的脚本名称，可能是路径，也可能是名称，取决于执行命令
- 子模块中：sys.argv[0]是主程序的路径，与主程序中获取的是一样的

打包

- 子模块中sys.argv[0]同样是主程序的路径
- 即无论exe在哪个目录执行，均为主程序的路径

综上：sys.argv[0]无论在主程序还是在子模型中，均获取的是主程序路径，子模块中的路径可以据此进行定位（也可以使用abspath定位，但仅限于子模块，主程序中的abspath会错）





