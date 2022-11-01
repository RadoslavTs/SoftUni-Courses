class Catalogue:
    products = []

    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        temp_list = []
        for sequence in self.products:
            if sequence[0] == first_letter:
                temp_list.append(sequence)
        return temp_list

    def __repr__(self):
        self.products.sort()
        return "Items in the {0} catalogue:\n" \
               "{1}".format(self.name, '\n'.join(self.products))


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)