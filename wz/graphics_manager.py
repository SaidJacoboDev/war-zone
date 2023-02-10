class GraphicsManager():

    def __init__(self):
        self.all_objects = []
        self.object_tags  = {}
    
    def add_object(self, object):
        if object.type in self.object_tags.keys():
            self.object_tags[object.type].append(object)
        else:
            self.object_tags[object.type] = [object]

        self.all_objects.append(object)


    def update(self):
        for object in self.all_objects:
            alive = object.update()

            if not alive:
                self.remove_object([object])

    def draw(self):
        for object in self.all_objects:
            object.draw()
            

    def check_collision(self, type_1, type_2):
        type_1_elements = None
        type_2_elements = None

        if type_1 in self.object_tags.keys():
            type_1_elements = self.object_tags[type_1]
        
        if type_2 in self.object_tags.keys():
            type_2_elements = self.object_tags[type_2]

        if not type_1_elements or not type_2_elements:
            return None, None

        collide_type_1_elements = []
        collide_type_2_elements = []

        for type_1_element in type_1_elements:
            for type_2_element in type_2_elements:
                if type_2_element.rect.colliderect(type_1_element.rect):
                    collide_type_1_elements.append(type_1_element)
                    collide_type_2_elements.append(type_2_element)
        return collide_type_1_elements, collide_type_2_elements

    def remove_object(self, objects):
        for object in objects:
            if object in self.all_objects:
                self.all_objects.remove(object)
                self.object_tags[object.type].remove(object)
