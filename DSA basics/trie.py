class trieNode:
    def __init__(this,char = "*"):
        this.char = char
        this.children = {}
        this.wordFinished = True
        this.counter = 1
    
    def add(this,word):
        node = this
        for char in word:
            found_in_child = False
            for child in node.children:
                if child.char == char:
                    node = child
                    found_in_child = True
                    node.counter += 1
                    break
            if not found_in_child:
                new_node = trieNode(char)
                node.children.append(new_node)
                node = new_node
        node.wordFinished = True
        return node
    
    def add_word(this, word):
            node = this
            for c in word:
                if c not in node.children:
                    node.children[c] = trieNode()
                node = node.children[c]
            node.wordFinished = True
        
    def wordPresent(this,word):
        node = this
        for char in word:
            isPresent = False
            for child in node.children:
                
                if char == child.char:
                    isPresent = True
                    node = child
                    print(char)
                    break
            
            if isPresent == False:
                return "not Found"
            
        return "Found"