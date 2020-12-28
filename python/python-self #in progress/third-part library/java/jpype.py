# python调用执行java代码
# pip install jpype1
import jpype

jvm_path = jpype.getDefaultJVMPath()

# 通过jar包来调用
jar_path = "d:/python/abc.jar"

# 启动java虚拟机
# convertStrings表示是否将java的字符串转换成python中的字符串类型
jpype.startJVM(jvm_path, "-ea", "-Djava.class.path={}".format(jar_path), convertStrings=True)

# 获取类
javaClass = jpype.JClass(Java_Class)

# 创建对象，后续发现如果是静态方法则不需要创建对象直接用类调即可
javaObj = javaClass()

# 调用方法
ret = javaObj.java_method1("params1")
print(ret)

# 关闭虚拟机
jpype.shutdownJVM()

