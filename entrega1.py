# Definición de la clase Node (nodo de la lista)
class Node:
    def __init__(self, data):
        self.data = data      # Información del nodo (por ejemplo, una ubicación)
        self.next = None      # Puntero al siguiente nodo

# Definición de la clase LinkedList (lista enlazada)
class LinkedList:
    def __init__(self):
        self.head = None  # La lista se inicia vacía

    # Método 1: Verificar si la lista está vacía
    def is_empty(self):
        return self.head is None

    # Método 2: Contar la cantidad de elementos en la lista
    def count(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    # Método 3: Imprimir en pantalla los elementos de la lista
    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    # Método 4: Agregar un elemento al inicio de la lista
    def add_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Métodos auxiliares para merge sort y búsqueda binaria, los cuales fueron estudiados en clase (Método 5)

    def _get_middle(self, head):
        if head is None:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def _sorted_merge(self, left, right):
        if left is None:
            return right
        if right is None:
            return left
        if left.data <= right.data:
            result = left
            result.next = self._sorted_merge(left.next, right)
        else:
            result = right
            result.next = self._sorted_merge(left, right.next)
        return result

    def _merge_sort(self, head):
        if head is None or head.next is None:
            return head
        middle = self._get_middle(head)
        next_to_middle = middle.next
        middle.next = None  # Separamos la lista en dos mitades
        left = self._merge_sort(head)
        right = self._merge_sort(next_to_middle)
        sorted_list = self._sorted_merge(left, right)
        return sorted_list

    def sort(self):
        self.head = self._merge_sort(self.head)

    def _get_middle_in_range(self, start, end):
        slow = start
        fast = start
        while fast != end and fast.next != end:
            fast = fast.next.next if fast.next else None
            slow = slow.next
        return slow

    def search(self, target):
        # Ordenamos la lista primero
        self.sort()
        start = self.head
        end = None
        while start != end:
            mid = self._get_middle_in_range(start, end)
            if mid is None:
                break
            if mid.data == target:
                return True
            elif mid.data < target:
                start = mid.next
            else:
                end = mid
        return False

# Ejemplo de uso de la lista enlazada con ciudades del área metropolitana de Bucaramanga
if __name__ == '__main__':
    route_list = LinkedList()

    print("¿La lista está vacía?", route_list.is_empty())

    # Agregar elementos al inicio de la lista.
    # Se utilizan ciudades del área metropolitana de Bucaramanga.
    route_list.add_at_beginning("Ciudad C: Piedecuesta (7.1600, -73.1200)")
    route_list.add_at_beginning("Ciudad B: Floridablanca (7.1300, -73.0800)")
    route_list.add_at_beginning("Ciudad A: Bucaramanga (7.1254, -73.1198)")

    print("¿La lista está vacía?", route_list.is_empty())
    print("Cantidad de elementos:", route_list.count())

    print("\nElementos de la lista:")
    route_list.print_list()

    # Buscar un elemento específico (ejemplo: Floridablanca)
    target = "Ciudad B: Floridablanca (7.1300, -73.0800)"
    found = route_list.search(target)
    print(f"\n¿El elemento '{target}' fue encontrado?", found)

    # Mostrar la lista ordenada (por la búsqueda se ordena la lista)
    print("\nLista ordenada:")
    route_list.print_list()