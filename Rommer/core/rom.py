class Rom:
    """
    Rom 基类， 定义获取 serial，文件名称，加解压，计算 hash 等
    """

    def __init__(self, rom_path):
        pass

    def get_serial(self):
        pass

    def set_cn_name(self, cn_name):
        pass

    def get_cn_name(self):
        pass

    def set_en_name(self, en_name):
        pass

    def get_en_name(self):
        pass

    def calc_hash(self):
        "crc32, md5, sha1"
        pass

    def is_archive(self):
        """判断是否为压缩文件"""
        pass

    def load(self):
        """加载内容"""
        if self.is_archive():
            self.load_archive()
        else:
            self.load_file()

    def load_file(self):
        pass

    def load_archive(self):
        pass


class GBA(Rom):
    pass


class NDS(Rom):
    pass
