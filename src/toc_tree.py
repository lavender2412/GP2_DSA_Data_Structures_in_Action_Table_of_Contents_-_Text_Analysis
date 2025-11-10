#create node class
class Node:
    def __init__(self, book, section, title, page):
        self.section = section
        self.title = title
        self.page = page
        self.book = book
        #create section order, count of periods in section + 1
        self.section_order = section.count(".") + 1 if section else 0
        self.total = 0
        self.children = []

    #assumes sorted table of contents
    def insert_section(self, section, title, page):
        new_section = Node(self.book, section, title, page)
        new_order = new_section.section_order
        #if section order is 1 greater than root/current node, appending to current node's children
        if new_order == self.section_order + 1:
            self.children.append(new_section)
            #increment total nodes
            self.total += 1
            return new_section
        #if not a direct child, loop through each child node
        for children in self.children:
            #check if child is in section lineage
            if section.startswith(children.section + "."):
                #if so, recurse with child node
                inserted = children.insert_section(section, title, page)
                #increment total nodes
                if inserted:
                    self.total+=1
                return inserted
        print(f"Could not add {new_section.title}, {new_section.section}")

    #loop through cleaned list of contents
    def insert_many(self, arr):
        for val in arr:
            self.insert_section(val[0], val[1], val[2])

    def print_toc(self, mode):
      # will store the values in list instead of printing them all
        lines = []

        def traverse(node, chapter_hierarchy, level):
            if node.title:
                number_str = ".".join(str(num) for num in chapter_hierarchy)
                indent = "  " * level
                if mode == "plain":
                    lines.append(node.title)
                elif mode == "indented":
                    lines.append(indent + node.title)
                elif mode == "numbered":
                    lines.append(indent + (f"{number_str} " if number_str else "") + node.title)

            for i, child in enumerate(node.children, 1):
                traverse(child, chapter_hierarchy + [i], level + 1)

        traverse(self, [], 0)
        return lines

    def show_toc(book, mode):
        toc_lines = book.print_toc(mode)
        html_block = "<br>".join(toc_lines)
        display(HTML(f"""<div style="max-height: 400px; overflow-y: auto; white-space: pre; font-family: monospace;">{html_block}</div>"""))


    def tree_height(self):
        #initialize empty array
        heights_arr = []
        #check for children of root/current node
        if self.children:
            #iterate over each child node
            for children in self.children:
                #recurse to each leaf
                height = children.tree_height()
                #after recursion, append height of each leaf
                heights_arr.append(height)
        #base case - return 0 because root node has height 0
        else:
            return 0
        #return max height + 1 to increment each recurion
        return 1 + max(heights_arr)

    def tree_depth(self, title):
        #using dfs approach here
        if self.book == title:
          return 0
        def dfs(node, depth):
            if node.title == title:
                return depth
            for child in node.children:
                result = dfs(child, depth + 1)
                if result is not None:
                    return result
            return None
        return dfs(self, 0)