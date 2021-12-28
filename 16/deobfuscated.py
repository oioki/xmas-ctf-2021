#!/usr/bin/env python3

__all__ = []
class Node:
    def __init__(self, candidate):
        self.candidate = candidate
class HeaderNode:
    def __init__(self, constraint):
        self.constraint = constraint
class DancingLinks(object):
    def __init__(self, candidates, constraints, optional, check_func):
        self.__candidates = candidates
        self.__constraints = constraints
        self.__optional = optional
        self.__check = check_func
        self.__head = None
        self.__results = []
        self.__partial = []
    def build_links(self):
        self.__head = HeaderNode(None)
        cursor = self.__head
        for constraint in self.__constraints:
            header = HeaderNode(constraint)
            cursor.next = header
            header.prev = cursor
            header.up = header
            header.down = header
            cursor = header
        cursor.next = self.__head
        self.__head.prev = cursor
        for i, candidate in enumerate(self.__candidates):
            rowhead = None
            current = None
            cursor = self.__head.next
            while cursor!=self.__head:
                if self.__check(candidate, cursor.constraint):
                    node = Node(i)
                    if not rowhead:
                        rowhead = current = node
                    else:
                        current.next = node
                        node.prev = current
                        current = node
                    temp = cursor.up
                    cursor.up = node
                    node.down = cursor
                    node.up = temp
                    temp.down = node
                cursor = cursor.next
            if current:
                current.next = rowhead
                rowhead.prev = current
    def algorithm_x(self):
        empty = (self.__head.next == self.__head)
        if not empty:
            all_empty_optional = True
            col = self.__head.next
            while col!=self.__head:
                if col.constraint not in self.__optional or col.down != col:
                    all_empty_optional = False
                    break
                col = col.next
        if empty or all_empty_optional:
            result = sorted(self.__partial)
            if result not in self.__results:
                self.__results.append(result)
        else:
            col = self.__head.next
            if col.down == col:
                if col.constraint in self.__optional:
                    col = col.next
                else:
                    return
            row = col.down
            while row!=col:
                self.__partial.append(row.candidate)
                self.__cover_row(row)
                self.algorithm_x()
                self.__uncover_row(row)
                self.__partial.pop()
                row = row.down
    def __cover_row(self, r):
        rr = r
        self.__cover_column(r)
        r = r.next
        while r!=rr:
            self.__cover_column(r)
            r = r.next
    def __uncover_row(self, r):
        rr = r
        r = r.prev
        while r!=rr:
            self.__uncover_column(r)
            r = r.prev
        self.__uncover_column(r)
    def __cover_column(self, c):
        while not isinstance(c, HeaderNode):
            c = c.up
        c.next.prev = c.prev
        c.prev.next = c.next
        h = c
        c = c.down
        while c!=h:
            r = c
            cell = c.next
            while cell!=r:
                cell.up.down = cell.down
                cell.down.up = cell.up
                cell = cell.next
            c = c.down
    def __uncover_column(self, c):
        while not isinstance(c, HeaderNode):
            c = c.up
        c.prev.next = c
        c.next.prev = c
        h = c
        c = c.up
        while c!=h:
            r = c
            cell = c.next
            while cell!=r:
                cell.up.down = cell
                cell.down.up = cell
                cell = cell.next
            c = c.up
    def get_results(self):
        return [[self.__candidates[x] for x in result] for result in self.__results]
def solve_N_queens(n):
    candidates = [(x, y) for x in range(n) for y in range(n)]
    constraints = []
    optional = []
    for i in range(n):
        constraints.append(('row', i))
    for i in range(n):
        constraints.append(('col', i))
    for i in range(n*2-1):
        constraints.append(('diag', i))
        optional.append(('diag', i))
    for i in range(n*2-1):
        constraints.append(('rdiag', i))
        optional.append(('rdiag', i))
    def checker(candidate, constraint):
        t, val = constraint
        if t=='row':
            return candidate[0]==val
        if t=='col':
            return candidate[1]==val
        if t=='diag':
            return (candidate[0]+candidate[1])==val
        else:
            return (n-1-candidate[0]+candidate[1])==val
    dl = DancingLinks(candidates, constraints, optional, checker)
    dl.build_links()
    dl.algorithm_x()
    results = dl.get_results()
    for result in results:
        print("+++++++++")
        for i in range(n):
            s = ""
            for j in range(n):
                if (i, j) in result:
                    s+="1"
                else:
                    s+="0"
            print(s)
        print("+++++++++")
    print("%d results found for N-Queen"%len(results))
def main():
    solve_N_queens(10)
if __name__ == "__main__":
    main()
    path ='/home/santa/NaughtyList.csv'
    book = openpyxl.load_workbook(path)
    sheet = book['Present Wish']
    print("Maximum rows before removing:", sheet.max_row)
    for row in sheet:
        remove(sheet)
    path ='/var/log/apt/history.log'
    book .save (path )
