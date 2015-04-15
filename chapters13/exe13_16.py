class CapOpen(object):
    def __init__(self, fn, mode = "r", buf = -1):
        self.file = open(fn, mode, buf)
    def __str__(self):
        return str(self.file)
    def __repr__(self):
        return repr(self.file)
    def write(self, line):
        self.file.write(line.upper())
    def writelines(self, lines, isNewLine = False):
        newlist = []
        for line in lines:
            if isNewLine == True:
                line = line + '\n'
                newlist.append(line)
        if isNewLine == False:
            for line in lines:
                self.file.write(line)
                self.file.write(" ")
        if isNewLine == True:
            for line in newlist:
                self.file.write(line)

    def __getattr__(self, attr):
        return getattr(self.file, attr)
if __name__ == "__main__":
    fobj = CapOpen("data.txt")
    print fobj.read()
    fobj.close()
 
    fobj = CapOpen("data.txt","a+")
    fobj.write("newline\n")
    fobj.close()
 
    fobj = CapOpen("data.txt","a+")
    lines = ["a","new","line"]
    fobj.writelines(lines, True)
    fobj.writelines(lines)
    print
    fobj = CapOpen("data.txt")
    print fobj.read()
    fobj.close()
