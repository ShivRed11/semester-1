# Reference solution (rewritten after original work was lost)
# Week 1.5, Session 2: Task 5

class Dataset:
    """
    A numeric dataset, loaded from a file.
    """

    def __init__(self, filename=None):
        """
        Creates a Dataset containing data from the specified file.

        If no file is specified, an empty Dataset is created.
        """
        self.data = []
        if filename:
            self.load_data(filename)

    def load_data(self, filename):
        """
        Loads data from the specified file into this Dataset.

        Any existing data will be deleted.
        """
        self.data.clear()                  # remove any existing values
        with open(filename, "r") as infile:
            for line in infile:
                line = line.strip()
                if line:                   # skip blank lines
                    self.data.append(float(line))

    def __len__(self):
        """
        Returns the size of this Dataset.
        """
        return len(self.data)              # lets us write len(dataset)

    def __getitem__(self, index):
        """
        Returns the value at the specified position in this Dataset.
        """
        # lets us write dataset[i] - and also makes 'for value in dataset'
        # work, because Python tries index 0, 1, 2... until IndexError
        return self.data[index]

    def mean(self):
        """
        Returns the arithmetic mean of the values in this Dataset.
        """
        return sum(self.data) / len(self.data)

    def median(self):
        """
        Returns the median of the values in this Dataset.
        """
        # sorted() makes a NEW sorted list, so self.data keeps its order
        sorted_data = sorted(self.data)
        size = len(sorted_data)
        middle = size // 2
        if size % 2 == 1:
            return sorted_data[middle]            # odd: the middle value
        # even: mean of the two middle values
        return (sorted_data[middle - 1] + sorted_data[middle]) / 2
