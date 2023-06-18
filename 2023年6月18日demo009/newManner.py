from esda.moran import Moran
from libpysal.weights.contiguity import Queen

# w = Queen.from_dataframe(gdf)
# moran = Moran(y, w)
# moran.I
import numpy as np
from array import array

# 创建一个ndarray
ndarr = np.array([1, 2, 3, 4, 5], dtype=np.int32)

# 将ndarray保存到二进制文件
ndarr.tofile('data.bin')

# 定义array.pyi文件
with open('array.pyi', 'w') as f:
    f.write('from typing import List\n')
    f.write('\n')
    f.write('def array(obj: List[()]) -> None:\n')
    f.write('    ...\n')
