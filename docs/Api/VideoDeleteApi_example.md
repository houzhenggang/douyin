###VideoDeleteApi_video_delete_post
```python
from __future__ import print_function
import time
import douyin.open.video_delete
from douyin.open.video_delete.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = douyin.open.video_delete.VideoDeleteApi()
open_id = 'ba253642-0590-40bc-9bdf-9a1334b94059' # str | 通过/oauth/access_token/获取，用户唯一标志
access_token = 'act.1d1021d2aee3d41fee2d2add43456badMFZnrhFhfWotu3Ecuiuka27L56lr' # str | 调用/oauth/access_token/生成的token，此token需要用户授权。
body = douyin/open/video_delete.VideoDeleteBody() # VideoDeleteBody |  (optional)

try:
    # 删除授权用户发布的视频
    api_response = api_instance.video_delete_post(open_id, access_token, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideoDeleteApi->video_delete_post: %s\n" % e)
```
