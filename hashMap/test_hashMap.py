from hashMap.hashmap import HashMap


class TestHashMap:

    def test_puts_key_value_in_hashmap(self):
        test_map = HashMap()
        test_map.put("a", "Apple")
        assert test_map.get("a") == "Apple"

    def test_gets_values_from_hashmap(self):
        test_map = HashMap()
        test_map.put("a", "Apple")
        test_map.put("b", 2)
        test_map.put("z", "Zebra")
        assert test_map.get("a") == "Apple"
        assert test_map.get("b") == 2
        assert test_map.get("z") == "Zebra"

    def test_updates_values_from_hashmap(self):
        test_map = HashMap()
        test_map.put("a", "Apple")
        assert test_map.get("a") == "Apple"
        test_map.put("a", 2)
        assert test_map.get("a") == 2

    def test_removes_value_from_hashmap(self):
        test_map = HashMap()
        test_map.put("a", "apple")
        test_map.remove("a")
        assert False == test_map.contains("a")

    def test_clears_all_values_from_hashmap(self):
        test_map = HashMap()
        test_map.put("a", "apple")
        test_map.put("b", "ball")
        test_map.put("c", "cat")
        test_map.clear()
        assert test_map.size() == 0

    def test_increases_hashmap_capacity_underload_ratio_is_2(self):
        size = 100
        test_map = HashMap(size)
        for num in range(125):
            test_map.put(num, "test")
        assert len(test_map._buckets) == 200

