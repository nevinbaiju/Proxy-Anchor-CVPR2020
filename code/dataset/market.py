from base import *

class Market(BaseDataset):
    def __init__(self, root, mode, transform = None):
        self.root = root
        self.mode = mode

        gt_bbox = [os.path.join(self.root, 'gt_bbox', x) for x in os.listdir(os.path.join(self.root, 'gt_bbox'))]
        bbox_train = [os.path.join(self.root, 'bounding_box_train', x) for x in os.listdir(os.path.join(self.root, 'gt_bbox'))]
        train_images = gt_bbox + bbox_train
        
        self.transform = transform
        if self.mode == 'train':
            self.classes = range(0,1000)
        elif self.mode == 'eval':
            self.classes = range(1000,1501)
                
        BaseDataset.__init__(self, self.root, self.mode, self.transform)
        
        ys = [int(image.split('/')[-1].split('_')[0]) for image in train_images[:4]]
        index = 0
        self.im_paths = []
        for im_path, y in zip(train_images, ys):
            if y in self.classes: # choose only specified classes
                self.im_paths.append(im_path)
                self.ys.append(y)
                self.I += [index]
                index += 1