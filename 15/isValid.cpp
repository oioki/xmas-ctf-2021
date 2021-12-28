
/* isValid(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char>>) */

ulong isValid(basic_string param_1)

{
  bool bVar1;
  bool bVar2;
  long lVar3;
  char *pcVar4;
  undefined4 in_register_0000003c;
  char **ppcVar5;
  char cVar6;
  int iVar7;
  long *local_58 [2];
  long local_48 [3];
  
  ppcVar5 = (char **)CONCAT44(in_register_0000003c,param_1);
  if ((char *)0xe < ppcVar5[1] + -8) {
    return 0;
  }
  lVar3 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::find
                    ((char *)ppcVar5,(ulong)" ",0);
  if (lVar3 == -1) {
    cVar6 = '0';
    bVar1 = false;
    do {
      local_58[0] = local_48;
      std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::_M_construct
                ((ulong)local_58,'\x01');
      *(char *)local_58[0] = cVar6;
      lVar3 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::find
                        ((char *)ppcVar5,(ulong)local_58[0],0);
      if (lVar3 != -1) {
        bVar1 = true;
      }
      if (local_58[0] != local_48) {
        operator.delete(local_58[0],local_48[0] + 1);
      }
      cVar6 = cVar6 + '\x01';
    } while (cVar6 != ':');
    if ((bVar1) &&
       ((((((((lVar3 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>
                       ::find((char *)ppcVar5,(ulong)&DAT_0010204c,0), lVar3 != -1 ||
              (lVar3 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>
                       ::find((char *)ppcVar5,(ulong)&DAT_0010204e,0), lVar3 != -1)) ||
             (lVar3 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::
                      find((char *)ppcVar5,(ulong)&DAT_00102050,0), lVar3 != -1)) ||
            ((lVar3 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::
                      find((char *)ppcVar5,(ulong)&DAT_00102052,0), lVar3 != -1 ||
             (lVar3 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::
                      find((char *)ppcVar5,(ulong)&DAT_00102054), lVar3 != -1)))) ||
           ((lVar3 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::
                     find((char *)ppcVar5,(ulong)&DAT_00102056), lVar3 != -1 ||
            ((lVar3 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::
                      find((char *)ppcVar5,(ulong)&DAT_00102058), lVar3 != -1 ||
             (lVar3 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::
                      find((char *)ppcVar5,(ulong)&DAT_0010205a), lVar3 != -1)))))) ||
          (lVar3 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::
                   find((char *)ppcVar5,(ulong)&DAT_0010205c), lVar3 != -1)) ||
         ((((lVar3 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::
                     find((char *)ppcVar5,(ulong)&DAT_0010205e), lVar3 != -1 ||
            (lVar3 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::
                     find((char *)ppcVar5,(ulong)&DAT_00102060), lVar3 != -1)) ||
           (lVar3 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::
                    find((char *)ppcVar5,(ulong)&DAT_00102062), lVar3 != -1)) ||
          (((lVar3 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::
                     find((char *)ppcVar5,(ulong)&DAT_00102064), lVar3 != -1 ||
            (lVar3 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::
                     find((char *)ppcVar5,(ulong)&DAT_00102066), lVar3 != -1)) ||
           ((lVar3 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::
                     find((char *)ppcVar5,(ulong)&DAT_00102068), lVar3 != -1 ||
            ((lVar3 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::
                      find((char *)ppcVar5,(ulong)&DAT_0010206a), lVar3 != -1 ||
             (lVar3 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::
                      find((char *)ppcVar5,(ulong)&DAT_0010206c), lVar3 != -1)))))))))) ||
        ((lVar3 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::find
                            ((char *)ppcVar5,(ulong)&DAT_0010206e), lVar3 != -1 ||
         (((lVar3 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::
                    find((char *)ppcVar5,(ulong)&DAT_00102070), lVar3 != -1 ||
           (lVar3 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::
                    find((char *)ppcVar5,(ulong)&DAT_00102072), lVar3 != -1)) ||
          (lVar3 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::
                   find((char *)ppcVar5,(ulong)&DAT_00102074), lVar3 != -1)))))))) {
      bVar2 = false;
      iVar7 = 0x41;
      do {
        local_58[0] = local_48;
        std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::_M_construct
                  ((ulong)local_58,'\x01');
        lVar3 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::find
                          ((char *)ppcVar5,(ulong)local_58[0],0);
        if (lVar3 != -1) {
          bVar2 = bVar1;
        }
        if (local_58[0] != local_48) {
          operator.delete(local_58[0],local_48[0] + 1);
        }
        iVar7 = iVar7 + 1;
      } while (iVar7 != 0x5b);
      if (bVar2) {
        bVar1 = false;
        iVar7 = 0x5a;
        do {
          local_58[0] = local_48;
          std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::_M_construct
                    ((ulong)local_58,'\x01');
          lVar3 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::find
                            ((char *)ppcVar5,(ulong)local_58[0],0);
          if (lVar3 != -1) {
            bVar1 = bVar2;
          }
          if (local_58[0] != local_48) {
            operator.delete(local_58[0],local_48[0] + 1);
          }
          iVar7 = iVar7 + 1;
        } while (iVar7 != 0x7b);
        if ((((((bVar1) && (ppcVar5[1] == (char *)0x16)) &&
              (((pcVar4 = *ppcVar5, *pcVar4 == 'c' && ((pcVar4[0x15] == '}' && (pcVar4[1] == 't'))))
               && (pcVar4 = (char *)std::__cxx11::
                                    basic_string<char,std::char_traits<char>,std::allocator<char>>::
                                    at((ulong)pcVar4), *pcVar4 == '!')))) &&
             ((((((pcVar4 = (char *)std::__cxx11::
                                    basic_string<char,std::char_traits<char>,std::allocator<char>>::
                                    at((ulong)*ppcVar5), *pcVar4 == 'f' &&
                  (pcVar4 = (char *)std::__cxx11::
                                    basic_string<char,std::char_traits<char>,std::allocator<char>>::
                                    at((ulong)*ppcVar5), *pcVar4 == 'n')) &&
                 (pcVar4 = (char *)std::__cxx11::
                                   basic_string<char,std::char_traits<char>,std::allocator<char>>::
                                   at((ulong)*ppcVar5), *pcVar4 == '{')) &&
                ((pcVar4 = (char *)std::__cxx11::
                                   basic_string<char,std::char_traits<char>,std::allocator<char>>::
                                   at((ulong)*ppcVar5), *pcVar4 == 'a' &&
                 (pcVar4 = (char *)std::__cxx11::
                                   basic_string<char,std::char_traits<char>,std::allocator<char>>::
                                   at((ulong)*ppcVar5), *pcVar4 == 'F')))) &&
               (pcVar4 = (char *)std::__cxx11::
                                 basic_string<char,std::char_traits<char>,std::allocator<char>>::at
                                           ((ulong)*ppcVar5), *pcVar4 == 'm')) &&
              (((pcVar4 = (char *)std::__cxx11::
                                  basic_string<char,std::char_traits<char>,std::allocator<char>>::at
                                            ((ulong)*ppcVar5), *pcVar4 == 'r' &&
                (pcVar4 = (char *)std::__cxx11::
                                  basic_string<char,std::char_traits<char>,std::allocator<char>>::at
                                            ((ulong)*ppcVar5), *pcVar4 == 'w')) &&
               ((pcVar4 = (char *)std::__cxx11::
                                  basic_string<char,std::char_traits<char>,std::allocator<char>>::at
                                            ((ulong)*ppcVar5), *pcVar4 == 'o' &&
                (((pcVar4 = (char *)std::__cxx11::
                                    basic_string<char,std::char_traits<char>,std::allocator<char>>::
                                    at((ulong)*ppcVar5), *pcVar4 == '0' &&
                  (pcVar4 = (char *)std::__cxx11::
                                    basic_string<char,std::char_traits<char>,std::allocator<char>>::
                                    at((ulong)*ppcVar5), *pcVar4 == 's')) &&
                 (pcVar4 = (char *)std::__cxx11::
                                   basic_string<char,std::char_traits<char>,std::allocator<char>>::
                                   at((ulong)*ppcVar5), *pcVar4 == 'n')))))))))) &&
            ((pcVar4 = (char *)std::__cxx11::
                               basic_string<char,std::char_traits<char>,std::allocator<char>>::at
                                         ((ulong)*ppcVar5), *pcVar4 == 't' &&
             (pcVar4 = (char *)std::__cxx11::
                               basic_string<char,std::char_traits<char>,std::allocator<char>>::at
                                         ((ulong)*ppcVar5), *pcVar4 == 'S')))) &&
           ((pcVar4 = (char *)std::__cxx11::
                              basic_string<char,std::char_traits<char>,std::allocator<char>>::at
                                        ((ulong)*ppcVar5), *pcVar4 == 'y' &&
            ((pcVar4 = (char *)std::__cxx11::
                               basic_string<char,std::char_traits<char>,std::allocator<char>>::at
                                         ((ulong)*ppcVar5), *pcVar4 == 'e' &&
             (pcVar4 = (char *)std::__cxx11::
                               basic_string<char,std::char_traits<char>,std::allocator<char>>::at
                                         ((ulong)*ppcVar5), *pcVar4 == 'T')))))) {
          pcVar4 = (char *)std::__cxx11::
                           basic_string<char,std::char_traits<char>,std::allocator<char>>::at
                                     ((ulong)*ppcVar5);
          return (ulong)pcVar4 & 0xffffffffffffff00 | (ulong)(*pcVar4 == 'h');
        }
      }
    }
  }
  return 0;
}

