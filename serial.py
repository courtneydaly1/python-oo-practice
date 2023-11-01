"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start =0):
        """Make a new generator and start at 0"""
        self.start = self.next = start

    def __repr__(self):
        """str explains what the start value and next values are"""
        return f"<SerialGenerator start ={self.start} and next ={self.next}"
    
    def generate(self):
        """Return next number in serial count"""
        self.next += 1
        return self.next -1
    
    def reset(self):
        """resets the function to start at 0"""
        self.next = self.start


