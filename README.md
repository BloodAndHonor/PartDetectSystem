# PartDetectSystem 

服务器：ngnix和uwsgi

## Done ##
1. 用户实体设计。
2. 图片实体设计。
3. **接收图片作为文件上传，添加到数据库。**
4. 用户与图片的关系表。 
5. 用户的登录和创建

## Doing ##
1. 用户投票的后台处理 
2. 为用户展示可用图片集合 

## 一些设计 ##
双队列设计：
1. 用户队列和系统队列
- 用户队列用于保存该用户需要投票的图片
- 系统队列用户保存需要投票的图片
