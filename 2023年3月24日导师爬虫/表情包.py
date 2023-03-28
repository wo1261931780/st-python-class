import os

from PicImageSearch.sync import SauceNAO
from PicImageSearch.model import SauceNAOResponse
from PicImageSearch.sync import BaiDu
from PicImageSearch.model import BaiDuResponse
from PicImageSearch.sync import Ascii2D
from PicImageSearch.model import Ascii2DResponse

# proxies = "http://127.0.0.1:1081"
proxies = None
url = "https://tiebapic.baidu.com/forum/w%3D580%3B/sign=d2247bd3c294a4c20a23e7233ecf19d5/024f78f0f736afc37d9da5b9f619ebc4b645125c.jpg"#搜图地址
bovw = True  # 是否使用特征检索
api_key = "a4ab3f81009b003528f7e31aed187fa32a063f58"
saucenao = SauceNAO(api_key=api_key)
resp = saucenao.search(url)
if resp.raw[0].similarity < 70:
    ascii2d = Ascii2D(bovw=bovw)
    resp = ascii2d.search(url)
    print(f"略缩图:{resp.raw[1].thumbnail}")
    print(f"原图地址:{resp.raw[1].url}")
    print(f"标题:{resp.raw[1].title}")
    print(f"作者{resp.raw[1].author}")
else:
    print(f"略缩图:{resp.raw[0].thumbnail}")
    print(f"原图地址:{resp.raw[0].url}")
    print(f"标题:{resp.raw[0].title}")
    print(f"作者{resp.raw[0].author}")
    print(f"p站id:{resp.raw[0].pixiv_id}")

os.system("pause")
