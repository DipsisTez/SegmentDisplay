# Segment display simulation - display.py

class SegmentDisplay:
    def __init__(self):
        # Initialize the display matrix and display buffer
        self.MatrixDisplay = [[0]*5 for _ in range(9)]
        self.bufferDisplay = []

    def setTopSegment(self, signal):
        """Sets the top segment of the display"""
        self.MatrixDisplay[0] = [0, signal, signal, signal, 0]

    def setUpperRightSegment(self, signal):
        """Sets the upper right segment of the display"""
        for i in range(1, 4):
            self.MatrixDisplay[i][4] = signal

    def setLowerRightSegment(self, signal):
        """Sets the lower right segment of the display"""
        for i in range(5, 8):
            self.MatrixDisplay[i][4] = signal

    def setBottomSegment(self, signal):
        """Sets the bottom segment of the display"""
        self.MatrixDisplay[-1] = [0, signal, signal, signal, 0]

    def setLowerLeftSegment(self, signal):
        """Sets the lower left segment of the display"""
        for i in range(5, 8):
            self.MatrixDisplay[i][0] = signal

    def setUpperLeftSegment(self, signal):
        """Sets the upper left segment of the display"""
        for i in range(1, 4):
            self.MatrixDisplay[i][0] = signal

    def setMiddleSegment(self, signal):
        """Sets the middle segment of the display"""
        self.MatrixDisplay[4] = [0, signal, signal, signal, 0]

    def clearDisplayBuffer(self):
        """Clears the display buffer"""
        self.bufferDisplay = []

    def renderDisplay(self):
        """Renders the current state of the display into the buffer"""
        self.clearDisplayBuffer()
        for i in range(len(self.MatrixDisplay)):
            for j in range(len(self.MatrixDisplay[i])):
                self.bufferDisplay.append('#' if self.MatrixDisplay[i][j] else ' ')
            self.bufferDisplay.append('\n')

    def outputDisplayBuffer(self):
        """Outputs the contents of the display buffer"""
        print(''.join(self.bufferDisplay))

    def getMatrixDisplay(self):
        return self.MatrixDisplay

    def renderDoubleDisplay(self, TwoDisplay):
        """Renders the current state of the display into the double buffer"""
        slinkBuffer = []
        for i in range(len(self.MatrixDisplay)):
            for j in range(len(self.MatrixDisplay[i])):
                slinkBuffer.append('#' if self.MatrixDisplay[i][j] else ' ')

            slinkBuffer.append(' ')
            for j in range(len(TwoDisplay[i])):
                slinkBuffer.append('#' if TwoDisplay[i][j] else ' ')
            slinkBuffer.append('\n')

        print(''.join(slinkBuffer))

    def setState(self, arrayState):
        a,b,c,d,e,f,g = arrayState
        self.setTopSegment(a)
        self.setUpperRightSegment(b)
        self.setLowerRightSegment(c)
        self.setBottomSegment(d)
        self.setLowerLeftSegment(e)
        self.setUpperLeftSegment(f)
        self.setMiddleSegment(g)

    def decoder(self,input_data):
        d3,d2,d1,d0 = map(int, input_data.zfill(4))
        s1 = ((not d3) and d1) or ((not d2) and (not d1) and (not d0)) or ( d3 and (not d2) and (not d1) ) or ((not d3) and d2 and d0)
        s2 = ((not d3) and (not d2)) or (( not d3) and (not d1) and (not d0)) or (d3 and (not d2) and (not d1)) or ((not d3) and d1 and d0)
        s3 = ((not d3) and (not d1)) or (d3 and (not d2) and (not d1)) or ((not d2) and d1 and d0) or ((not d3) and d2 and d1)
        s4 = (d3 and (not d2) and (not d1)) or (d2 and (not d1) and d0) or (not(d3) and not(d2) and not(d0)) or ((not d3) and (not d2) and d1) or ((not d3) and d1 and (not d0))
        s5 = ((not d2) and (not d1) and (not d0)) or ((not d3) and d1 and (not d0))
        s6 = ((not d2) and (not d1) and (not d0)) or ((not d3) and d2 and (not d1)) or ((not d3) and d2 and (not d0)) or (d3 and (not d2) and (not d1))
        s7 = ((not d3) and (not d2) and d1) or ((not d3) and d2 and (not d1)) or ((not d3) and d2 and (not d0)) or (d3 and (not d2) and (not d1))
        return [s1,s2,s3,s4,s5,s6,s7]

    def setData(self, input_data):
        self.setState(self.decoder(input_data))
