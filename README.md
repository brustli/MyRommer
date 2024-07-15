# Rommer 

一个能获取各类中文汉化rom元数据并自动整理的命令行工具

## 架构

Rommer/core/rom.py rom对象基类，实现对rom的各种操作
Rommer/utils 各种工具函数
...

## 实现目标

1. 解析 gba rom 的序列号，并根据序列号找到游戏对应的元数据并下载
2. 处理文件
    0. 首先判断是否是常见的压缩文件，如果是则解压
    1. 通过Python的自带库解压zip，并通过其他三方库实现对rar和7z的解压
    2. 解压出的对象（文件流）不直接写成文件，先留在内存处理
    3. 单文件或者多文件压缩包中正确找到rom文件
    4. rom类型判断，是否是预期的 rom 类型
    5. 后续根据参数决定文件流输出成原始文件还是压缩等
3. 处理得到的文件流，读取序列号或者其他可用信息
4. 通过序列号或者其他信息，找到对应的元数据
    1. 游戏封面 https://github.com/libretro-thumbnails/libretro-thumbnails
    2. 游戏信息(GBA) https://github.com/libretro/libretro-database/blob/master/metadat/no-intro/Nintendo%20-%20Game%20Boy%20Advance.dat
    3. 封面通过requests之类的爬虫手段下载下来
    4. 游戏信息通过 pyparsing 解析 dat 文件获得
5. 整理元数据，将图片和其他信息输出到指定目录或者数据库

## 注意事项
1. git提交不要带上.gitignore
2. 语法风格统一
3. 多加注释
4. 多考虑扩展性
