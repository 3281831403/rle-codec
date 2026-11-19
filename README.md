# RLE 与变长整数：游程、差分与解码

补丁包解压后错位：游程没有合并相邻相同值，解码没有按计数展开，变长整数没有按 7 位分组，差分首项被重复减，空输入崩溃，损坏字节没有停止，压缩比按元素数而不是字节，批量编解码只成功一半。

## 目录结构

```
README.md
conftest.py
.gitignore
codec/__init__.py
codec/rle.py
tests/test_rle.py
```

## 当前状态

`codec/rle.py` 中所有函数只保留签名与文档字符串，函数体统一
`raise NotImplementedError`。`tests/test_rle.py` 有 15 个参数化用例，
初始全部失败。

## 需要修复的 10 个问题

1. 游程合并
2. 按计数解码
3. 变长整数 7 位分组
4. 差分首项保留
5. 空输入处理
6. 损坏字节停止
7. 压缩比按字节

## 验收

```bash
python -m pytest -q
```

初始应得到 `15 failed`，且没有 collection error。实现 `codec/rle.py`
后 15 条用例应全部通过。
