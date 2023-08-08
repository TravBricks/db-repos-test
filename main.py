# importing module
import sys
 
# appending a path
sys.path.append('article')

# importing required module
import myexample
from myexample import MyExample
 
# accessing its content
MyExample.method_in()
myexample.method_out()