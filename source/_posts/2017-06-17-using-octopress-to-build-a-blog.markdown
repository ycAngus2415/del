---
layout: post
title: "using octopress to build a blog"
date: 2017-06-17 00:14:56 +0800
comments: true
categories: 
---

# 新建一个github.io

1. 创建了域名后千万不要在其他地方引用，不然会很麻烦，push 需要pull， pull 前需要branch, 反正就是各种麻烦事，把它当做最干净的时候用来写博客可以免去很多麻烦
2. 新建后只需要ssh ， 连密码都不用，当然最好是有一个git客户端，但是千万别把github.io 从客户端放到本地，一定要从octopress。



# 更换octopress 主题，

1. 先把source 中atom.xml 和robots.txt中的nil 改成null