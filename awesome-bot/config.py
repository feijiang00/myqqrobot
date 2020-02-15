#import re
#COMMAND_START = ['', re.compile(r'[/!]+')] 也可以是正则表达式的类型

from nonebot.default_config import * #从 NoneBot 的默认配置中导入所有项

SUPERUSERS = {2679245726} #超级用户的qq号

COMMAND_START = {'', '/', '!', '／', '！'}

#这样可以在bot.py文件中的run函数中不再传递参数，实现了该文件（配置文件）的作用
HOTS='0.0.0.0'
PORT =8080
