class HashMap:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        hash_key = self._hash_function(key)
        for i, (k, v) in enumerate(self.table[hash_key]):
            if k == key:
                self.table[hash_key][i] = (key, value)
                return
        self.table[hash_key].append((key, value))
        print(self.table,"put")

    def get(self, key):
        hash_key = self._hash_function(key)
        for k, v in self.table[hash_key]:
            if k == key:
                return v
        print(self.table,"get")
        return -1

    def remove(self, key):
        print(self.table)
        hash_key = self._hash_function(key)
        for i, (k, v) in enumerate(self.table[hash_key]):
            if k == key:
                del self.table[hash_key][i]
                print(self.table,"remove")
                return

# 사용 예제
hm = HashMap()
hm.put("key1", "value1")
hm.put("key2", "value2")
hm.put("key3", "value3")

print(hm.get("key1"))  # "value1" 출력
print(hm.get("key4"))  # -1 출력, 존재하지 않는 키

hm.remove("key2")
print(hm.get("key2"))  # -1 출력, 삭제된 키
