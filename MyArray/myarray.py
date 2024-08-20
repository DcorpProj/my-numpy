class MyArray:
    def __init__(self, x, y, num, j):
        self.data = self.ArrayGen(x, y, num, j)

    def ArrayGen(self, x, y, num, j):
        result = []
        for n in range(x):
            row = [num + b for b in range(y * n, y * (n + 1), j)]
            result.append(row)
        return result

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __len__(self):
        return len(self.data)

    def reshape(self, new_shape):
        if len(self.data) != prod(new_shape):
            raise ValueError(f"Cannot reshape array of size {len(self.data)} into shape {new_shape}")

        new_data = []
        for i in range(new_shape[0]):
            start = i * new_shape[1]
            end = start + new_shape[1]
            new_data.append(self.data[start:end])

        return MyArray(*new_shape, self.data[0], self.j)

    def __repr__(self):
        return str(self.data)

def prod(iterable):
    result = 1
    for x in iterable:
        result *= x
    return result
    
