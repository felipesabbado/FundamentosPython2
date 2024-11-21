from sys import path
path.append('../packages')

# import extra.iota
# print(extra.iota.funI())

from extra.iota import funI
print(funI())

import extra.good.best.sigma as sigma
import extra.good.alpha as alpha
from extra.good.best.tau import funT

print(sigma.funS())
print(funT())
print(alpha.funA())
