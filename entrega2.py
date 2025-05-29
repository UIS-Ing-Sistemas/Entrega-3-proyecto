# Definición de la clase Node para el Árbol Binario de Búsqueda
class TreeNode:
    def __init__(self, data):
        self.data = data      # Información almacenada en el nodo (por ejemplo, ciudad)
        self.left = None      # Subárbol izquierdo
        self.right = None     # Subárbol derecho

# Definición de la clase BinarySearchTree
class BinarySearchTree:
    def __init__(self):
        self.root = None  # El árbol inicialmente está vacío

    # Método para insertar un nuevo dato en el árbol
    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursive(node.right, data)

    # Método para buscar un dato en el árbol
    def search(self, target):
        return self._search_recursive(self.root, target)

    def _search_recursive(self, node, target):
        if node is None:
            return False
        if node.data == target:
            return True
        elif target < node.data:
            return self._search_recursive(node.left, target)
        else:
            return self._search_recursive(node.right, target)

    # Método para recorrer el árbol en orden (inorder) e imprimir los datos
    def inorder_traversal(self):
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        if node:
            self._inorder_recursive(node.left)
            print(node.data)
            self._inorder_recursive(node.right)

    # Funcionalidad extra: Buscar todas las ciudades que empiecen con un prefijo dado
    def search_by_prefix(self, prefix):
        results = []
        self._search_by_prefix_recursive(self.root, prefix, results)
        return results

    def _search_by_prefix_recursive(self, node, prefix, results):
        if node:
            if node.data.startswith(prefix):
                results.append(node.data)
            self._search_by_prefix_recursive(node.left, prefix, results)
            self._search_by_prefix_recursive(node.right, prefix, results)

# Ejemplo de uso
if __name__ == '__main__':
    city_tree = BinarySearchTree()

    # Insertar ciudades
    city_tree.insert("Ciudad C: Piedecuesta (7.1600, -73.1200)")
    city_tree.insert("Ciudad B: Floridablanca (7.1300, -73.0800)")
    city_tree.insert("Ciudad A: Bucaramanga (7.1254, -73.1198)")

    # Buscar una ciudad
    target = "Ciudad B: Floridablanca (7.1300, -73.0800)"
    found = city_tree.search(target)
    print(f"\n¿El elemento '{target}' fue encontrado?", found)

    # Mostrar todas las ciudades en orden
    print("\nCiudades en orden alfabético:")
    city_tree.inorder_traversal()

    # Funcionalidad adicional: buscar ciudades por prefijo
    prefix = "Ciudad B"
    matches = city_tree.search_by_prefix(prefix)
    print(f"\nCiudades que comienzan con '{prefix}':")
    for match in matches:
        print(match)