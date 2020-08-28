import imagematrix

class ResizeableImage(imagematrix.ImageMatrix):
    def best_seam(self):
        
        dic={}
        j_max=self.height-1
        for i in range(self.width):
            dic[(i,j_max)]={'parent':None, 'energy_path':self.energy(i,j_max)}
            
        #setup initial base now need to go through all locations above that
        for i in range(self.width):
            for j in range(self.height-2,0,-1):
                parent=self.min_parent(i,j,dic)
                energy=self.energy(i,j)+dic[parent]['energy_path']
                dic[(i,j)]={'parent':parent, 'energy_path':energy}
        
        min_pos=None
        for i in range(self.width):
            parent=self.min_parent(i,0,dic)
            energy=self.energy(i,0)+dic[parent]['energy_path']
            dic[(i,j)]={'parent':parent, 'energy_path':energy}
            if not min_pos:
                min_pos=(i,0)
                continue
            if dic[(i,0)]['energy_path']<dic[min_pos]['energy_path']:
                min_pos=(i,0)
        
        seam=[]
        seam.append(min_pos)
        while dic[min_pos]['parent']:
            min_pos=dic[min_pos]['parent']
            seam.append(min_pos)
        
        return seam
                
            
    def min_parent(self, i,j,dic):
        
        allowed_parents=[(a,j+1) for a in range(i-1,i+2) if 0<=i<self.width]
        min_p=None
        for parent in allowed_parents:
            if not min_p:
                min_p=parent
                continue
            if dic[parent]['energy_path']<dic[min_p]['energy_path']:
                min_p=parent
        return min_p
             
        
    def remove_best_seam(self):
        self.remove_seam(self.best_seam())
