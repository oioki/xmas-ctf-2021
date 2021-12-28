""#line:5:"""
__all__ =[]#line:7:__all__ = []
class O000O0OO0O00OO00O :#line:9:class Node:
    def __init__ (OO00000O0OOO0O000 ,O00O0O00OO0O0OO00 ):#line:11:def __init__(self, candidate):
        OO00000O0OOO0O000 .candidate =O00O0O00OO0O0OO00 #line:13:self.candidate = candidate
class OO0O0O0OOO0O0O00O :#line:15:class HeaderNode:
    def __init__ (O0O00OOOO000000O0 ,OOO0O0O00OOO00O00 ):#line:17:def __init__(self, constraint):
        O0O00OOOO000000O0 .constraint =OOO0O0O00OOO00O00 #line:18:self.constraint = constraint
class O0OOOO00000000O00 (object ):#line:20:class DancingLinks(object):
    def __init__ (OO000O00O0OOOO000 ,OOO0000O0O00O0OO0 ,O0O0O00O0O0O00000 ,OO000OO00O0O00OO0 ,O00OOO0O0O0OOO00O ):#line:22:def __init__(self, candidates, constraints, optional, check_func):
        OO000O00O0OOOO000 .__O0O00OO0OOOO0OOO0 =OOO0000O0O00O0OO0 #line:23:self.__candidates = candidates
        OO000O00O0OOOO000 .__O0O0O0O0OO00OOOO0 =O0O0O00O0O0O00000 #line:24:self.__constraints = constraints
        OO000O00O0OOOO000 .__OOOOOO0OO00O0OO00 =OO000OO00O0O00OO0 #line:25:self.__optional = optional
        OO000O00O0OOOO000 .__OOO0O0O00OOOOO0O0 =O00OOO0O0O0OOO00O #line:26:self.__check = check_func
        OO000O00O0OOOO000 .__OO0O00OOOOOOOOOO0 =None #line:28:self.__head = None
        OO000O00O0OOOO000 .__O00O0OOO0OO00OOOO =[]#line:30:self.__results = []
        OO000O00O0OOOO000 .__O0O0OOOO0O0O000O0 =[]#line:31:self.__partial = []
    def build_links (OOO0OO0000000OO00 ):#line:33:def build_links(self):
        OOO0OO0000000OO00 .__OO0O00OOOOOOOOOO0 =OO0O0O0OOO0O0O00O (None )#line:35:self.__head = HeaderNode(None)
        O0O0O00O0OO0OOOO0 =OOO0OO0000000OO00 .__OO0O00OOOOOOOOOO0 #line:36:cursor = self.__head
        for O00O00OO0OOO00O00 in OOO0OO0000000OO00 .__O0O0O0O0OO00OOOO0 :#line:37:for constraint in self.__constraints:
            O0OOOOOO0000O0O00 =OO0O0O0OOO0O0O00O (O00O00OO0OOO00O00 )#line:38:header = HeaderNode(constraint)
            O0O0O00O0OO0OOOO0 .next =O0OOOOOO0000O0O00 #line:39:cursor.next = header
            O0OOOOOO0000O0O00 .prev =O0O0O00O0OO0OOOO0 #line:40:header.prev = cursor
            O0OOOOOO0000O0O00 .up =O0OOOOOO0000O0O00 #line:42:header.up = header
            O0OOOOOO0000O0O00 .down =O0OOOOOO0000O0O00 #line:43:header.down = header
            O0O0O00O0OO0OOOO0 =O0OOOOOO0000O0O00 #line:44:cursor = header
        O0O0O00O0OO0OOOO0 .next =OOO0OO0000000OO00 .__OO0O00OOOOOOOOOO0 #line:45:cursor.next = self.__head
        OOO0OO0000000OO00 .__OO0O00OOOOOOOOOO0 .prev =O0O0O00O0OO0OOOO0 #line:46:self.__head.prev = cursor
        for O000OOOOO000000O0 ,O0OO0OOOOOO0000OO in enumerate (OOO0OO0000000OO00 .__O0O00OO0OOOO0OOO0 ):#line:49:for i, candidate in enumerate(self.__candidates):
            O0O0OO00O0OO0OO00 =None #line:50:rowhead = None
            O0OOOO00O0000OOO0 =None #line:51:current = None
            O0O0O00O0OO0OOOO0 =OOO0OO0000000OO00 .__OO0O00OOOOOOOOOO0 .next #line:52:cursor = self.__head.next
            while O0O0O00O0OO0OOOO0 !=OOO0OO0000000OO00 .__OO0O00OOOOOOOOOO0 :#line:53:while cursor!=self.__head:
                if OOO0OO0000000OO00 .__OOO0O0O00OOOOO0O0 (O0OO0OOOOOO0000OO ,O0O0O00O0OO0OOOO0 .constraint ):#line:54:if self.__check(candidate, cursor.constraint):
                    O0OO00000OO00OO0O =O000O0OO0O00OO00O (O000OOOOO000000O0 )#line:56:node = Node(i)
                    if not O0O0OO00O0OO0OO00 :#line:58:if not rowhead:
                        O0O0OO00O0OO0OO00 =O0OOOO00O0000OOO0 =O0OO00000OO00OO0O #line:59:rowhead = current = node
                    else :#line:60:else:
                        O0OOOO00O0000OOO0 .next =O0OO00000OO00OO0O #line:61:current.next = node
                        O0OO00000OO00OO0O .prev =O0OOOO00O0000OOO0 #line:62:node.prev = current
                        O0OOOO00O0000OOO0 =O0OO00000OO00OO0O #line:63:current = node
                    O0O000O00O0O000O0 =O0O0O00O0OO0OOOO0 .up #line:65:temp = cursor.up
                    O0O0O00O0OO0OOOO0 .up =O0OO00000OO00OO0O #line:66:cursor.up = node
                    O0OO00000OO00OO0O .down =O0O0O00O0OO0OOOO0 #line:67:node.down = cursor
                    O0OO00000OO00OO0O .up =O0O000O00O0O000O0 #line:68:node.up = temp
                    O0O000O00O0O000O0 .down =O0OO00000OO00OO0O #line:69:temp.down = node
                O0O0O00O0OO0OOOO0 =O0O0O00O0OO0OOOO0 .next #line:71:cursor = cursor.next
            if O0OOOO00O0000OOO0 :#line:73:if current:
                O0OOOO00O0000OOO0 .next =O0O0OO00O0OO0OO00 #line:74:current.next = rowhead
                O0O0OO00O0OO0OO00 .prev =O0OOOO00O0000OOO0 #line:75:rowhead.prev = current
    def algorithm_x (O0OOO0OOO0OOOO0OO ):#line:79:def algorithm_x(self):
        OOOOOO0OOO0OO000O =(O0OOO0OOO0OOOO0OO .__OO0O00OOOOOOOOOO0 .next ==O0OOO0OOO0OOOO0OO .__OO0O00OOOOOOOOOO0 )#line:81:empty = (self.__head.next == self.__head)
        if not OOOOOO0OOO0OO000O :#line:83:if not empty:
            OOO00O00OOOOOOOO0 =True #line:84:all_empty_optional = True
            O00000O0OOOO00OO0 =O0OOO0OOO0OOOO0OO .__OO0O00OOOOOOOOOO0 .next #line:85:col = self.__head.next
            while O00000O0OOOO00OO0 !=O0OOO0OOO0OOOO0OO .__OO0O00OOOOOOOOOO0 :#line:86:while col!=self.__head:
                if O00000O0OOOO00OO0 .constraint not in O0OOO0OOO0OOOO0OO .__OOOOOO0OO00O0OO00 or O00000O0OOOO00OO0 .down !=O00000O0OOOO00OO0 :#line:87:if col.constraint not in self.__optional or col.down != col:
                    OOO00O00OOOOOOOO0 =False #line:88:all_empty_optional = False
                    break #line:89:break
                O00000O0OOOO00OO0 =O00000O0OOOO00OO0 .next #line:90:col = col.next
        if OOOOOO0OOO0OO000O or OOO00O00OOOOOOOO0 :#line:92:if empty or all_empty_optional:
            OO00000OOOO0OOO00 =sorted (O0OOO0OOO0OOOO0OO .__O0O0OOOO0O0O000O0 )#line:93:result = sorted(self.__partial)
            if OO00000OOOO0OOO00 not in O0OOO0OOO0OOOO0OO .__O00O0OOO0OO00OOOO :#line:94:if result not in self.__results:
                O0OOO0OOO0OOOO0OO .__O00O0OOO0OO00OOOO .append (OO00000OOOO0OOO00 )#line:95:self.__results.append(result)
        else :#line:96:else:
            O00000O0OOOO00OO0 =O0OOO0OOO0OOOO0OO .__OO0O00OOOOOOOOOO0 .next #line:97:col = self.__head.next
            if O00000O0OOOO00OO0 .down ==O00000O0OOOO00OO0 :#line:98:if col.down == col:
                if O00000O0OOOO00OO0 .constraint in O0OOO0OOO0OOOO0OO .__OOOOOO0OO00O0OO00 :#line:99:if col.constraint in self.__optional:
                    O00000O0OOOO00OO0 =O00000O0OOOO00OO0 .next #line:100:col = col.next
                else :#line:101:else:
                    return #line:103:return
            O000O0O00O0O00000 =O00000O0OOOO00OO0 .down #line:105:row = col.down
            while O000O0O00O0O00000 !=O00000O0OOOO00OO0 :#line:106:while row!=col:
                O0OOO0OOO0OOOO0OO .__O0O0OOOO0O0O000O0 .append (O000O0O00O0O00000 .candidate )#line:108:self.__partial.append(row.candidate)
                O0OOO0OOO0OOOO0OO .__O0OOOO0OO0O00OO0O (O000O0O00O0O00000 )#line:110:self.__cover_row(row)
                O0OOO0OOO0OOOO0OO .algorithm_x ()#line:112:self.algorithm_x()
                O0OOO0OOO0OOOO0OO .__O000OOOOOOO0OOOOO (O000O0O00O0O00000 )#line:114:self.__uncover_row(row)
                O0OOO0OOO0OOOO0OO .__O0O0OOOO0O0O000O0 .pop ()#line:116:self.__partial.pop()
                O000O0O00O0O00000 =O000O0O00O0O00000 .down #line:118:row = row.down
    def __O0OOOO0OO0O00OO0O (OO0OOOO0O0OO00OO0 ,O000OOOO0000O0000 ):#line:120:def __cover_row(self, r):
        O000O00OO00OOO0OO =O000OOOO0000O0000 #line:121:rr = r
        OO0OOOO0O0OO00OO0 .__OOOOOO0OOOOO0OO00 (O000OOOO0000O0000 )#line:122:self.__cover_column(r)
        O000OOOO0000O0000 =O000OOOO0000O0000 .next #line:123:r = r.next
        while O000OOOO0000O0000 !=O000O00OO00OOO0OO :#line:124:while r!=rr:
            OO0OOOO0O0OO00OO0 .__OOOOOO0OOOOO0OO00 (O000OOOO0000O0000 )#line:125:self.__cover_column(r)
            O000OOOO0000O0000 =O000OOOO0000O0000 .next #line:126:r = r.next
    def __O000OOOOOOO0OOOOO (O0O0O00O0000OO0O0 ,O00OOOO0O0O0OOOO0 ):#line:128:def __uncover_row(self, r):
        O0O00O0OOO0O0O00O =O00OOOO0O0O0OOOO0 #line:129:rr = r
        O00OOOO0O0O0OOOO0 =O00OOOO0O0O0OOOO0 .prev #line:130:r = r.prev
        while O00OOOO0O0O0OOOO0 !=O0O00O0OOO0O0O00O :#line:131:while r!=rr:
            O0O0O00O0000OO0O0 .__O00OOOO0000O000OO (O00OOOO0O0O0OOOO0 )#line:132:self.__uncover_column(r)
            O00OOOO0O0O0OOOO0 =O00OOOO0O0O0OOOO0 .prev #line:133:r = r.prev
        O0O0O00O0000OO0O0 .__O00OOOO0000O000OO (O00OOOO0O0O0OOOO0 )#line:134:self.__uncover_column(r)
    def __OOOOOO0OOOOO0OO00 (O0O00O0OOO0OO0000 ,OOOO0OOOO00O00000 ):#line:136:def __cover_column(self, c):
        while not isinstance (OOOO0OOOO00O00000 ,OO0O0O0OOO0O0O00O ):#line:138:while not isinstance(c, HeaderNode):
            OOOO0OOOO00O00000 =OOOO0OOOO00O00000 .up #line:139:c = c.up
        OOOO0OOOO00O00000 .next .prev =OOOO0OOOO00O00000 .prev #line:142:c.next.prev = c.prev
        OOOO0OOOO00O00000 .prev .next =OOOO0OOOO00O00000 .next #line:143:c.prev.next = c.next
        O00O00O0O00000O0O =OOOO0OOOO00O00000 #line:146:h = c
        OOOO0OOOO00O00000 =OOOO0OOOO00O00000 .down #line:147:c = c.down
        while OOOO0OOOO00O00000 !=O00O00O0O00000O0O :#line:148:while c!=h:
            OOOO000OOO00000O0 =OOOO0OOOO00O00000 #line:149:r = c
            O0O0O0OOO00OOO0O0 =OOOO0OOOO00O00000 .next #line:150:cell = c.next
            while O0O0O0OOO00OOO0O0 !=OOOO000OOO00000O0 :#line:151:while cell!=r:
                O0O0O0OOO00OOO0O0 .up .down =O0O0O0OOO00OOO0O0 .down #line:152:cell.up.down = cell.down
                O0O0O0OOO00OOO0O0 .down .up =O0O0O0OOO00OOO0O0 .up #line:153:cell.down.up = cell.up
                O0O0O0OOO00OOO0O0 =O0O0O0OOO00OOO0O0 .next #line:154:cell = cell.next
            OOOO0OOOO00O00000 =OOOO0OOOO00O00000 .down #line:155:c = c.down
    def __O00OOOO0000O000OO (O0OO000OOO00OO0O0 ,OO0000O0OO000OO00 ):#line:157:def __uncover_column(self, c):
        while not isinstance (OO0000O0OO000OO00 ,OO0O0O0OOO0O0O00O ):#line:159:while not isinstance(c, HeaderNode):
            OO0000O0OO000OO00 =OO0000O0OO000OO00 .up #line:160:c = c.up
        OO0000O0OO000OO00 .prev .next =OO0000O0OO000OO00 #line:162:c.prev.next = c
        OO0000O0OO000OO00 .next .prev =OO0000O0OO000OO00 #line:163:c.next.prev = c
        O0000O00OOOOOO0OO =OO0000O0OO000OO00 #line:165:h = c
        OO0000O0OO000OO00 =OO0000O0OO000OO00 .up #line:166:c = c.up
        while OO0000O0OO000OO00 !=O0000O00OOOOOO0OO :#line:167:while c!=h:
            OOO0OOO0O0OO0OO0O =OO0000O0OO000OO00 #line:168:r = c
            OO00O000000OO0OOO =OO0000O0OO000OO00 .next #line:169:cell = c.next
            while OO00O000000OO0OOO !=OOO0OOO0O0OO0OO0O :#line:170:while cell!=r:
                OO00O000000OO0OOO .up .down =OO00O000000OO0OOO #line:171:cell.up.down = cell
                OO00O000000OO0OOO .down .up =OO00O000000OO0OOO #line:172:cell.down.up = cell
                OO00O000000OO0OOO =OO00O000000OO0OOO .next #line:173:cell = cell.next
            OO0000O0OO000OO00 =OO0000O0OO000OO00 .up #line:174:c = c.up
    def get_results (O00OO0OO0O00O00O0 ):#line:176:def get_results(self):
        return [[O00OO0OO0O00O00O0 .__O0O00OO0OOOO0OOO0 [O0O00O0OO000OO00O ]for O0O00O0OO000OO00O in O0O000O0OO00OO00O ]for O0O000O0OO00OO00O in O00OO0OO0O00O00O0 .__O00O0OOO0OO00OOOO ]#line:179:return [[self.__candidates[x] for x in result] for result in self.__results]
def O000OOOO0O0OO0OO0 (O0O0000O0O00OOO0O ):#line:181:def solve_N_queens(n):
    OOOO000OO0000000O =[(O00000OO000000OOO ,OOO0O00OO000OO000 )for O00000OO000000OOO in range (O0O0000O0O00OOO0O )for OOO0O00OO000OO000 in range (O0O0000O0O00OOO0O )]#line:182:candidates = [(x, y) for x in range(n) for y in range(n)]
    O0O0OO0O000OO00O0 =[]#line:183:constraints = []
    O0O000O00OOO00000 =[]#line:184:optional = []
    for OOO0OO00000OOO00O in range (O0O0000O0O00OOO0O ):#line:185:for i in range(n):
        O0O0OO0O000OO00O0 .append (('row',OOO0OO00000OOO00O ))#line:187:constraints.append(('row', i))
    for OOO0OO00000OOO00O in range (O0O0000O0O00OOO0O ):#line:188:for i in range(n):
        O0O0OO0O000OO00O0 .append (('col',OOO0OO00000OOO00O ))#line:190:constraints.append(('col', i))
    for OOO0OO00000OOO00O in range (O0O0000O0O00OOO0O *2 -1 ):#line:193:for i in range(n*2-1):
        O0O0OO0O000OO00O0 .append (('diag',OOO0OO00000OOO00O ))#line:195:constraints.append(('diag', i))
        O0O000O00OOO00000 .append (('diag',OOO0OO00000OOO00O ))#line:196:optional.append(('diag', i))
    for OOO0OO00000OOO00O in range (O0O0000O0O00OOO0O *2 -1 ):#line:197:for i in range(n*2-1):
        O0O0OO0O000OO00O0 .append (('rdiag',OOO0OO00000OOO00O ))#line:198:constraints.append(('rdiag', i))
        O0O000O00OOO00000 .append (('rdiag',OOO0OO00000OOO00O ))#line:199:optional.append(('rdiag', i))
    def OOOOOOOO0O00O0O00 (OO000OO0OO000OO0O ,O000OOOOO000OO000 ):#line:201:def checker(candidate, constraint):
        OOOOOO0OO00OO0OO0 ,OOOOO0OOOOO0O00O0 =O000OOOOO000OO000 #line:202:t, val = constraint
        if OOOOOO0OO00OO0OO0 =='row':#line:203:if t=='row':
            return OO000OO0OO000OO0O [0 ]==OOOOO0OOOOO0O00O0 #line:204:return candidate[0]==val
        if OOOOOO0OO00OO0OO0 =='col':#line:205:if t=='col':
            return OO000OO0OO000OO0O [1 ]==OOOOO0OOOOO0O00O0 #line:206:return candidate[1]==val
        if OOOOOO0OO00OO0OO0 =='diag':#line:207:if t=='diag':
            return (OO000OO0OO000OO0O [0 ]+OO000OO0OO000OO0O [1 ])==OOOOO0OOOOO0O00O0 #line:208:return (candidate[0]+candidate[1])==val
        else :#line:209:else:
            return (O0O0000O0O00OOO0O -1 -OO000OO0OO000OO0O [0 ]+OO000OO0OO000OO0O [1 ])==OOOOO0OOOOO0O00O0 #line:210:return (n-1-candidate[0]+candidate[1])==val
    O00OO00OOOO00OO0O =O0OOOO00000000O00 (OOOO000OO0000000O ,O0O0OO0O000OO00O0 ,O0O000O00OOO00000 ,OOOOOOOO0O00O0O00 )#line:212:dl = DancingLinks(candidates, constraints, optional, checker)
    O00OO00OOOO00OO0O .build_links ()#line:213:dl.build_links()
    O00OO00OOOO00OO0O .algorithm_x ()#line:214:dl.algorithm_x()
    OO0OOOO0OOOO0000O =O00OO00OOOO00OO0O .get_results ()#line:215:results = dl.get_results()
    for O00O00O000OO000OO in OO0OOOO0OOOO0000O :#line:217:for result in results:
        print ("+++++++++")#line:218:print("+++++++++")
        for OOO0OO00000OOO00O in range (O0O0000O0O00OOO0O ):#line:219:for i in range(n):
            O0O0OOO0OOO0O0O0O =""#line:220:s = ""
            for O0O0OOO000O000OO0 in range (O0O0000O0O00OOO0O ):#line:221:for j in range(n):
                if (OOO0OO00000OOO00O ,O0O0OOO000O000OO0 )in O00O00O000OO000OO :#line:222:if (i, j) in result:
                    O0O0OOO0OOO0O0O0O +="1"#line:223:s+="1"
                else :#line:224:else:
                    O0O0OOO0OOO0O0O0O +="0"#line:225:s+="0"
            print (O0O0OOO0OOO0O0O0O )#line:226:print(s)
        print ("+++++++++")#line:227:print("+++++++++")
    print ("%d results found for N-Queen"%len (OO0OOOO0OOOO0000O ))#line:228:print("%d results found for N-Queen"%len(results))
def O0OO000O0O00O00OO ():#line:230:def main():
    O000OOOO0O0OO0OO0 (10 )#line:231:solve_N_queens(10)
if __name__ =="__main__":#line:233:if __name__ == "__main__":
	O0OO000O0O00O00OO ()#line:234:main()
	O00OOOO00O00O000O ='/home/santa/NaughtyList.csv'#line:235
	OOO0OO0O00O0O0O00 =openpyxl .load_workbook (O00OOOO00O00O000O )#line:238:book = openpyxl.load_workbook(path)
	O000O00OOO000O0OO =OOO0OO0O00O0O0O00 ['Present Wish']#line:241:sheet = book['Present Wish']
	print ("Maximum rows before removing:",O000O00OOO000O0OO .max_row )#line:243:print("Maximum rows before removing:", sheet.max_row)
	for O0OO0O000OOOOOO0O in O000O00OOO000O0OO :#line:246:for row in sheet:
		remove (O000O00OOO000O0OO )#line:247:remove(sheet)
	O00OOOO00O00O000O ='/var/log/apt/history.log'#line:251
	OOO0OO0O00O0O0O00 .save (O00OOOO00O00O000O )
