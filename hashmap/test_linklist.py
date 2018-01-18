from hashmap.linklist import LinkList
from hashmap.node import Node


class TestLinkList:

    def test_add_node_list(self):
        test_list = LinkList()
        test_list.add_node("a", "apple")
        test_list.add_node("z", "zebra")
        assert test_list.first_node.key == "a"
        assert test_list.last_node.key == "z"
        assert test_list.first_node.value == "apple"
        assert test_list.last_node.value == "zebra"

    def test_append_new_node_to_list(self):
        test_node = Node("d", 5)
        test_list = LinkList()
        test_list.append_new_node_to_list(test_node)

    def test_contains_value(self):
        test_list = LinkList()
        test_list.add_node("a", "apple")
        assert True == test_list.contains_value("apple")

    def test_contains_key(self):
        test_list = LinkList()
        test_list.add_node("a", "aaa")
        assert True == test_list.contains_key("a")

    def test_delete_node_with_key(self):
        test_list = LinkList()
        test_list.add_node("z", "zebra")
        test_list.delete_node_with_key("z")
        assert False == test_list.contains_key("z")
        assert False == test_list.contains_value("zebra")

    def test_clear(self):
        test_list = LinkList()
        test_list.add_node("a", "apple")
        test_list.clear()
        assert test_list.first_node == None
        assert test_list.last_node == None
