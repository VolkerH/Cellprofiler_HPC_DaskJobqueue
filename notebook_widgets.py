import os
import ipywidgets as widgets

# The FileBrowser class is from GitHub user DrDub:
# https://gist.github.com/DrDub/6efba6e522302e43d055
class FileBrowser(object):
    def __init__(self, path=None):
        if path is None:
            self.path = os.getcwd()
        else:
            self.path = path
        self._update_files()
        
    def _update_files(self):
        self.files = list()
        self.dirs = list()
        if(os.path.isdir(self.path)):
            for f in os.listdir(self.path):
                ff = self.path + "/" + f
                if os.path.isdir(ff):
                    self.dirs.append(f)
                else:
                    self.files.append(f)
        
    def widget(self):
        box = widgets.VBox()
        self._update(box)
        return box
    
    def _update(self, box):
        
        def on_click(b):
            if b.description == '..':
                self.path = os.path.split(self.path)[0]
            else:
                self.path = self.path + "/" + b.description
            self._update_files()
            self._update(box)
        
        buttons = []
        if self.files:
            button = widgets.Button(description='..', background_color='#d0d0ff')
            button.on_click(on_click)
            buttons.append(button)
        for f in self.dirs:
            button = widgets.Button(description=f, background_color='#d0d0ff')
            button.on_click(on_click)
            buttons.append(button)
        for f in self.files:
            button = widgets.Button(description=f)
            button.on_click(on_click)
            buttons.append(button)
        box.children = tuple([widgets.HTML("<h2>%s</h2>" % (self.path,))] + buttons)
               


# It may look strange to create these widgets 
# here, but I want to keep the notebook readable for non-programmers
            
            
# Walltime
# Sliders for batch size and time per image set
style = {'description_width': 'initial'}
time_per_im = widgets.IntSlider(description='time_per_image (min):', value=5, min=1, max=30,style=style)
im_per_batch = widgets.IntSlider(description='images_per_batch:', value=20, min=1, max=300, style=style)
h = widgets.HTML('<b>Walltime</b> {}*{} = {} min'.format(im_per_batch.value, time_per_im.value, 
                                                         im_per_batch.value*time_per_im.value))
def walltime_calc(t, n):
    h.value = '<b>Walltime</b> {}*{} = {} min'.format(n, t, n*t)
    
out = widgets.interactive_output(walltime_calc, {'t': time_per_im, 'n': im_per_batch})
walltime_chooser = widgets.VBox([im_per_batch, time_per_im, h])

# Nr Nodes, GB of RAM
nr_cpus = widgets.IntSlider(description='CPUs per node:', value=1, min=1, max=10,style=style)
gb_of_RAM = widgets.IntSlider(description='GB of RAM per Worker:', value=4, min=1, max=256,style=style)
resource_chooser = widgets.VBox([nr_cpus, gb_of_RAM])

# BatchfileChooser
batchfile = FileBrowser()

# CSV folder browsers
csv_folder = FileBrowser()
concat_csv_folder = FileBrowser()
