#tramvaj
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularLinkedList:
    def __init__(self, head=None):
        self.head = head

    def prepend(self, value):
        new_node = Node(value)
        current = self.head
        new_node.next = self.head

        if not self.head:
            new_node.next = new_node
        else:
            while current.next != self.head:
                current = current.next
            current.next = new_node
        self.head = new_node
    
    def append(self, value):
        if not self.head:
            self.head = Node(value)
            self.head.next = self.head
        else:
            new_node = Node(value)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head

    def print_list(self):
        current = self.head

        while current:
            print(current.value)
            current = current.next
            if current == self.head:
                break
    def change_value_by_key_ulaz(self, key):
        new_value =int(input('ulaz: '))
        current = self.head
        current.value[key] = new_value
        print(current.value)

        

    def change_value_by_key_izlaz(self, key):
        new_value = int(input('izlaz: '))
        current = self.head
        current.value[key] = new_value
              


        

    def is_circular_linked_list(self, input_list):
        #input_list je siglylinked lista iz te klase
        cur = input_list.head
        while cur.next:
            cur=cur.next
            if cur.next == input_list.head:
                return True
        return False

def tramvaj_8(N):
    cl=CircularLinkedList()
    for i in range(N):
        cl.append({'naziv': input('naziv:'), 'ulaz' : int(input('ulaz putnika:')), 'izlaz' : int(input('izlaz:')) })
    
    cur=cl.head
    while cur:
        if cur.value['ulaz'] < cur.value['izlaz']:
            print(cur.value['naziv'], 0)
        else:
            print('na stanici ',cur.value['naziv'],' je bilo ',cur.value['ulaz']-cur.value['izlaz'],'putnika')
        cur = cur.next
        if cur.value['naziv'] == cl.head.value['naziv']:
            break
    
    broj_krugova_tramvaja = 1
    while broj_krugova_tramvaja <= 3:
        current = cl.head
        while current:
            print(current.value['naziv']+':')
            current.value['ulaz'] =   int(input('ulaz: '))
            print(current.value['naziv']+':')
            current.value['izlaz'] =   int(input('izlaz: '))
            current=current.next
            if current.value['naziv'] == cl.head.value['naziv']:
                break
        broj_krugova_tramvaja += 1 
        cur=cl.head
        while cur:
            if cur.value['ulaz'] < cur.value['izlaz']:
                print(cur.value['naziv'], 0)
            else:
                print('na stanici ',cur.value['naziv'],' je bilo ',cur.value['ulaz']-cur.value['izlaz'],'putnika')
            cur = cur.next
            if cur.value['naziv'] == cl.head.value['naziv']:
                break    
        
    print('gotovo')




        



        

        


'''
c1 = CircularLinkedList()
c1.append({'naziv': 'stanica_1', 'ulaz' : input('ulaz putnika:'), 'izlaz' : input('izlaz:') })
c1.append({'naziv': 'stanica_2', 'ulaz' :  input('ulaz putnika:'), 'izlaz' : input('izlaz:') })
c1.append({'naziv': 'stanica_3', 'ulaz' :  input('ulaz putnika:'), 'izlaz' : input('izlaz:') })

cl.print_list()

'''
tramvaj_8(2)