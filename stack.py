class Stack:

    def __init__(self, * items):
        self.data = []
        if len(items) > 0:
            for item in items:
                self.push(item)

    def push(self, item):
        self.data.append(item)
    
    def pop(self):
        return self.data.pop()

    def len(self):
        count = 0
        for item in self.data:
            count += 1
        return count
    
    def removeCentral(self):
        size = contar(self.data)
        # Pilha vazia!
        if size == 0:
            return None
        rem = None
        # Criar pilha temporária
        tempStack = Stack()
        # Verificar se é par ou ímpar
        if size % 2 == 0:
            # É par!
            for i in range((size / 2) - 1):
                aux = self.pop()
                tempStack.push(aux)
            # Identifica maior
            c1 = self.pop()
            c2 = self.pop()
            if c1 > c2:
                rem = c1
                self.push(c2)
            else:
                rem = c2
                self.push(c1)
        else:
            # É ímpar!
            for i in range(size // 2):
                aux = self.pop()
                tempStack.push(aux)
            # Remove central
            rem = self.pop()
        # Re-empilha
        for i in range(tempStack.len()):
            aux = tempStack.pop()
            self.push(aux)
        return rem