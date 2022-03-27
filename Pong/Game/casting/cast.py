class Cast:
    

    def __init__(self):
        
        self._actors = {}
        
    def add_actor(self, group, actor):
        
        if not group in self._actors.keys():
            self._actors[group] = []
            
        if not actor in self._actors[group]:
            self._actors[group].append(actor)

    def get_actors(self, group):
       
        results = []
        if group in self._actors.keys():
            results = self._actors[group].copy()
        return results
    
    def get_all_actors(self):
        
        results = []
        for group in self._actors:
            results.extend(self._actors[group])
        return results

    def get_first_actor(self, group):
        
        result = None
        if group in self._actors.keys():
            result = self._actors[group][0]
        return result

    def remove_actor(self, group, actor):
        
        if group in self._actors:
            self._actors[group].remove(actor)

    def reset_actor_group(self, group):

        if group in self._actors:
            for actor in self._actors[group]:
                self._actors[group].remove(actor)

    def remove_all_actors(self):
            self._actors.clear()
