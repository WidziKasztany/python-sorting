# Ugly overly complicated code for sorting

# Data class that holds all relevant data with helper functions like Data#print()
class Data:
    # Raw data
    data : list[int] = []
    
    def __init__(self, data : list[int] = []):
        self.data = data
        
    # Prints entire data stored
    def print(self):
        print("data: [", end="")
        for i in self.data:
            print(i, end=", ")
        print("]")

    # Adds new data
    def addData(self, data : int):
        self.data.append(data)

    def getSize(self) -> int:
        return len(self.data)

    def getElement(self, index : int) -> int:
        return self.data[index]

    def swap(self, indexA : int, indexB : int):
        a = self.data[indexA]
        self.data[indexA] = self.data[indexB]
        self.data[indexB] = a

# Handles all stuff that requires user input
class InputReader:

    # Reads user input and inserts it into given Data object
    def readInto(self, data : Data, amount = 10):
        for i in range(amount):
            data.addData(int(input(f"[{i}] Enter number: ")))

# Handles everything related to sorting
class Sorter:
    # Data that sorter will be working on
    data : Data = None

    def __init__(self, data : Data):
        self.data = data

    # Sorting using some random O2 algorithm
    def sort(self):
        for i in range(self.data.getSize()):
            minIndex = i
            for j in range(i + 1, self.data.getSize()):
                if(self.data.data[j] < self.data.data[minIndex]):
                    minIndex = j

            old = self.data.data[i]
            self.data.data[i] = self.data.data[minIndex]
            self.data.data[minIndex] = old



# Main application
class App:
    data : Data = None
    reader : InputReader = None
    sorter: Sorter = None

    def __init__(self):
        self.data = Data()
        self.reader = InputReader()
        self.sorter = Sorter(self.data)

    # Executes app
    def run(self):
        print("Please insert new data")
        
        self.reader.readInto(self.data)

        self.data.print()
        self.sorter.sort()
        self.data.print()


if __name__ == "__main__":
    print("Starting app...");
    app = App()
    app.run()
