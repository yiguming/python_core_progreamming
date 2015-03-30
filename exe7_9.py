#!/usr/bin/env python
def tr(srcstr, dststr, string,casemap=True):
    assert len(srcstr)>=len(dststr)
    
    table = dict(zip(srcstr,dststr))
    print table
    if len(srcstr) > len(dststr):
        temp = {}.fromkeys(srcstr[len(dststr):])
        print temp
        table.update(temp)
    print table

    ls = [ ]
    for ch in string:
        if not casemap:
            if ch.lower() in table:
                ls.append(table[ch.lower()])
            elif ch.upper() in table:
                ls.append(table[ch.upper()])
            else:
                ls.append(ch)
            continue
        
        if ch in table:
            ls.append(table[ch])
        else:
            ls.append(ch)
        
    ls = [ch for ch in ls if ch]
    return " ".join(ls)


if __name__ =="__main__":
    print tr('abc', 'mno', 'abcdef')  
    print tr('aBcdef', 'mno', 'abcdefghi', False)
