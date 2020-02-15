from os import path

import nonebot

import config

if __name__ == '__main__':
    nonebot.init(config) #将config作为配置对象传给noneot.init函数
    
    #加载插件
    nonebot.load_plugins(
         path.join(path.dirname(__file__), 'awesome', 'plugins'),
        'awesome.plugins'
    )
    nonebot.load_builtin_plugins() #加载notebot内置的插件
    
    nonebot.run() #在地址127.0.0.1:8080运行notebot
