import module1
import module1 as m1
import module2
import module2 as m2

from module1 import hi as hi1
from module2 import hi as hi2

module1.hi()
module2.hi()

m1.hi()
m2.hi()

hi1()
hi2()