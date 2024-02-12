class lst_:
    def __iter__(self):
        self.data = ["ali", "mohsen", "reza", "sara", "shabnam"]
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.data):
            n = self.n
            self.n += 1
            return f"Mr. {self.data[n]}"
        else:
            raise StopIteration

    def __len__(self):
        return len(self.data)

    def __index__(self, item):
        pass

    def find(self, item):
        pass


myclass = lst_()
myIter = iter(myclass)


for item in myIter:
    print(item)
