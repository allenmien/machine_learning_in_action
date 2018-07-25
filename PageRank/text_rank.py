# -*-coding:utf-8-*-
"""
@Time   : 2018/7/25 12:03
@Author : Mark
@File   : text_rank.py
"""
import sys

from pygraph.classes.digraph import digraph

reload(sys)
sys.setdefaultencoding('utf-8')


class PRIterator:
    __doc__ = '''计算一张图中的PR值'''

    def __init__(self, dg):
        self.damping_factor = 0.85  # 阻尼系数,即α
        self.max_iterations = 100  # 最大迭代次数
        self.min_delta = 0.00001  # 确定迭代是否结束的参数,即ϵ
        self.graph = dg

    def page_rank(self):
        #  先将图中没有出链的节点改为对所有节点都有出链
        for node in self.graph.nodes():
            if len(self.graph.neighbors(node)) == 0:
                for node2 in self.graph.nodes():
                    digraph.add_edge(self.graph, (node, node2))

        nodes = self.graph.nodes()
        graph_size = len(nodes)

        if graph_size == 0:
            return {}
        page_rank = dict.fromkeys(nodes, 1.0 / graph_size)  # 给每个节点赋予初始的PR值
        damping_value = (
                                1.0 - self.damping_factor) / graph_size  # 公式中的(1−α)/N部分

        flag = False
        for i in range(self.max_iterations):
            change = 0
            for node in nodes:
                rank = 0
                for incident_page in self.graph.incidents(node):  # 遍历所有“入射”的页面
                    rank += self.damping_factor * (
                            page_rank[incident_page] / len(
                        self.graph.neighbors(incident_page)))
                rank += damping_value
                change += abs(page_rank[node] - rank)  # 绝对值
                page_rank[node] = rank

            print("This is NO.%s iteration" % (i + 1))

            if change < self.min_delta:
                flag = True
                break
        if flag:
            print("finished in %s iterations!" % node)
        else:
            print("finished out of 100 iterations!")
        return page_rank


if __name__ == '__main__':
    dg = digraph()
    words_dict = {
        u"开发": [u"专业", u"程序员", u"维护", u"英文", u"程序", u"人员"],
        u"软件": [u"程序员", u"分为", u"界限", u"高级", u"中国", u"特别", u"人员"],
        u"程序员": [u"开发", u"软件", u"分析员", u"维护", u"系统", u"项目", u"经理", u"分为", u"英文", u"程序", u"专业", u"设计", u"高级", u"人员",
                 u"中国"],
        u"分析员": [u"程序员", u"系统", u"项目", u"经理", u"高级"],
        u"维护": [u"专业", u"开发", u"程序员", u"分为", u"英文", u"程序", u"人员"],
        u"系统": [u"程序员", u"分析员", u"项目", u"经理", u"分为", u"高级"],
        u"项目": [u"程序员", u"分析员", u"系统", u"经理", u"高级"],
        u"经理": [u"程序员", u"分析员", u"系统", u"项目"],
        u"分为": [u"专业", u"软件", u"设计", u"程序员", u"维护", u"系统", u"高级", u"程序", u"中国", u"特别", u"人员"],
        u"英文": [u"专业", u"开发", u"程序员", u"维护", u"程序"],
        u"程序": [u"专业", u"开发", u"设计", u"程序员", u"编码", u"维护", u"界限", u"分为", u"英文", u"特别", u"人员"],
        u"特别": [u"软件", u"编码", u"分为", u"界限", u"程序", u"中国", u"人员"],
        u"专业": [u"开发", u"程序员", u"维护", u"分为", u"英文", u"程序", u"人员"],
        u"设计": [u"程序员", u"编码", u"分为", u"程序", u"人员"],
        u"编码": [u"设计", u"界限", u"程序", u"中国", u"特别", u"人员"],
        u"界限": [u"软件", u"编码", u"程序", u"中国", u"特别", u"人员"],
        u"高级": [u"程序员", u"软件", u"分析员", u"系统", u"项目", u"分为", u"人员"],
        u"中国": [u"程序员", u"软件", u"编码", u"分为", u"界限", u"特别", u"人员"],
        u"人员": [u"开发", u"程序员", u"软件", u"维护", u"分为", u"程序", u"特别", u"专业", u"设计", u"编码", u"界限", u"高级", u"中国"]
    }

    words_key_list = list()
    for k, v in words_dict.iteritems():
        words_key_list.append(k)
    dg.add_nodes(words_key_list)

    for k, v in words_dict.iteritems():
        for i in v:
            dg.add_edge((k, i))

    pr = PRIterator(dg)
    page_ranks = pr.page_rank()

    sort_text_rank = sorted(page_ranks.items(), key=lambda d: d[1], reverse=True)
    for k, v in sort_text_rank:
        print str(k) + u":" + str(v)
